# ============================================================================
#
# ../scripts/conjugation_mapper.py
#
# Run or Import this Script to get Conjugated Forms
#
# load /datasets/kanienkeha_vocab_extended_rules.yaml
# accept a verb root and dialect info
# map correct prefix for a given category, stem and pronoun combo
# return conjugated form or clearly log missing data for completion
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
import yaml
import sys
from pathlib import Path

VOCAB_YAML_PATH = Path("../datasets/kanienkeha_vocab_extended_rules.yaml")

def load_vocab_rules():
    with open(VOCAB_YAML_PATH, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def conjugate(dialect, category, stem, pronoun, verb_root):
    rules = load_vocab_rules()
    
    try:
        prefix = rules['dialects'][dialect]['verb_prefixes'][category][stem][pronoun]
    except KeyError:
        print(f"[⚠️ Missing] {dialect}.{category}.{stem}.{pronoun} not defined.")
        return None

    if prefix.startswith("TODO"):
        print(f"[⚠️ TODO] This combination has not been defined yet.")
        return None

    # Concatenate prefix + root (simple version; you could insert thematic vowels later)
    return f"{prefix}{verb_root}"

if __name__ == "__main__":
    # Example use: python conjugation_mapper.py western blue_category C_STEM I kenonwes
    if len(sys.argv) != 6:
        print("Usage: python conjugation_mapper.py [dialect] [category] [stem] [pronoun] [verb_root]")
        sys.exit(1)

    dialect, category, stem, pronoun, verb_root = sys.argv[1:]
    result = conjugate(dialect, category, stem, pronoun, verb_root)

    if result:
        print(f"✅ Conjugated: {result}")
