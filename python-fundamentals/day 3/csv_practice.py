import csv

with open("score.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name","score"])
    writer.writerow(["Anubhav","70"])
    writer.writerow(["Supriya","200"])
    writer.writerow(["Rakesh","300"])
if __name__ == "__main__":

    with open("score.csv","r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

    with open("score.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["score"]) > 85:
                print(row["name"], row["score"])