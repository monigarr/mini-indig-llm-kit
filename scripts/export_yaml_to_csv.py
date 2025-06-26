# ============================================================================
#
# ../scripts/export_yaml_to_csv.py
# Generate dialect-wise editable .csv tables for fluent Kanien’kéha writers / speakers
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
import yaml
import pandas as pd
from pathlib import Path

YAML_PATH = Path("../datasets/kanienkeha_vocab_rules.yaml")
OUTPUT_DIR = Path("../editable_worksheets/")
OUTPUT_DIR.mkdir(exist_ok=True)

def flatten_rules(dialect, data):
    rows = []
    for category, stems in data.get("verb_prefixes", {}).items():
        for stem, pronouns in stems.items():
            for pronoun, value in pronouns.items():
                rows.append({
                    "dialect": dialect,
                    "category": category,
                    "stem": stem,
                    "pronoun": pronoun,
                    "value": value
                })
    return rows

def convert_yaml_to_csv():
    with open(YAML_PATH, "r", encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f)

    all_rows = []
    for dialect, ddata in yaml_data.get("dialects", {}).items():
        rows = flatten_rules(dialect, ddata)
        df = pd.DataFrame(rows)
        csv_path = OUTPUT_DIR / f"{dialect}_conjugation_table.csv"
        df.to_csv(csv_path, index=False)
        print(f"✅ Saved: {csv_path}")
        all_rows.extend(rows)

    # Save a combined file too
    pd.DataFrame(all_rows).to_csv(OUTPUT_DIR / "all_dialects_conjugation_table.csv", index=False)

convert_yaml_to_csv()
