# ============================================================================
#
# scripts/config_loader.py
#
# loads and validates training configs before launch 
#
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
import jsonschema
from pathlib import Path

CONFIG_PATH = Path("../config/training_config.yaml")
SCHEMA_PATH = Path("../config/training_config_schema.yaml")

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def validate_training_config():
    config = load_yaml(CONFIG_PATH)
    schema = load_yaml(SCHEMA_PATH)

    try:
        jsonschema.validate(instance=config, schema=schema)
        print("✅ training_config.yaml is valid.")
        return config
    except jsonschema.ValidationError as e:
        print(f"❌ Validation Error: {e.message}")
        raise

if __name__ == "__main__":
    validate_training_config()
