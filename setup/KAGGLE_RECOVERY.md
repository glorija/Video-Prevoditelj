# Video Prevoditelj HR — Kaggle Recovery

## Repo

- GitHub: `glorija/Video-Prevoditelj`
- Radna grana: `project/3saL8oW3o7o`
- Projekt: `3saL8oW3o7o`
- Zadnji potvrđeni projektni commit: `5a8e2ac`

## Cilj

Kaggle je izvršno okruženje.
GitHub je trajno spremište koda, konfiguracije i malih reproducibilnih rezultata.
Veliki WAV/MP4/model artefakti ostaju izvan GitHuba.

## Sutrašnji redoslijed

1. Otvoriti Kaggle notebook.
2. Uključiti potreban GPU za sesiju.
3. Provjeriti povezane Kaggle Datasourceove.
4. Provjeriti Kaggle Secrets — samo prisutnost, nikad ne ispisivati vrijednosti.
5. Pokrenuti `setup/verify_kaggle.py`.
6. Ako su verzije i importi ispravni, NE reinstalirati pakete bez razloga.
7. Ako se sesija resetirala, koristiti poznatu bootstrap kombinaciju iz `requirements/kaggle-lock.txt`.
8. Klonirati/otvoriti GitHub repo i prebaciti se na:
   `project/3saL8oW3o7o`
9. Nastaviti od zadnjeg trajno spremljenog stanja.
10. Ne regenerirati već potvrđene rezultate bez razloga.

## Secrets

NE spremati vrijednosti tokena u GitHub.

Poznati secretovi:

- `GITHUB_TOKEN` — GitHub read/write za ovaj repo
- `fuck_token` — Hugging Face token koji koristi postojeći KlonAudio notebook
- `hf_token` — Hugging Face secret može postojati, ali postojeći KlonAudio notebook trenutno čita `fuck_token`

Secret vrijednosti se nikada ne zapisuju u notebook, JSON ili GitHub.

## Poznata kompatibilna kombinacija

Primarna poznata radna kombinacija:

- Python: 3.12.x
- NumPy: 2.0.2
- SciPy: 1.16.3
- PyTorch: 2.10.0+cu128
- TorchAudio: 2.10.0+cu128
- TorchVision: 0.25.0+cu128
- TorchCodec: 0.10.0+cu128
- Transformers: 4.57.3
- Hugging Face Hub: 0.34.4
- Lightning: 2.5.5
- pyannote.audio: 4.0.7
- pyannote.core: 6.0.1
- pyannote.database: 6.1.1
- pyannote.metrics: 4.1
- pyannote.pipeline: 4.0.0
- accelerate: 1.13.0
- diffusers: 0.37.1
- safetensors: 0.7.0
- KlonAudio: fixed commit
  `53f866dd49dd1645c26aa1929a3efadef006aece`

## Važno

Kaggle nakon restarta može vratiti novije zadane verzije.
Posebno ne pretpostavljati da su zadane verzije Transformers / Hugging Face Hub kompatibilne s našim KlonAudio setupom.

Povijesni test s Transformers 5.x i Hub 1.x nije baseline za naš projekt.

Povijesni test s Transformers 4.50.3 bio je eksperiment; nije primarna zaključana kombinacija.

## KlonAudio

Poznati fiksni commit:

`53f866dd49dd1645c26aa1929a3efadef006aece`

KlonAudio učitavanje može zahtijevati postojeći CPU/meta patch iz notebooka.
Ne mijenjati taj patch bez novog testa.

## Projektno stanje

Do sada trajno spremljeno:

- source manifest
- diarization rezultat
- speaker registry
- voice quality rezultat
- project README
- GitHub branch
- GitHub commit `5a8e2ac`

Sljedeći korak:

**transkripcija**

Nakon toga:
transkripcija → hrvatski prijevod → TTS/voice cloning → timing → finalni video.

## Velike datoteke

Ne commitati:

- WAV
- MP3
- MP4
- modele
- safetensors
- cijeli Python/venv
- cache

Veliki artefakti ostaju u Kaggle Dataset / radnom prostoru.

## Pravilo kvalitete

Ne mijenjati poznato dobar dio pipelinea eksperimentalnim dijelom
dok se kompatibilnost i kvaliteta prethodno ne provjere.
