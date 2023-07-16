# .github/scripts/update_publiccode.py

import os
import yaml
import warnings

# Check the metadata of the repository
# For the simplicity, we're assuming that the metadata are environment variables
# In a real case, you would fetch the metadata from the repository or other sources

# Metadata variables
variables = [
    "GITHUB_REPOSITORY", 
    "REPO_DESCRIPTION", 
    "ORGANISATION", 
    "TAGS", 
    "WEBSITE", 
    "LICENCE"
]

# Create a dictionary to hold the metadata
metadata = {}

# Check if each variable is set and if not, issue a warning
for var in variables:
    value = os.getenv(var)
    if value:
        metadata[var] = value
    else:
        warnings.warn(f"The {var} environment variable is not set")

# Always set the repository url
metadata["REPO_URL"] = f"https://github.com/{metadata.get('GITHUB_REPOSITORY', 'default_repo_name')}"

# Read the current publiccode.yaml (if exists)
try:
    with open("publiccode.yaml", "r") as file:
        publiccode = yaml.safe_load(file)
except FileNotFoundError:
    publiccode = {}

# Update the publiccode with the new metadata
publiccode["publiccode"] = publiccode.get("publiccode", {})
publiccode["publiccode"]["name"] = metadata.get("GITHUB_REPOSITORY")
publiccode["publiccode"]["description"] = {
    "nl": metadata.get("REPO_DESCRIPTION")
}
publiccode["publiccode"]["url"] = metadata.get("REPO_URL")
publiccode["publiccode"]["tags"] = metadata.get("TAGS")
publiccode["publiccode"]["website"] = metadata.get("WEBSITE")
publiccode["publiccode"]["license"] = metadata.get("LICENCE")
publiccode["publiccode"]["owner"] = metadata.get("ORGANISATION")

# Write back the publiccode.yaml
with open("publiccode.yaml", "w") as file:
    yaml.safe_dump(publiccode, file)
