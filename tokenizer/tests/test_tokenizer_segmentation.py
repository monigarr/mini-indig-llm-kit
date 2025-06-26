# ============================================================================
#
# test_tokenizer_segmentation.py
# Compares actual tokenizer outputs to expected morphemes.
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
from transformers import AutoTokenizer

def load_test_data(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def test_tokenizer(tokenizer_path, test_data_path):
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
    test_cases = load_test_data(test_data_path)

    print("🧪 Testing tokenizer segmentation quality...\n")

    for case in test_cases:
        input_text = case["input"]
        expected = case["expected_tokens"]
        output = tokenizer.tokenize(input_text)

        match = output == expected
        print(f"ID: {case['id']} | Dialect: {case['dialect']}")
        print(f"Input: {input_text}")
        print(f"Expected: {expected}")
        print(f"Tokenized: {output}")
        print("✅ Match\n" if match else "❌ Mismatch\n")

if __name__ == "__main__":
    test_tokenizer("tokenizer/custom_tokenizer.json", "tests/tokenizer_test_set.json")
