# generate_morphemes_json.py
# reads kanienkeha_vocab_rules.yaml and data_template.json to generate a standardized morphemes.json file

import json
import yaml

def load_yaml_rules(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def load_data_template(json_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def extract_morphemes(entry, rules):
    output = {
        "id": entry["id"],
        "input_text": entry["input_text"],
        "translation": entry["translation"],
        "morpheme_gloss": entry["morpheme_gloss"],
        "morpheme_tags": entry["morpheme_tags"],
        "stem_type": entry["stem_type"],
        "category": entry["category"],
        "dialect": entry["dialect"],
        "speaker_id": entry["speaker_id"],
        "speaker_role": entry["speaker_role"],
        "source": entry["source"],
        "validation_status": entry["validation_status"],
        "tokenized": entry["tokenized"],
        "notes": entry["notes"],
        "usage_context": entry["usage_context"]
    }
    return output

def build_morphemes_json(yaml_path, json_path, output_path="morphemes.json"):
    rules = load_yaml_rules(yaml_path)
    data = load_data_template(json_path)
    morphemes = [extract_morphemes(entry, rules) for entry in data]

    with open(output_path, 'w', encoding='utf-8') as outfile:
        json.dump(morphemes, outfile, indent=2, ensure_ascii=False)
    print(f"✅ Morphemes file saved to {output_path}")

if __name__ == "__main__":
    build_morphemes_json(
        yaml_path="kanienkeha_vocab_rules.yaml",
        json_path="data_template.json"
    )
