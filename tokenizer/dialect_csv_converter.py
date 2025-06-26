# ============================================================================
#
# dialect_csv_converter.py
# Converts editable .csv dialect sheets into YAML format for tokenizer use.
#
# Converts dialect spreadsheets into kanienkeha_vocab_rules.yaml format
# for tokenizer alignment and rule-based segmentation.
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

def convert_csv_to_yaml(csv_path, yaml_output):
    df = pd.read_csv(csv_path)
    output = {"dialects": {}}

    for dialect in df["dialect"].unique():
        output["dialects"][dialect] = {}
        sub = df[df["dialect"] == dialect]
        for category in sub["category"].unique():
            output["dialects"][dialect][category] = sub[sub["category"] == category]["morpheme"].dropna().tolist()

    with open(yaml_output, "w", encoding="utf-8") as f:
        yaml.dump(output, f, allow_unicode=True)

    print(f"✅ Exported to {yaml_output}")

# Example usage:
# convert_csv_to_yaml("kanienkeha_dialects.csv", "kanienkeha_vocab_rules.yaml")
