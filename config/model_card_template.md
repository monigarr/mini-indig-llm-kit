# 🧾 Model Card: Mini-Indig-LLM-Kit

## 📌 Model Overview

**Model Name**: [MODEL_NAME_HERE]  
**Version**: [MODEL_VERSION]  
**Date**: [YYYY-MM-DD]  
**License**: [LICENSE_TYPE]  
**Author(s)**: [AUTHOR_NAMES]  
**Community Affiliation**: [COMMUNITY / ORGANIZATION]  
**Dialect(s)**: [Eastern / Central / Western / English-Phonetic]  
**Model Type**: Fine-tuned LLaMA3-8B w/ QLoRA  
**Toolkit**: Trained and packaged using the Mini-Indig-LLM-Kit  
**Offline Capable**: Yes  
**Intended Use**: Language retention, education, cultural storytelling, community research  
**Source Repo**: [GitHub Repository URL]

---

## 📚 Intended Use

This model is designed for Indigenous communities working on the revival and retention of their own low-resource polysynthetic languages (e.g., Kanien’kéha dialects) with minimal compute, bandwidth, or storage requirements. It supports:

- Morphological tokenization and analysis
- Pronoun prefix generation
- Audio-to-text transcription with Whisper
- Culturally respectful fine-tuning of LLMs
- Community-led dataset creation and validation

---

## 🌐 Supported Languages & Dialects

| Language       | Dialects Supported       | Notes |
|----------------|--------------------------|-------|
| Kanien’kéha    | Eastern, Central, Western, Eng


# Programmatically load tokenizer and run prefix mapping
from tokenizer.custom_tokenizer import KanienkehaTokenizer
tokenizer = KanienkehaTokenizer("eastern")
tokenizer.tokenize("khenòn:we’s")

