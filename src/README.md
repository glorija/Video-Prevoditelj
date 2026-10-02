# Source Code

This directory contains the Python source code for Video Prevoditelj HR.

## Organization

Keep reusable application logic here.

Examples:

- video analysis
- diarization
- transcription
- Croatian translation
- voice cloning and synthesis
- timing and synchronization
- final video rendering
- utility functions

## Rules

Prefer small, focused modules instead of one large script.

Known-good production components should be preserved unless a replacement has been tested for compatibility and quality.

Experimental code should be clearly identified and should not silently replace the working pipeline.

## Dependencies

Python dependencies and installation instructions belong in `requirements/` and `setup/`, not inside individual source files unless required for a specific module.
