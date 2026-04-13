# example-python-research-package

This repository was inspired by a coaching engagement with a PhD student who wanted to better understand how to package Python code for academic research use.

It provides a minimal but realistic example of a small research project structured and packaged in a way that (hopefully!) avoids common pitfalls.

## Who is this for?
This repository is aimed at:
- PhD students
- Early-career researchers
- Researchers who currently work with Python scripts or notebooks and want a cleaner structure.

It assumes basic familiarity with Python, but no prior experience with Python packaging.

## What this repository shows
This example demonstrates:
- How to structure a small research codebase using a `src/` layout
- How to define a project using `pyproject.toml`
- How to install your own code in editable mode
- How to write simple tests against research code
- How a minimal example module and test suite fit into this structure

## Repository structure and examples

This repository contains a small, deliberately simple example package and a corresponding test suite. The goal is to demonstrate *structure and workflow*, rather than sophisticated functionality.

### The example module

The example code lives in:

    src/example_python_research_package/example.py

This module contains a small, self-contained function that performs a simple text-processing task. The choice of example is intentionally non‑domain‑specific, so that the focus remains on code structure and packaging rather than subject matter.

The module is placed inside a directory with the same name as the package (`example_python_research_package`). This is the directory that is installed when the project is installed with `pip`.

### The `__init__.py` files

Both the package directory and the `tests` directory contain an empty `__init__.py` file.

These files indicate to Python that the directories should be treated as packages. Including them makes imports explicit and predictable, and avoids subtle differences in behaviour across Python versions and environments. For small research projects, it is generally safest to include them.

### Tests

The tests live in the `tests/` directory:

    tests/test_example.py

These tests:
- import the code from the installed package (rather than via relative paths)
- check expected behaviour for typical inputs
- check that appropriate errors are raised for invalid inputs

This mirrors how the code would be used in practice and helps ensure that it behaves consistently across different environments, including HPC systems and CI pipelines.

### `.gitignore`

A `.gitignore` file is included to prevent files such as virtual environments, compiled Python files, and test artefacts from being committed to version control.

This helps keep the repository focused on source code and documentation, and avoids accidental commits of local or machine‑specific files.

## How to use it
You are not expected to use this repository verbatim.

Instead, treat it as:
- a reference structure
- a starting point for your own research projects
- something to adapt rather than copy

## Running the example

This section shows how to install the project, run the example code, and execute the tests. These steps mirror a typical workflow for a small research codebase.

### Create and activate a virtual environment

It is recommended to work inside a virtual environment to avoid conflicts with other Python projects.

From the root of the repository:

```bash
python -m venv .venv
```

Activate the environment:
```bash
# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### Install the project
Install the project in editable mode, along with the development dependencies:
``` bash
pip install -e .[dev]
```
Editable installation means changes to the source code are picked up immediately, without reinstalling the package.

### Run the example code
Once installed, the example module can be imported from anywhere inside the repository (or outside it).
For example, start a Python interpreter and run:
``` python
from example_python_research_package.example import count_words

count_words("This is a short example")
```
This demonstrates that the code is being imported from the installed package, rather than via relative paths.

### Run the tests
To run the test suite:
``` bash 
pytest
```
The tests import the package in the same way a user would and verify both expected behaviour and error handling. This helps ensure the code behaves consistently across different environments, including HPC systems and continuous integration pipelines.

## Common misconceptions
Common issues this structure helps avoid:

- Import errors when running scripts from different locations
- Code working locally but not on HPC or CI systems

## About `pyproject.toml`

This repository uses a `pyproject.toml` file to describe the project and how it should be installed.

If you are new to Python packaging, you do not need to understand every part of this file immediately. Instead, think of it as answering three main questions:

1. How is this project built and installed?
2. What is this project, and what does it need to run?
3. How is the code laid out?

### Build system

The `[build-system]` section tells tools like `pip` how to install the project.

In this example we use `setuptools`, which is widely supported and works well on HPC systems. You generally do not need to modify this section for small research projects.

### Project metadata

The `[project]` section describes basic information about the project: its name, version, Python requirements, licence, and authors.

This information is important for:
- reproducibility
- attribution
- avoiding accidental installs on incompatible Python versions (e.g. on HPC systems)

In a research context, metadata also plays an important role in clearly distinguishing **software authorship** from **paper authorship**.

The `authors` field should list the people who are responsible for designing, writing, and maintaining the software. This is often a subset of the authors who may appear on an academic paper derived from the research.

Broader intellectual, supervisory, or funding contributions are normally better acknowledged elsewhere (for example: in the README, a CITATION file, or a related publication), rather than in the software metadata itself.

### Dependencies

Runtime dependencies are listed under `dependencies`, while development tools (such as testing frameworks) are listed under `project.optional-dependencies`.

This allows users to install:
- only what is needed to run the code, or
- additional tools needed for development and testing

For example:

    pip install -e .
    pip install -e .[dev]

### Why a `src/` layout?

This repository uses a `src/` layout, meaning the Python package lives inside the `src/` directory.

This helps avoid common problems such as:
- accidental imports from the working directory
- code behaving differently on HPC systems or CI

It encourages thinking of research code as *installed software*, rather than a collection of scripts.

## Usage
All are warmly encouraged to use this repository freely and to modify it in accordance with the licence governing this repository.

## Contributing
Contributions, suggestions, and corrections are welcome.

## License
This project is licensed under the MIT License. See LICENSE for details.


## Contact
For questions or feedback, please open an issue or contact:

Dr Helen Abbott  
Advanced Research Computing, University of Birmingham

h.e.abbott.1@bham.ac.uk
