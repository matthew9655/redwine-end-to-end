# Production Environment

## Manual Installation

`pip install -r requirements/requirements.txt && pip install -r requirements/typing_requirements.txt`

## Packaging

To run all scripts, we will be using `tox` for its environment management capabilities. 

To train the model, perform tests and styling, simply run `tox`.

To only train the model, run `tox run -e train`. Consequently, there should be a model under `src/red_wine_mm/trained_models`. More details can be found in the `tox.ini` file. 


## Deploying to PyPI

In this work, I deploy the production environment as a package in PyPI to make it easier to install the package in the app section. However, package names and versions have to be unique, so change the project name and version in `pyproject.toml` to something different. These restrictions will persist even if the package has been deleted from PyPI. 

Create a PyPI account at https://pypi.org/ and create a token, when prompted to login through the CLI, the username is `__token__` and the password is the created token. 

To manually deploy, run `deploy.sh`.

