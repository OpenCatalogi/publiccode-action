# Publiccode Action
This GitHub Action automatically generates and updates a publiccode.yaml file in the root of your repository, based on repository metadata. The file is updated each time a push is made to the main branch. It is basically a more advanced varsion of [the publiccode softwareversion check](https://github.com/italia/publiccode-softwareversion-check-action/tree/master)

The Action works by running a Python script that reads repository metadata such as the repository name and description, and uses this information to create or update the publiccode.yaml file.

## Usage
To use this action, simply include it as a step in your workflow file. No inputs are required.

````yaml
steps:
  - name: Update publiccode.yaml
    uses: OpenCatalogi/publiccode-action@v1
    env:
      GITHUB_REPOSITORY: ${{ github.repository }}
      REPO_DESCRIPTION: "This is a sample repository description"
      ORGANISATION: "OpenAI"
      TAGS: "ai, machine-learning"
      WEBSITE: "https://openai.com"
      LICENCE: "MIT"
````
Note: Replace your-github-username with your actual GitHub username, and publiccode-update-action with the name of the repository where this action is hosted.

## Inputs
None

## Outputs
None

## Architecture
### Why python?
Python is nativly supported by github actions underlaying containers and therefore very quick

### Asumptions
We follow the "get data from teh source" princple

Please note that this action does not handle errors or exceptions while reading metadata or writing to publiccode.yaml. You should ensure that your repository is properly set up to avoid any issues. For example, make sure that your repository name and description are not empty.
