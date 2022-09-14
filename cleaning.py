import pandas as pd
import csv

df = pd.read_csv("merged_stars.csv")

with open("merged_stars.csv") as input, open("final_stars.csv", 'w', newline="") as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)