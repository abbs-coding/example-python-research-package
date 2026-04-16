# Development workflow

This repository uses a simple workflow that is suitable for small research projects.

## Editable install

The project is installed in editable mode:

```bash
pip install -e .[dev]
```

This means that changes to the source code are immediately available without reinstalling the package.

## Typical workflow

1. Make changes to code in `src/`
2. Run tests with `pytest`
3. Repeat

This loop helps catch errors early and keeps the codebase stable.

## Testing

Tests are located in the `tests/` directory.

They import the package in the same way a user would. This ensures that the code is tested in a realistic way.

## Why this matters

Without this workflow, it is easy to end up with:

- code that only works in one environment
- hidden dependencies on notebook state
- difficulty reproducing results

A small amount of structure makes research code much easier to maintain and reuse.