import requests
import json

# Read Builder Config from file:
json_text = ""
with open("builder.json", "r") as build_file:
    json_text = build_file.read()

BUILDER_CONFIG = json.loads(json_text)

# Concatenate all of the files.
new_data = ""
for fname in BUILDER_CONFIG["buildOrder"]:
    with open(f"{BUILDER_CONFIG['inDir']}/{fname}.css", 'r') as file:
        new_data = f"{new_data}\n{file.read()}"
        print(f"Added {fname} to bundle...")

# Unvariablize CSS vars:
for name, value in BUILDER_CONFIG["cssVars"].items():
    new_data = new_data.replace(f"var(--{name})", value)

# Write unminified bundle to file.
with open(f"{BUILDER_CONFIG['outDir']}/{BUILDER_CONFIG['outFilename']}.css", "w") as outfile:
    outfile.write(new_data)
    print("Wrote bundle to file...")

# Minify bundle/write to file.
print("Minifying bundle...")

url = 'https://cssminifier.com/raw'
data = {'input': new_data }
response = requests.post(url, data=data)

with open(f"{BUILDER_CONFIG['outDir']}/{BUILDER_CONFIG['outFilename']}.min.css", "w") as min_outfile:
    min_outfile.write(response.text)
    print("Wrote minified css to file...")



