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

# Add releaseDate if not present
if 'releaseDate' not in data:
  data['releaseDate'] = created_at_date

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

# Create or update nested 'nl' array
if 'nl' not in data:
  data['nl'] = {}

# Write updated publiccode.yaml
with open("publiccode.yaml", "w") as f:
  yaml.safe_dump(data, f)
END
