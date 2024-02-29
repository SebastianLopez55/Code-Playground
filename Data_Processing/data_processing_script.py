import pandas as pd
import csv

input_file_path = "/Users/sebastianlopez/Development-git/Coding_Interviews/Code_Playground/Data_Processing/jobs_list.txt"
output_csv_path = "/Users/sebastianlopez/Development-git/Coding_Interviews/Code_Playground/Data_Processing/jobs_table.csv"

data = []

with open(input_file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 2:
            data.append(parts)

with open(output_csv_path, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Company", "Status"])
    writer.writerows(data)

print("Script Completed")
