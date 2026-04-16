# Continuous Integration

## What is continuous integration?

Continuous integration (CI) is a way of automatically running checks on your code whenever it changes.

In this repository, CI is used to run the test suite whenever code is pushed to the repository or a pull request is opened.

This is handled by [GitHub Actions](https://github.com/features/actions).

## What happens in this repository?

When you push code:

- A fresh virtual machine is created
- Python is installed
- The package is installed
- The tests are run using pytest

This happens independently of your local machine.

## Why this matters

CI helps catch problems early.

For example:

- Code that works locally but fails in a clean environment
- Missing dependencies
- Changes that break existing functionality

It also improves reproducibility. If the tests pass in CI, you know the code works outside your own setup.

## How to read the results

On the repository page, you will see a status indicator:

- **Green tick**: the tests passed
- **Red cross**: something failed

You can click on the workflow run to see detailed logs.

If a test fails, the logs will show which step failed and why.

## What you do not need to worry about

You do not need to understand the full configuration of the CI system to use it effectively.

For most research projects, it is enough to know that:

- Tests run automatically
- Failures are reported clearly
- You should fix failing tests before continuing

This simple setup is often sufficient for small and medium-sized research codebases.