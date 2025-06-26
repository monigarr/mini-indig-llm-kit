# ============================================================================
#
# scripts/csv_to_yaml.py
# read the edited .csv files (one per dialect or combined) 
# and convert them back into the original nested 
# kanienkeha_vocab_rules.yaml or kanienkeha_vocab_extended_rules.yaml
# NOTE: this regenerates the structure WITHOUT dialect descriptions, 
#       so make a copy of the descriptions to manually add back if needed.
#
# convert full YAML tree into a flat csv file per dialect.
# columns: dialect, category, stem, pronoun, value
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
import pandas as pd
import yaml
from pathlib import Path
from collections import defaultdict

CSV_PATH = Path("../editable_worksheets/all_dialects_conjugation_table.csv")
YAML_OUT_PATH = Path("../datasets/kanienkeha_vocab_rules_updated.yaml")

def nested_dict():
    return defaultdict(nested_dict)

def update_nested_dict(root, dialect, category, stem, pronoun, value):
    root['dialects'][dialect]['verb_prefixes'][category][stem][pronoun] = value
    return root

def convert_csv_to_yaml():
    df = pd.read_csv(CSV_PATH)
    root = nested_dict()

    for _, row in df.iterrows():
        dialect = row['dialect']
        category = row['category']
        stem = row['stem']
        pronoun = row['pronoun']
        value = row['value']
        update_nested_dict(root, dialect, category, stem, pronoun, value)

    # Convert nested defaultdicts to normal dicts
    def convert(obj):
        if isinstance(obj, defaultdict):
            obj = {k: convert(v) for k, v in obj.items()}
        return obj

    clean_data = convert(root)
    with open(YAML_OUT_PATH, "w", encoding='utf-8') as out_file:
        yaml.dump(clean_data, out_file, sort_keys=False, allow_unicode=True)

    print(f"✅ YAML regenerated at {YAML_OUT_PATH}")

convert_csv_to_yaml()
