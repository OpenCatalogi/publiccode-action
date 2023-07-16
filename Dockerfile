FROM python:3.9-slim

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY update_publiccode.py /update_publiccode.py

# Executes `update_publiccode.py` when the Docker container starts up
ENTRYPOINT ["python3", "/update_publiccode.py"]
