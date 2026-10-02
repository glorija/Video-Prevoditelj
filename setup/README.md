# Setup

This directory contains environment setup and installation instructions.

## Environment separation

Different processing components may require different Python environments.

Keep incompatible environments isolated rather than forcing incompatible package versions into one environment.

## Reproducibility

Document:

- Python version
- operating system
- GPU / CPU environment
- important package versions
- model versions
- installation commands
- known compatibility constraints

## Safety rule

Do not change a known-good environment without recording the previous working versions first.

Before a major dependency change, verify compatibility with the existing pipeline.
