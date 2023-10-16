import os
import yaml
import json
from datetime import datetime

def set_default(d, key, default_value):
    if not isinstance(d, dict):
        return
    d.setdefault(key, default_value)

# Read existing publiccode.yaml
try:
    with open("publiccode.yaml", "r") as f:
        data = yaml.safe_load(f)
except FileNotFoundError:
    data = {}

# Convert created_at to date format
created_at_date = datetime.now().strftime('%Y-%m-%d')

# Initialize missing keys with default values
set_default(data, 'publiccodeYmlVersion', "0.2")
set_default(data, 'name', "")
set_default(data, 'url', "")
set_default(data, 'description', {'en': {}})

# Update or append values
if os.environ.get('REPO_NAME'):
    data['name'] = os.environ['REPO_NAME']
if os.environ.get('REPO_URL'):
    data['url'] = os.environ['REPO_URL']

# Check if 'description' is a string and convert it to a dictionary if needed
if not isinstance(data['description'], dict):
    data['description'] = {'en': {}}

if os.environ.get('REPO_DESC'):
    data['description']['en']['genericName'] = os.environ['REPO_DESC']

if os.environ.get('REPO_HOMEPAGE'):
    data['url'] = os.environ['REPO_HOMEPAGE']

# Uncomment this if you plan to use REPO_TOPICS
# if os.environ.get('REPO_TOPICS'):
#     data['topics'] = os.environ['REPO_TOPICS'].split(',')

if os.environ.get('REPO_LICENSE'):
    data['license'] = os.environ['REPO_LICENSE']

# Create or update nested 'organisation' array
if 'organisation' not in data:
    data['organisation'] = {}

if os.environ.get('ORGANISATION_NAME'):
    data['organisation']['name'] = os.environ['ORGANISATION_NAME']
if os.environ.get('ORGANISATION_AVATAR'):
    data['organisation']['logo'] = os.environ['ORGANISATION_AVATAR']
if os.environ.get('ORGANISATION_URL'):
    data['organisation']['url'] = os.environ['ORGANISATION_URL']
if os.environ.get('ORGANISATION_DESCRIPTION'):
    data['organisation']['description'] = os.environ['ORGANISATION_DESCRIPTION']

# Write updated publiccode.yaml
with open("publiccode.yaml", "w") as f:
    yaml.safe_dump(data, f)
