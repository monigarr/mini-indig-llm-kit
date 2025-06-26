# ============================================================================
#
# generate_model_card.py
# this script does the same as our Jupyter Notebook in
# ../notebooks/generate_model_card.ipynb
#
# Author: 
#   MoniGarr (Monica Peters), monigarr@MoniGarr.com
#
# This repository supports language revival & retention for
#     Polysynthetic, Low-Resource Indigenous Languages that
#       might lack industry standard language ISO codes.
#
# License: Apache 2.0
# 
# For technical consulting, collaboration, or mentorship on Indigenous
# Language Revival & Retention Tech Solutions (AI, XR, 3D, Cultural Protocols)
# contact:
#   MoniGarr (Monica Peters) – monigarr@monigarr.com
#   Founder of MoniGarr.com LLC and MohawkLanguage.ca
#   Akwesasne-based Onkwehonwe (Indigenous, Kanien’kéhake, Mohawk of Akwesasne)
#   https://www.linkedin.com/in/3dtechartist
#
# ============================================================================


from pathlib import Path
import json

TEMPLATE_PATH = Path("config/model_card_template.md")
METADATA_PATH = Path("datasets/sample_dataset_metadata.json")
OUTPUT_PATH = Path("models/generated_model_card.md")

def generate_model_card():
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)

    filled = template
    filled = filled.replace("[MODEL_NAME_HERE]", f"{meta['language']} {meta['dialect']} LLM")
    filled = filled.replace("[MODEL_VERSION]", meta.get("version", "1.0"))
    filled = filled.replace("[YYYY-MM-DD]", "2025-06-25")
    filled = filled.replace("[Apache 2.0]", meta.get("license", "custom-community-license"))
    filled = filled.replace("[MoniGarr, Monica Peters]", ", ".join([c["name"] for c in meta["contributors"] if c["role"] == "engineer"]))
    filled = filled.replace("[MohawkLanguage.ca, Akwesasne]", meta["contributors"][0].get("affiliation", ""))
    filled = filled.replace("[Eastern]", meta.get("dialect", ""))
    filled = filled.replace("[GitHub Repository URL]", "https://github.com/monigarr/mini-indig-llm-kit")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(filled)

    print(f"✅ Model card generated: {OUTPUT_PATH}")

if __name__ == "__main__":
    generate_model_card()
