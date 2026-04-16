# Why package research code?

Many research projects begin as a collection of scripts or notebooks. This works well at first, especially during exploration and early development. As projects grow, problems tend to appear.

## Common issues include:

- Code only works when run from a specific folder
- Imports break when moving between machines
- Notebooks depend on hidden state
- Code runs locally but fails on HPC systems or in clean environments
- Reusing code across projects becomes difficult

## Benefits of packaging

Packaging your code helps address these problems. When your code is structured as a package:

- It can be imported consistently from anywhere
- It does not depend on the current working directory
- It behaves the same on laptops, HPC systems, and CI pipelines
- It is easier to test and reuse

In practice, this mostly means:

- putting code into a clearly defined module
- installing it into the environment rather than running scripts directly

## Reproducibility and reviewers
Increasingly, reviewers expect to be able to run research code themselves.
For many journals and conferences, this may include:

- installing the code
- running analyses
- reproducing figures or tables from the paper

Packaging your code makes this much easier. If a reviewer can:
``` bash
pip install .
```
and then run the analysis without modifying paths or guessing setup steps, you remove a significant barrier to reproducibility.
Making your code easy to install and run is not just good practice, it can directly affect how smoothly the review process goes.

## Minimal approach

This does not mean turning research code into large software projects. The goal is simply to introduce enough structure to make your work more reliable and easier to maintain.

This repository shows a minimal version of that approach.
