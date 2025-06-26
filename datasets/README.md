# 📚 Datasets for Mini-Indig-LLM-Kit

This folder contains all training, evaluation, metadata, and vocabulary resources for building and adapting open-source language models for **Kanien’kéha** (Mohawk) and other low-resource polysynthetic Indigenous languages.

The structure and contents are designed to be **transparent, editable, and inclusive** of both technical and non-technical collaborators, and to support **offline use** on low-end hardware.

---

## 🔖 Folder Contents

| File/Folder                        | Description |
|-----------------------------------|-------------|
| `data_template.json`              | Starter template showing how to structure annotated examples with morpheme tags, glosses, speaker metadata, etc. |
| `sample_dataset_metadata.json`    | Metadata file describing the dataset's contributors, sources, and ethical terms. |
| `kanienkeha_prefixes.jsonl`       | Example training data in JSONL format used for tokenizer and model training. |
| `kanienkeha_vocab_rules.yaml`     | Community-defined rules for prefixes, suffixes, and morpheme boundaries (multi-dialect support). |
| `csv_to_yaml.py`                  | Converts filled-in CSV or ODS files into `kanienkeha_vocab_rules.yaml`. |
| `vocab_builder.py`                | Visualizes token/morpheme frequencies and generates vocab lists. |
| `conjugation_mapper.py`          | Helper for mapping conjugation logic using vocab rules + verb stems. |
| `ods_exports/`                    | Offline .ods spreadsheets for community review and editing. |
| `generated_dataset_metadata.json`| Auto-generated metadata used to create model cards and config files. |

---

## 🧬 Data Structure Summary (`data_template.json`)

Each record in the dataset includes:

- `input_text`: Kanien’kéha sentence or phrase  
- `translation`: English meaning  
- `morpheme_gloss`: List of segmented morphemes  
- `morpheme_tags`: Roles (e.g. "1SG", "PAST", "REFL", etc.)  
- `speaker_id`, `dialect`, `source`, `validation_status`, and more

| Field               | Description                                          |
| ------------------- | ---------------------------------------------------- |
| `id`                | Unique identifier per sample                         |
| `dialect`           | One of: Eastern, Central, Western, English Phonetics |
| `speaker_id`        | Anonymous label for the speaker (for privacy)        |
| `speaker_role`      | Fluent, Semi-Fluent, Learner, Elder, Teacher         |
| `source`            | Where the sentence came from (lesson, story, etc.)   |
| `input_text`        | Raw sentence text                                    |
| `translation`       | English meaning or gloss                             |
| `morpheme_gloss`    | Array of segmented morphemes                         |
| `morpheme_tags`     | Corresponding tags for each morpheme                 |
| `stem_type`         | C-STEM, A-STEM, I-STEM, etc.                         |
| `category`          | Blue / Red / Purple                                  |
| `notes`             | Any additional speaker/context notes                 |
| `usage_context`     | How or when this phrase is used                      |
| `validation_status` | verified, pending\_review, needs\_validation         |
| `tokenized`         | Whether this was pre-tokenized for training          |


These fields help Indigenous language experts, engineers, and learners work together on data curation, tokenization, and model training.

---

## 🧾 Data Protocols & Ethics

This directory operates with full respect for:

- 📜 **Data Sovereignty**: All language data remains under community ownership and consent.
- 🧓🏽 **Speaker Credit**: Contributors are credited (or anonymized) per their preference.
- ⚖️ **Validation Transparency**: Each example tracks whether it was verified, reviewed, or flagged for discussion.
- 🛠️ **Editable CSV/ODS Workflows**: Non-technical contributors can use spreadsheets to review or add data offline
