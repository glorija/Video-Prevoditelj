# Video Prevoditelj HR

A local and Kaggle-assisted pipeline for translating source-language video speech into Croatian, cloning speaker voices per video, synthesizing Croatian speech, synchronizing timing, and rendering the final video.

## Project flow

NEW VIDEO
→ diarization
→ identify all speakers
→ extract speaker audio
→ create a new voice clone for each speaker
→ transcription
→ Croatian translation
→ Croatian voice synthesis
→ timing / synchronization
→ final MP4

## Repository rules

GitHub stores:
- notebooks
- Python source code
- JSON results and manifests
- configuration
- requirements and setup documentation

Kaggle Dataset stores:
- large WAV/audio files
- large video files
- model files and other large artifacts

Do not commit large media or model files to the repository.

## Video isolation

Each input video is treated as a separate project.

Speaker voices are extracted and cloned anew for each video.
Voices from previous videos must not be reused automatically.

## Quality rule

Quality has priority over speed.

Known-good components should not be replaced by experimental alternatives without a compatibility and quality check.

## Reproducibility

Each important processing step should leave a durable result, manifest, or configuration record so that work can be resumed without regenerating already verified results unnecessarily.
