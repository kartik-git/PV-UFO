import csv
import json
import pandas as pd

csv_file = 'excelinput.csv'

# use pandas to read the first column and get all the files names
df = pd.read_csv(csv_file)
file_names = df.iloc[:, 0].tolist()

print(file_names)
# Create a blank JSON file with the corresponding file names
data = {}
for file_name in file_names:
    file_name = file_name.replace(" ", "_").replace("/", "_").replace(":", "_").replace("\\", "_").replace(".", "_").replace(",", "_").replace(";", "_").replace("?", "_").replace("!", "_").replace("'", "_").strip()
    json_file = f"{file_name}.json"
    with open(json_file, 'w') as file:
        json.dump({}, file, indent=4)