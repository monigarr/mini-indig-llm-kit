# ============================================================================
#
# validate_tokenizer_config.py 
# Validates tokenizer_config.json against dialects and metadata in kanienkeha_vocab_rules.yaml.
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


import json
import yaml

def validate_tokenizer_config(config_path, vocab_yaml_path):
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    with open(vocab_yaml_path, "r", encoding="utf-8") as f:
        vocab = yaml.safe_load(f)

    expected_dialects = set(vocab.get("dialects", {}).keys())
    config_dialects = set(config.get("metadata", {}).get("dialect_support", []))

    if expected_dialects != config_dialects:
        print("❌ Dialect mismatch between YAML and tokenizer_config.json:")
        print("YAML Dialects:   ", expected_dialects)
        print("Config Dialects: ", config_dialects)
    else:
        print("✅ Dialects match.")

    print("🔍 Validating required fields...")
    required_fields = ["tokenizer_class", "model_max_length", "language", "tokenizer_file"]
    for field in required_fields:
        if field not in config:
            print(f"❌ Missing field: {field}")
        else:
            print(f"✅ Found field: {field}")

validate_tokenizer_config("tokenizer_config.json", "kanienkeha_vocab_rules.yaml")
