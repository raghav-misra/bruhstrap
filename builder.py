# BUILDER CONFIGURATION
BUILDER_CONFIG = {
    "IN_DIR": "src",
    "OUT_DIR": "dist",
    "OUT_NAME": "bruhstrap",
    "BUILD_ORDER": [
        "main", "defaults", "utils", "layout", "elements", "transitions"
    ]
}
# END BUILDER CONFIGURATION
import requests

new_data = ""
for fname in BUILDER_CONFIG["BUILD_ORDER"]:
    with open(f"{BUILDER_CONFIG['IN_DIR']}/{fname}.css", 'r') as file:
        new_data = f"{new_data}\n{file.read()}"
        print(f"Added {fname} to bundle...")

with open(f"{BUILDER_CONFIG['OUT_DIR']}/{BUILDER_CONFIG['OUT_NAME']}.css", "w") as outfile:
    outfile.write(new_data)
    print("Wrote bundle to file...")

print("Minifying bundle...")


url = 'https://cssminifier.com/raw'
data = {'input': new_data }
response = requests.post(url, data=data)

with open(f"{BUILDER_CONFIG['OUT_DIR']}/{BUILDER_CONFIG['OUT_NAME']}.min.css", "w") as min_outfile:
    min_outfile.write(response.text)
    print("Wrote minified css to file...")



