import os
import json
import re

# Input/output folders
input_folder = "old-question-papers"
output_folder = "json"
output_file = os.path.join(output_folder, "old-qps.json")

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Match pattern: University-Month Year-Subject.ext
pattern = re.compile(r"^(.*?)\s*-\s*(\w+)\s+(\d{4})\s*-\s*(.*?)\.\w+$")

data = []

for filename in os.listdir(input_folder):
    match = pattern.match(filename)
    if match:
        university, month, year, subject = match.groups()
        data.append({
            "university": university.strip(),
            "month": month.strip(),
            "year": int(year),
            "subject": subject.strip(),
            "filename": filename
        })
    else:
        print(f"⚠️ Skipped invalid filename: {filename}")

# Write to JSON
with open(output_file, "w") as f:
    json.dump(data, f, indent=4)

print(f"✅ JSON written to {output_file}")
