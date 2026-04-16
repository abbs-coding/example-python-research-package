![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green) 
![Tests](https://github.com/abbs-coding/example-python-research-package/actions/workflows/tests.yml/badge.svg)

# example-python-research-package

A minimal example of how to structure and package a small Python research project.

This repository is intended as a reference for researchers who want a clean, reliable way to organise code beyond scripts and notebooks.

## Audience

This repository is aimed at:

- PhD students
- Early-career researchers
- Anyone working with Python who wants a more robust project structure

It assumes basic familiarity with Python, but no prior experience with packaging.

## Quickstart

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**macOS or Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

Install the project:

```bash
pip install -e .
```

For development (including tests):

```bash
pip install -e .[dev]
```

Run the tests:

```bash
pytest
```

Example usage:

```python
from example_python_research_package.example import count_words

count_words("This is a short example")
```

## Project structure

The repository is organised as follows:

- `src/` contains the package code
- `tests/` contains the test suite
- `pyproject.toml` defines how the project is built and installed

The package itself lives in:

```
src/example_python_research_package/
```

This layout helps ensure that code is always imported as an installed package rather than via local paths.

## What this repository demonstrates

- A `src/` layout for research code
- A minimal `pyproject.toml` configuration
- Editable installs for development
- Basic testing with pytest
- A simple but realistic module structure

## Learning resources

If you want to understand the reasoning behind this structure:

- [Why package research code?](docs/why-package-research-code.md)
- [Understanding pyproject.toml](docs/understanding-pyproject-toml.md)
- [How to write a README](docs/how-to-write-a-readme.md)
- [Development workflow](docs/development-workflow.md)

## Usage

This repository is intended as a starting point. You are encouraged to adapt it to your own research projects rather than copy it exactly.

## Contributing

Suggestions and improvements are welcome. Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact

For questions or feedback, please open an issue or contact:

**Dr Helen Abbott**  
Advanced Research Computing, University of Birmingham

h.e.abbott.1@bham.ac.uk