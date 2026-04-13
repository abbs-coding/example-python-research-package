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

## How to use it
You are not expected to use this repository verbatim.

Instead, treat it as:
- a reference structure
- a starting point for your own research projects
- something to adapt rather than copy

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
