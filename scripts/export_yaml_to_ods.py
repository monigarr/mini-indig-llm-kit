# ============================================================================
#
# export_yaml_to_ods.py
# to use this script
# suggested to run in virtual environment:
# pip install odfpy pandas pyyaml
# 
# scripts/export_yaml_to_ods.py
# 
# Directory Summary after running:
# /scripts/
#  ├─ csv_to_yaml.py ✅
#  ├─ export_yaml_to_ods.py ✅
#/editable_worksheets/
#  ├─ all_dialects_conjugation_table.csv ✅
#  ├─ all_dialects_conjugation_table.ods ✅
#/datasets/
#  ├─ kanienkeha_vocab_rules_updated.yaml ✅
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
from odf.opendocument import OpenDocumentSpreadsheet
from odf.table import Table, TableRow, TableCell
from odf.text import P

YAML_PATH = Path("../datasets/kanienkeha_vocab_extended_rules.yaml")
OUTPUT_PATH = Path("../editable_worksheets/all_dialects_conjugation_table.ods")

def flatten_rules(dialect, data):
    rows = []
    for category, stems in data.get("verb_prefixes", {}).items():
        for stem, pronouns in stems.items():
            for pronoun, value in pronouns.items():
                rows.append([dialect, category, stem, pronoun, value])
    return rows

def create_ods(dataframe, filename):
    doc = OpenDocumentSpreadsheet()
    table = Table(name="ConjugationTable")

    # Add header
    header = TableRow()
    for h in dataframe.columns:
        cell = TableCell()
        cell.addElement(P(text=str(h)))
        header.addElement(cell)
    table.addElement(header)

    # Add data rows
    for _, row in dataframe.iterrows():
        tr = TableRow()
        for item in row:
            tc = TableCell()
            tc.addElement(P(text=str(item)))
            tr.addElement(tc)
        table.addElement(tr)

    doc.spreadsheet.addElement(table)
    doc.save(filename)
    print(f"✅ ODS saved to: {filename}")

def export_to_ods():
    with open(YAML_PATH, "r", encoding='utf-8') as f:
        yaml_data = yaml.safe_load(f)

    all_rows = []
    for dialect, ddata in yaml_data.get("dialects", {}).items():
        rows = flatten_rules(dialect, ddata)
        all_rows.extend(rows)

    df = pd.DataFrame(all_rows, columns=["dialect", "category", "stem", "pronoun", "value"])
    create_ods(df, OUTPUT_PATH)

export_to_ods()
