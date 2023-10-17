# Publiccode Action
This GitHub Action automatically generates and updates a `publiccode.yaml` file in the root of your repository, based on repository metadata. The file is updated each time a push is made to the main branch. It is basically a more advanced varsion of [the publiccode softwareversion check](https://github.com/italia/publiccode-softwareversion-check-action/tree/master)

The Action works by running a Python script that reads repository metadata such as the repository name and description, and uses this information to create or update the publiccode.yaml file.

## Usage
To use this action, simply include it as a step in your workflow file. No inputs are required.

````yaml
name: My PublicCode Workflow

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Update publiccode.yaml
        uses: OpenCatalogi/publiccode-action@latest
````

In the above example a `publiccode` file is updated every time code on the `main` branche is touched

## Inputs

| Input Name   | Description                                                  | Default Value        |
|--------------|--------------------------------------------------------------|-----------------------|
| `name` | Git URL of the remote repository to check (Optional)         | {{ github.event.repository.name }}"         |
| `description` | Git URL of the remote repository to check (Optional)         | Empty String          |
| `remoterepo` | Git URL of the remote repository to check (Optional)         | Empty String          |
| `publiccode` | `publiccode.yml` path (Optional), e.g. `data/publiccode.yml` | `publiccode.yml`      |
| `gitname`    | Git name configuration for bump commit (Optional)            | `Open Catalogi bot`  |
| `gitmail`    | Git mail configuration for bump commit (Optional)            | `bot@opencatalogi.nl` |


## Outputs
The following outputs are provided by the action and can be used by other actions. 

| Output Name    | Description                                     |
|----------------|-------------------------------------------------|
| `version`      | New version of the `softwareVersion` field     |
| `releaseDate`  | New release date of the `releaseDate` field   |

## Example
To use this action, simply include it as a step in your workflow file. No inputs are required.

````yaml
steps:
  - name: Update publiccode.yaml
    uses: OpenCatalogi/publiccode-action
    with:
      name: "My Codebase"
      description: "This is a sample repository description"
      publiccode: "publiccode.yml"
      gitname: "Open Catalogi bot"
      gitmail: "bot@opencatalogi.nl"
````
Note: Replace `your-github-username` with your actual GitHub username, and `publiccode-update-action` with the name of the repository where this action is hosted.

## Architecture
### Why Python?
Python is natively supported by GitHub actions' underlaying containers and therefore very quick

### Asumptions
We follow the "get data from the source" principle, in practice for this action that means that we set the repository as the source. So any settings in the repository (e.g. name and description) will overwrite the values already pressent in your publiccode.

Please note that this action does not handle errors or exceptions while reading metadata or writing to publiccode.yaml. You should ensure that your repository is properly set up to avoid any issues. For example, make sure that your repository name and description are not empty.
