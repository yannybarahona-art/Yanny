import csv
#! CSV files
[{
    ""
}]
with open("source/example.csv", "r", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(f"{row['name']}, {row['age']}, {row['city']}")
        
        