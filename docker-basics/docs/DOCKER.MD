# Docker — Daily Commands

```bash
# Build
docker build -t <name>:<tag> .

# Run
docker run <name>:<tag>
docker run -d -p 8000:8000 <name>:<tag>     # background + port mapping
docker run --rm <name>:<tag>                 # auto-remove after exit

# See what's running / what exists
docker ps                # running containers
docker ps -a              # all containers, including stopped
docker images             # all images

# Logs
docker logs <container>
docker logs -f <container>   # follow, like tail -f

# Get inside a running container
docker exec -it <container> bash

# Stop / remove
docker stop <container>
docker rm <container>
docker rmi <name>:<tag>

# Cleanup when things pile up
docker container prune
docker image prune
```

**Daily loop while developing:**
```bash
docker build -t <name>:<tag> .
docker run --rm <name>:<tag>
```
Rebuild every time you change code — `docker run` never picks up file edits on its own.