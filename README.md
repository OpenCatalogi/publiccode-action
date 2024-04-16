# Publiccode Action
This GitHub Action automatically generates and updates a `publiccode.yaml` file in the root of your repository, based on repository metadata. The file is updated each time a push is made to the main branch. It is basically a more advanced varsion of [the publiccode softwareversion check](https://github.com/italia/publiccode-softwareversion-check-action/tree/master)

The Action works by running a Python script that reads repository metadata such as the repository name and description, and uses this information to create or update the publiccode.yaml file.

## Usage
To use this action, simply include it as a step in your workflow file. No inputs are required.

````yaml
name: My PublicCode Workflow

permissions:
  contents: write

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

> **Info**
> Alternatively to setting the write permission for the workflow, you can also supply the action with an access token or an SSH key; see inputs for more details.

### Sending event to OpenCatalogi
This action also automatically sends an update message to the OpenCatalogi-API, so that the publiccode is reloaded by OpenCatalogi. However, the repository has to be indexed by GitHub for this to work properly the first time. This can be done by performing a search on the GitHub website in the repository, for example by searching `repo:{{your org/user}}/{{your repo}} publiccode` in the search bar on the GitHub website. This might take 10-15 minutes and several refreshes of the GitHub website.

## Working with protected branches
It is common (and good) practise to protect the main branche of a repository from direct file editing and only allowing this trough pull requests. This will however couse the action (and workflow containing it) to fail becouse the workflow won't have the rights to actually write or create the resulting publiccode or opencatalogi files to the repository.

The sollution here is two run the action two time's
1- Once on the protected branche with the setting `save` set on false to prevent actual file creation or allteration
2- Once on a branche where files may actually be added without a pull request (normally dev or development) setting `federlize` set on false to prevent unnececcery upates to the network


## Inputs

| Input Name   | Description                                                  | Default Value                            |
|--------------|--------------------------------------------------------------|------------------------------------------|
| `name` | Git URL of the remote repository to check (Optional)         | {{ github.event.repository.name }} <br/> |
| `description` | Git URL of the remote repository to check (Optional)         | Empty String                             |
| `remoterepo` | Git URL of the remote repository to check (Optional)         | Empty String                             |
| `publiccode` | `publiccode.yml` path (Optional), e.g. `data/publiccode.yml` | `publiccode.yml`                         |
| `federlize` | Wheter to send an update event to the federilized open catalogi network | true                                     |
| `save` | Wheter to actually save the file to github | true                                     |
| `gitname`    | Git name configuration for bump commit (Optional)            | `Open Catalogi bot`                      |
| `gitmail`    | Git mail configuration for bump commit (Optional)            | `bot@opencatalogi.nl`                    |

example ussage of the inputs

````yaml
name: My PublicCode Workflow

permissions:
  contents: write

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
        with:
          name: ${{ github.head_ref }}   # Git URL of the remote repository to check
          description: ${{ github.head_ref }}   # Git URL of the remote repository to check
          publiccode: docs/publiccode.yam   #  `publiccode.yml` path
          gitname:  bot myorganisation   # Git name configuration for bump commit
          gitmail: info@myorganisation.com   # Git mail configuration for bump commit
````

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
    uses: OpenCatalogi/publiccode-action@latest
    with:
      name: "My Codebase"
      description: "This is a sample repository description"
      publiccode: "publiccode.yml"
      gitname: "Open Catalogi bot"
      gitmail: "bot@opencatalogi.nl"
````
Note: Replace `your-github-username` with your actual GitHub username, and `publiccode-update-action` with the name of the repository where this action is hosted.

## Tips
Need a quick way to present your project online but don't have the time te create a dedicated website? Combine the publiccode code actions with the product page action to get an instant website for you project.

````yaml
name: My PublicCode Workflow

permissions:
  contents: write

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
      - name: Deploy Product Github Page
        uses: OpenCatalogi/productpage-action@latest
````

[Read more](https://github.com/marketplace/actions/create-an-product-page) about the product  page action

## Architecture
### Why Python?
Python is natively supported by GitHub actions' underlaying containers and therefore very quick

### Asumptions
We follow the "get data from the source" principle, in practice for this action that means that we set the repository as the source. So any settings in the repository (e.g. name and description) will overwrite the values already pressent in your publiccode.

Please note that this action does not handle errors or exceptions while reading metadata or writing to publiccode.yaml. You should ensure that your repository is properly set up to avoid any issues. For example, make sure that your repository name and description are not empty.

## Maintainers
This software is maintained by [Conduction b.v.](https://conduction.nl/)

## License
© 2023 Conduction B.V.

Licensed under the EUPL. The version control system provides attribution for specific lines of code.

## Remarks
This GitHub Action is published in the GitHub Marketplace. As such, you can find the [Terms of Service here](). Also, [here]() you can find the GitHub Marketplace Developer Agreement.
