# Understanding pyproject.toml

The `pyproject.toml` file defines how your project is built and installed.

You do not need to understand every detail to use it effectively. At a high level, it answers three questions:

- How is the project installed?
- What is the project?
- What does it depend on?

## Build system

The `build-system` section tells tools like pip how to install your project.

In this repository, setuptools is used because it is widely supported and works reliably across environments.

## Project metadata

The `project` section includes:

- `name`
- `version`
- required Python version
- `authors`
- `licence`

This information is important for reproducibility and attribution.

In research, the authors listed here are the people responsible for the software itself. This may not match the authors of a related paper.

## Dependencies

Dependencies are split into two groups:

- `dependencies`: required to run the code
- `optional dependencies`: used for development, such as testing

This allows you to install only what you need:

```bash
pip install -e .
pip install -e .[dev]
```

You can modify this file gradually as your project grows. There is no need to understand every field from the start.