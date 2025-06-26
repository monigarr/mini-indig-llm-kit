# ============================================================================
#
# validate_metadata.py
# ✔️ Usage: python scripts/validate_metadata.py ../datasets/sample_dataset_metadata.json
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

import json
import sys
from pathlib import Path
from jsonschema import validate, ValidationError

SCHEMA_PATH = Path("../config/dataset_metadata_schema.json")
EXAMPLE_METADATA_PATH = Path("../datasets/sample_dataset_metadata.json")

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def main(metadata_path):
    schema = load_json(SCHEMA_PATH)
    metadata = load_json(metadata_path)

    try:
        validate(instance=metadata, schema=schema)
        print(f"✅ {metadata_path.name} is valid.")
    except ValidationError as e:
        print(f"❌ Validation failed:\n{e.message}\n\nAt path: {e.path}")

if __name__ == "__main__":
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else EXAMPLE_METADATA_PATH
    main(path)
