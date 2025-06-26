# Kanien’kéha Custom Tokenizer

This directory contains a custom [SentencePiece](https://github.com/google/sentencepiece) tokenizer trained from token frequency data extracted from a Kanien’kéha (Mohawk) corpus. It supports multiple dialects and morpheme boundaries commonly found in polysynthetic Indigenous languages.

---

## 📦 Files

- `kanienkeha_tokenizer.model` — The tokenizer model file (Unigram type)
- `kanienkeha_tokenizer.vocab` — Vocabulary list aligned with the model
- `test_tokenizer.py` — Script to validate segmentation output
- `../datasets/kanienkeha_vocab_rules.yaml` — Language-specific vocabulary rules per dialect

---

## 🧠 How to Use

### Python (with `sentencepiece`)

```python
import sentencepiece as spm

sp = spm.SentencePieceProcessor()
sp.load("tokenizer/kanienkeha_tokenizer.model")

text = "Kenòn:we’s tsi ní:io?"
tokens = sp.encode(text, out_type=str)
print(tokens)

CLI BASH
spm_encode --model=kanienkeha_tokenizer.model --input=sample.txt --output_format=piece

This tokenizer is dialect-aware via YAML config:
* Eastern Dialect (Akwesasne)
* Central Dialect (Kahnawake)
* Western Dialect (Tyendinaga, Six Nations)
* Non-Standardized (English Speaker Friendly)

You may configure prefix/suffix handling per dialect by editing:
../datasets/kanienkeha_vocab_rules.yaml

### tokenizer_config.json 
supports a custom tokenizer for Kanien’kéha (Mohawk) and other polysynthetic Indigenous languages with:

Support for prefix/suffix-heavy morphology

Culturally respectful lowercasing and normalization

Offline reuse and integration with Hugging Face-compatible models

Alignment with kanienkeha_vocab_rules.yaml and custom vocab

🧠 How This Works
do_lower_case: true: Helps unify English-style phonetics with standard orthography.

special_tokens_map: Ensures alignment with model config.

prefix_indicator / suffix_indicator: Useful for morph boundary debugging.

additional_special_tokens: Allow for speaker and dialect labeling during fine-tuning and inference.

tokenizer_file: Matches your serialized tokenizer built from kanienkeha_vocab_rules.yaml.

### Component	Purpose
tokenizer_test_set.json	Gold standard segmentation examples
test_tokenizer_segmentation.py	Offline CLI test to check BPE or morpheme rules
tokenizer_tests.ipynb	Easy-to-read token comparison for team review





