# Requirements

This directory contains dependency definitions for Video Prevoditelj HR.

## Purpose

Keep reproducible dependency sets for:

- the main Windows application
- Kaggle processing
- diarization
- translation
- voice cloning and synthesis
- testing and development

## Rules

Record exact package versions for known-good environments.

Do not use a single dependency file for components that require incompatible environments.

When an environment is changed, preserve the previous working dependency set before testing the new one.

## Compatibility

Important model and framework combinations should be documented together with:

- Python version
- PyTorch version
- CUDA version
- Transformers version
- model version or commit
- other critical package versions
