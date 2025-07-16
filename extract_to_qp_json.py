import os
import json
import re
import urllib.parse

# GitHub repo info
GITHUB_USERNAME = "kalvikraft"
REPO_NAME = "kalvi-kraft"
BRANCH = "main"

# Paths
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

        # Encode the filename for URL safety
        encoded_filename = urllib.parse.quote(filename)

        download_url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/{BRANCH}/{input_folder}/{encoded_filename}"

        data.append({
            "university": university.strip(),
            "month": month.strip(),
            "year": int(year),
            "subject": subject.strip(),
            "filename": filename,
            "download_url": download_url
        })
    else:
        print(f"⚠️ Skipped invalid filename: {filename}")

# Write JSON
with open(output_file, "w") as f:
    json.dump(data, f, indent=4)

print(f"✅ JSON written to {output_file}")
