# .github/scripts/update_publiccode.py

import yaml
import json
from datetime import datetime

# Read existing publiccode.yaml
try:
  with open("publiccode.yaml", "r") as f:
      data = yaml.safe_load(f)
except FileNotFoundError:
  data = {}

# Convert created_at to date format
# created_at_date = datetime.fromisoformat("$REPO_CREATED_AT".replace("Z", "+00:00")).strftime('%Y-%m-%d')
created_at_date = datetime.now().strftime('%Y-%m-%d')

# Convert topics JSON string to Python list and then to comma-separated string

################################################
# Creating a publiccode array if it is missing #
################################################

# Lets see if we have an nice exmple publiccode and values if they are missing
if 'publiccodeYmlVersion' not in data:
  data['publiccodeYmlVersion'] = "0.2"
if 'name' not in data:
  data['name'] = ""
if 'url' not in data:
  data['url'] = ""
if 'landingURL' not in data:
  data['landingURL'] = ""
if 'softwareVersion' not in data:
  data['softwareVersion'] = ""
if 'releaseDate' not in data:
  data['releaseDate'] = created_at_date
if 'platforms' not in data:
  data['platforms'] = ["web"]
if 'categories' not in data:
  data['categories'] = ["it-development"]
if 'usedBy' not in data:
  data['usedBy'] = []
if 'roadmap' not in data:
  data['roadmap'] = ""
if 'developmentStatus' not in data:
  data['developmentStatus'] = "development"
if 'softwareType' not in data:
  data['softwareType'] = "standalone/web"

# Description
if 'description' not in data:
  data['description'] = {"en":[]}
if 'en' not in data['description']:
  data['description']['en'] = []
if 'nl' not in data['description']:
  data['description']['nl'] = []
if 'shortDescription' not in data['description']['en']:
  data['description']['en']['localisedName'] = ""
  data['description']['en']['genericName'] = ""
  data['description']['en']['shortDescription'] = ""
  data['description']['en']['longDescription'] =""
  data['description']['en']['documentation'] = ""
  data['description']['en']['apiDocumentation'] = ""
  data['description']['en']['features'] = []
  data['description']['en']['screenshots'] = []
  data['description']['en']['videos'] = []
  data['description']['en']['awards'] = []

# Legal
if 'legal' not in data:
  data['legal'] = []
if 'license' not in data['legal']:
  data['legal']['license'] = ""
if 'mainCopyrightOwner' not in data['legal']:
  data['legal']['mainCopyrightOwner'] = ""
if 'repoOwner' not in data['legal']:
  data['legal']['repoOwner'] = ""
if 'authorsFile' not in data['legal']:
  data['legal']['authorsFile'] = ""

# Maintenance
if 'maintenance' not in data:
  data['maintenance'] = []
if 'type' not in data['maintenance']:
  data['maintenance']['type'] = "none"
if 'contractors' not in data['maintenance']:
  data['maintenance']['contractors'] = []
if 'contacts' not in data['maintenance']:
  data['maintenance']['contacts'] = []

# Localisation
if 'localisation' not in data:
  data['localisation'] = []
if 'localisationReady' not in data['localisation']:
  data['localisation']['localisationReady'] = false
if 'availableLanguages' not in data['localisation']:
  data['localisation']['availableLanguages'] = ["en"]

# NL Specific
if 'nl' not in data:
  data['nl'] = []
## Lets do GEMMA and Commen Ground
if 'vng' not in data['nl']:
  data['nl']['vng'] = []
if 'gemma' not in data['nl']['vng']:
  data['nl']['vng']['gemma'] = []
if 'commenground' not in data['nl']['vng']:
  data['nl']['vng']['commenground'] = []

###########################################
# Updating the values from the repository #
###########################################

# Update or append values
if "$REPO_NAME" != "null" and "$REPO_NAME":
  data['name'] = "$REPO_NAME"
if "$REPO_URL" != "null" and "$REPO_URL":
  data['url'] = "$REPO_URL"
if "$REPO_DESC" != "null" and "$REPO_DESC":
  data['description'] = "$REPO_DESC"
if "$REPO_HOMEPAGE" != "null" and "$REPO_HOMEPAGE":
  data['url'] = "$REPO_HOMEPAGE"
#if "$REPO_TOPICS" != "null" and "$REPO_TOPICS":
#    data['topics'] = "$REPO_TOPICS"
if "$REPO_LICENSE" != "null" and "$REPO_LICENSE":
  data['license'] = "$REPO_LICENSE"

# Create or update nested 'organisation' array
if 'organisation' not in data:
  data['organisation'] = {}
if "$ORGANISATION_NAME" != "null" and "$ORGANISATION_NAME":
  data['organisation']['name'] = "$ORGANISATION_NAME"
if "$ORGANISATION_AVATAR" != "null" and "$ORGANISATION_AVATAR":
  data['organisation']['logo'] = "$ORGANISATION_AVATAR"
if "$ORGANISATION_URL" != "null" and "$ORGANISATION_URL":
  data['organisation']['url'] = "$ORGANISATION_URL"
if "$ORGANISATION_DESCRIPTION" != "null" and "$ORGANISATION_DESCRIPTION":
  data['organisation']['description'] = "$ORGANISATION_DESCRIPTION"

# Write updated publiccode.yaml
with open("publiccode.yaml", "w") as f:
  yaml.safe_dump(data, f)
