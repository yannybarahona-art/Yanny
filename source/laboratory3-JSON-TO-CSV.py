import json
import csv

with open("source/API.json", "r") as f:
    data = json.load(f)

with open("source/API.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=data["results"][0].keys())
    writer.writeheader()
    writer.writerows(data["results"])