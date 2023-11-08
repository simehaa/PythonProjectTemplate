# Python Project Template
This repository is meant as template for Python projects. Poetry is used as dependency managemenet/packaging tool, and these packages are included:
* Black for linting
* Isort for linting
* Pytest for unit tests
* Pre-commit for simple code checks when `git commit ...` is run

Additionally a simple folder structure is included, with source code in the *./src* directory and unit tests in the *./tests* directory.

**Two Workflows**
* CI on pushes or PRs towards the *main* branch:
    1. Runs black and isort linting checks
    2. Runs unit tests
* CodeQL, GitHub's security vulnerability analysis, set up to run weekly