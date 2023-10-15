# .github/scripts/update_publicorganisation.py

import yaml
import json
from datetime import datetime

# Read existing openCatalogi.yaml
try:
  with open("openCatalogi.yaml", "r") as f:
      data = yaml.safe_load(f)
except FileNotFoundError:
  data = {}

if "$ORGANISATION_NAME" != "null" and "$ORGANISATION_NAME":
  data['name'] = "$ORGANISATION_NAME"
if "$ORGANISATION_AVATAR" != "null" and "$ORGANISATION_AVATAR":
  data['logo'] = "$ORGANISATION_AVATAR"
if "$ORGANISATION_URL" != "null" and "$ORGANISATION_URL":
  data['url'] = "$ORGANISATION_URL"
if "$ORGANISATION_DESCRIPTION" != "null" and "$ORGANISATION_DESCRIPTION":
  data['description'] = "$ORGANISATION_DESCRIPTION"

# Create or update nested 'nl' array
if 'nl' not in data:
  data['nl'] = {}

# Write updated openCatalogi.yaml
with open("openCatalogi.yaml", "w") as f:
  yaml.safe_dump(data, f)
END