# Why package research code?

Many research projects begin as a collection of scripts or notebooks. This works well at first, but problems tend to appear as projects grow.

## Common issues include:

- Code only works when run from a specific folder
- Imports break when moving between machines
- Notebooks depend on hidden state
- Code runs locally but fails on HPC systems
- Reusing code across projects becomes difficult

## Benefits of packaging

Packaging your code helps address these problems. When your code is structured as a package:

- It can be imported consistently from anywhere
- It does not depend on the current working directory
- It behaves the same on laptops, HPC systems, and CI pipelines
- It is easier to test and reuse

## Minimal approach

This does not mean turning research code into large software projects. The goal is simply to introduce enough structure to make your work more reliable and easier to maintain.

This repository shows a minimal version of that approach.
