# Projects

Each input video is a separate project.

## Project structure

Use one directory per video:

projects/
└── <video-project-name>/
    ├── README.md
    ├── manifests/
    ├── diarization/
    ├── translation/
    ├── voices/
    └── results/

## Persistent data

Store small, reproducible files in GitHub:

- JSON
- manifests
- configuration
- metadata
- processing notes
- text results

Store large files outside GitHub:

- WAV
- MP4
- model files
- large intermediate audio/video artifacts

## Speaker rule

Every new video gets a new speaker analysis.

For every detected speaker:
1. extract the speaker audio from the current video
2. create a new voice clone
3. associate that clone with the current project

Do not automatically reuse speaker voices from another video project.

## Reproducibility

Each project should contain enough metadata to identify:
- input video
- detected speakers
- processing configuration
- model versions
- important output files
- processing status
