# mini-indig-llm-kit 🪶

**An open-source starter kit to build, fine-tune, and deploy culturally responsible, offline-compatible Mini LLMs for Indigenous, polysynthetic, low-resource languages.**

---

## 🧠 What is This?

This toolkit helps Onkwehonwe communities, researchers, and technologists fine-tune open-source LLMs like LLaMA 3 (8B) using QLoRA for their own languages—especially those without an ISO code for each dialect, dictionaries, or digital resources that are not currently supported by standardized communication protocols and platforms.

All tools are optimized to run **offline**, with clear instructions, low-resource compatibility, and collaborative cultural protocols.

---

## ✨ Features

- ✅ **Fine-tune LLaMA 3 with QLoRA** on your own corpus
- 🌐 **Train custom tokenizers** for polysynthetic languages
- 🛠️ **Use and deploy models offline** (USB sticks, old laptops, no internet)
- 📄 **Ethical templates and worksheets** for culturally safe collaboration
- 🧩 Modular Jupyter notebooks for tokenization, fine-tuning, inference
- 🔤 Prompt templates for translation, summarization, and chat

---

## 💻 Quick Start

1. **Clone the repo**  
   ```bash
   git clone https://github.com/YOUR_USERNAME/mini-indig-llm-kit.git
   cd mini-indig-llm-kit

### GitHub Actions

## build_tokenizer_reports.yml
Make sure GitHub Pages is enabled in your repo:

Settings → Pages → Source → Select GitHub Actions as source.

Ensure your main branch includes:

/tokenizer/tokenizer_segmentation_scores.ipynb

/tokenizer/tests/tokenizer_test_set.csv

/tokenizer/custom_tokenizer.json

Add the following to your requirements.txt:
pandas
openpyxl
transformers
scikit-learn
nbconvert
jupyter

✅ 3. Result: Reviewer Dashboard
After every tokenizer update, your team will get:

File	                     Available in main repo?	         Public GitHub Pages?
segmentation_results.html	✅ /reports/index.html	         ✅ [your-org].github.io/[repo-name]
segmentation_results.ods	✅ for download	                  ❌ (no preview)
segmentation_results.csv	✅ for download	                  ❌




