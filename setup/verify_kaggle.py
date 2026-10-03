from pathlib import Path
import importlib.metadata as md
import os
import subprocess
import sys

EXPECTED = {
    "numpy": "2.0.2",
    "scipy": "1.16.3",
    "torch": "2.10.0+cu128",
    "torchaudio": "2.10.0+cu128",
    "torchvision": "0.25.0+cu128",
    "torchcodec": "0.10.0+cu128",
    "transformers": "4.57.3",
    "huggingface-hub": "0.34.4",
    "lightning": "2.5.5",
    "pyannote.audio": "4.0.7",
    "pyannote.core": "6.0.1",
    "pyannote.database": "6.1.1",
    "pyannote.metrics": "4.1",
    "pyannote.pipeline": "4.0.0",
    "accelerate": "1.13.0",
    "diffusers": "0.37.1",
    "safetensors": "0.7.0",
}

print("=" * 60)
print("VIDEO PREVODITELJ HR — KAGGLE VERIFY")
print("=" * 60)

print("\n=== PYTHON ===")
print(sys.version)
print(sys.executable)

print("\n=== TORCH / CUDA ===")
try:
    import torch
    print("torch:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())

    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))
        print("CUDA runtime:", torch.version.cuda)
except Exception as e:
    print("Torch ERROR:", type(e).__name__, str(e))

print("\n=== PACKAGE VERSIONS ===")
for name, expected in EXPECTED.items():
    try:
        actual = md.version(name)
        mark = "OK" if actual == expected else "MISMATCH"
        print(f"{name:22} {actual:18} expected={expected:18} [{mark}]")
    except Exception:
        print(f"{name:22} NOT INSTALLED        expected={expected}")

print("\n=== PYANNOTE IMPORT ===")
try:
    from pyannote.audio import Pipeline
    print("pyannote.audio import: OK")
except Exception as e:
    print("pyannote.audio import:", type(e).__name__, str(e))

print("\n=== KLONAUDIO IMPORT ===")
try:
    import kugelaudio_open
    from kugelaudio_open import (
        KugelAudioForConditionalGenerationInference,
        KugelAudioProcessor,
    )
    print("kugelaudio_open: OK")
    print("path:", kugelaudio_open.__file__)
except Exception as e:
    print("KlonAudio import:", type(e).__name__, str(e))

print("\n=== KAGGLE FILES ===")
paths = [
    "/kaggle/working/3saL8oW3o7o",
    "/kaggle/input/datasets/zeljkozic/voice-source/source_voice.wav",
]

for p in paths:
    print(f"{p:80} {'DA' if Path(p).exists() else 'NE'}")

print("\n=== SECRETS — ONLY PRESENCE ===")
try:
    from kaggle_secrets import UserSecretsClient
    secrets = UserSecretsClient()

    for name in ["GITHUB_TOKEN", "fuck_token", "hf_token"]:
        try:
            value = secrets.get_secret(name)
            print(f"{name:15} DA")
        except Exception:
            print(f"{name:15} NE")
except Exception as e:
    print("Secrets check error:", type(e).__name__, str(e))

print("\n=== GIT ===")
repo = Path("/kaggle/working/Video-Prevoditelj")

if repo.exists():
    r = subprocess.run(
        ["git", "-C", str(repo), "branch", "--show-current"],
        text=True,
        capture_output=True,
    )
    print("branch:", r.stdout.strip() or "(none)")

    r = subprocess.run(
        ["git", "-C", str(repo), "status", "--short", "--branch"],
        text=True,
        capture_output=True,
    )
    print(r.stdout)

print("=" * 60)
print("VERIFY GOTOV — NE MIJENJA OKRUŽENJE")
print("=" * 60)
