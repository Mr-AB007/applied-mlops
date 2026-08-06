# Day 6 — Docker Fundamentals (Java → Python)
**Topics:** Containers vs VMs, Dockerfile basics, building/running images, containerizing a simple Python app

This is your first real MLOps *tooling* day — everything before this was Python-the-language. From here on, most days are about the infrastructure layer that wraps around your model/code. Good news: Docker maps almost 1:1 onto things you already do with JARs and deployment, so this should move faster than Days 1-5.

---

## 1. The core idea — "it works on my machine" solved

You already know this problem from Java: a service runs fine locally, but breaks in prod because of a JVM version mismatch, a missing env var, an OS-level library difference, etc. You've probably fixed this before with a fat JAR + a documented runtime (specific JDK version, specific OS packages).

Docker's answer is more aggressive: instead of documenting the environment, you **package the entire environment** — OS layer, runtime, dependencies, code — into a single portable unit called an **image**. A **container** is a running instance of that image.

### The Java-equivalent mental model

| Java world | Docker world |
|---|---|
| `.jar` file | Docker **image** |
| `java -jar app.jar` (a running process) | a running **container** |
| JDK installed on the host machine | **base image** (e.g. `python:3.11-slim`) bundles the runtime *inside* the image |
| `MANIFEST.MF` / build config | **Dockerfile** — declarative build recipe |
| Maven/Gradle repo (Nexus, Artifactory) | **Docker registry** (Docker Hub, ECR, GCR) |
| `pom.xml` dependencies | `requirements.txt` installed during image build |

The key mental shift: a JAR still depends on *whatever JRE is already on the machine*. A Docker image needs nothing pre-installed on the host except Docker itself — the image carries its own mini-OS filesystem layer. That's the whole point.

### Containers vs Virtual Machines (quick clarification, since people conflate these)
A VM virtualizes an entire OS, including its own kernel — heavy, slow to boot (minutes), fully isolated. A container shares the host machine's kernel and only virtualizes the *user-space* (filesystem, processes, network) — lightweight, boots in ~seconds, and multiple containers share one kernel. This is why you can run 20 containers on a laptop but not 20 VMs.

---

## 2. Images vs Containers — precisely

- **Image** = a read-only, versioned template (like a class definition, or a compiled JAR sitting in a repo). It doesn't "run" — it's just bytes on disk describing a filesystem + a startup command.
- **Container** = a running (or stopped) instance created *from* an image (like an object instantiated from a class — `new MyImage()`). You can spin up multiple containers from the same image, each with its own isolated process/filesystem-diff, same way multiple threads can run the same JAR concurrently but with separate memory.

```bash
docker build -t my-app:1.0 .      # image: my-app:1.0  (compile the JAR)
docker run my-app:1.0             # container: a running instance (java -jar)
docker ps                         # list running containers (like `jps` for JVM processes)
```

---

## 3. The Dockerfile — your build recipe

Each line is a **layer**. Docker caches layers, so if you don't change a layer, it isn't rebuilt on the next `docker build` — this is directly analogous to Maven/Gradle's incremental build caching, or how your IDE doesn't recompile unchanged `.class` files.

```dockerfile
# Base image — like choosing your JDK version
FROM python:3.11-slim

# Working directory inside the container's filesystem
WORKDIR /app

# Copy dependency manifest FIRST, install, THEN copy code
# (this ordering matters — see "layer caching" below)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the actual application code
COPY . .

# Document which port the container listens on (informational only)
EXPOSE 8000

# The command that runs when the container starts
# (like the Main-Class entry in a JAR's manifest)
CMD ["python", "app.py"]
```

### Why `COPY requirements.txt` happens *before* `COPY . .`
This is the single most common Dockerfile mistake to avoid. Docker rebuilds a layer — and every layer *after* it — whenever the files it copies change. Your source code (`.py` files) changes constantly; your dependencies (`requirements.txt`) change rarely. If you `COPY . .` first and `pip install` second, **every single code change forces a full dependency reinstall** on every build. Copying the manifest first means `pip install` only re-runs when dependencies actually change — same instinct as why you wouldn't want Maven re-downloading the entire `.m2` repo on every code edit.

---

## 4. Building and running

```bash
# Build an image from the Dockerfile in the current directory, tag it "my-app:1.0"
docker build -t my-app:1.0 .

# Run a container from that image
docker run my-app:1.0

# Run it in the background (detached) and map host port 8000 -> container port 8000
docker run -d -p 8000:8000 my-app:1.0

# See what's currently running
docker ps

# Stop a running container
docker stop <container_id>

# View logs from a container (like tailing a log file)
docker logs <container_id>
```

### Port mapping — `-p host_port:container_port`
The container has its own isolated network namespace. If your Python app listens on port 8000 *inside* the container, nothing outside can reach it unless you explicitly map a host port to it. This is conceptually similar to configuring a reverse proxy or port forwarding for a Java service running inside a restricted environment — the container's internal port is invisible until you punch a hole through to it.

---

## 5. `.dockerignore` — like `.gitignore`, but for image builds

Anything matching patterns in `.dockerignore` never gets sent to the Docker build context, so it can't bloat the image or leak into it by accident.

```
.venv/
__pycache__/
*.pyc
.git/
.env
```

Same instinct as excluding `target/` or `.idea/` from a Java repo — don't ship build artifacts or local environment junk inside the image.

---

## 6. A quick note on image size

`python:3.11-slim` is deliberately a stripped-down base image (no compilers, no docs, minimal OS packages) versus the full `python:3.11` image. Smaller images pull faster, deploy faster, and have a smaller attack surface — same reasoning as preferring a minimal JRE base image over a full JDK-plus-tools image for a production Java container. Don't reach for `-slim` variants yet if you hit build errors requiring system packages (some ML libraries need compilers) — but default to `-slim` for simple apps like today's task.

---

## Today's Tasks

Create a new folder in your repo: `docker-basics/`.

1. **A minimal Python app** — `app.py`:
   - Write a tiny script (no need for a real web framework yet) that just prints a message and exits, e.g. `print("Hello from inside a container!")`.
   - Add one line using a package from `requirements.txt` (e.g. `import pandas as pd; print(pd.__version__)`) — this proves the container actually installed your dependencies, not just ran bare Python.

2. **`requirements.txt`** — just the one dependency you used above (e.g. `pandas`).

3. **Write a `Dockerfile`** in `docker-basics/`:
   - Use `python:3.11-slim` as the base.
   - Follow the correct layer order (requirements copied + installed *before* app code copied).
   - Set the `CMD` to run `app.py`.

4. **Write a `.dockerignore`** excluding at least `.venv/`, `__pycache__/`, and `.git/`.

5. **Build and run it:**
   - `docker build -t applied-mlops-day6:1.0 .`
   - `docker run applied-mlops-day6:1.0`
   - Confirm you see both print statements in the output.

6. **One-paragraph write-up** (add to a `NOTES.md` in the folder): in your own words, explain why `COPY requirements.txt` + `RUN pip install` happens *before* `COPY . .` in the Dockerfile. This is the one concept most people get wrong early on — writing it out yourself will cement it.

**Time estimate:** 1.5–2 hours (this should genuinely move faster than the pandas days — most of the friction is Docker Desktop/CLI setup, not concepts, given your deployment background).

---

**Tomorrow (Day 7 preview):** Wrapping a real prediction endpoint with **FastAPI**, then containerizing *that* — so the Docker skills from today get immediately reused on something that actually resembles a production ML service.