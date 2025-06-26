# ============================================================================
#
# validate_yaml_structure.py
# to use pip install pyyaml cerberus
# Lint YAML structure before training or tokenizing
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

from cerberus import Validator
import yaml
from pathlib import Path

schema = {
    'dialects': {
        'type': 'dict',
        'valuesrules': {
            'type': 'dict',
            'schema': {
                'verb_prefixes': {
                    'type': 'dict',
                    'schema': {
                        'blue_category': {'type': 'dict'},
                        'red_category': {'type': 'dict'},
                        'purple_category': {'type': 'dict'}
                    }
                }
            }
        }
    }
}

def validate_yaml(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    v = Validator(schema)
    if v.validate(data):
        print("✅ YAML is valid.")
    else:
        print("❌ YAML validation errors:")
        print(v.errors)

validate_yaml("../datasets/kanienkeha_vocab_rules.yaml")