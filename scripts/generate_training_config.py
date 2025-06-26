# ============================================================================
#
# generate_training_config.py
# auto-generates trainign_config.yaml using metadata and tokenizer info
# Jupyter Notebook Version of this is available in notebooks directory
#  ../notebooks/generate_training_config.ipynb
# NOTE: Run in this order:  
# 1. python generate_training_config.py
# 2. python config_loader.py
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
from pathlib import Path

metadata_path = Path("../datasets/sample_dataset_metadata.json")
tokenizer_path = Path("../tokenizer/custom_tokenizer.json")
output_path = Path("../config/training_config.yaml")

def generate_config():
    with open(metadata_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    config = {
        "project_name": "mini-indig-llm-kit",
        "language": meta["language"],
        "dialect": meta["dialect"],
        "version": meta["version"],
        "run_id": f"{meta['dialect'].lower()}-llm-qlora-v1",

        "base_model": {
            "name": "meta-llama/Llama-3-8B",
            "revision": "main",
            "quantization": "4bit",
            "architecture": "llama",
            "tokenizer_path": str(tokenizer_path)
        },

        "trainer": "qlora",
        "precision": "bf16",
        "use_flash_attention": False,
        "gradient_checkpointing": True,

        "dataset": {
            "name": f"{meta['language'].lower()}_{meta['dialect'].lower()}_dataset",
            "path": "../datasets/kanienkeha_prefixes.jsonl",
            "metadata": str(metadata_path),
            "format": "jsonl",
            "text_field": "text",
            "max_seq_length": 2048,
            "shuffle": True,
            "num_workers": 2,
            "tokenization_rules": "../tokenizer/kanienkeha_vocab_rules.yaml"
        },

        "training": {
            "epochs": 3,
            "batch_size": 2,
            "gradient_accumulation_steps": 8,
            "learning_rate": 2e-4,
            "weight_decay": 0.01,
            "warmup_steps": 20,
            "logging_steps": 10,
            "save_steps": 50,
            "eval_steps": 25,
            "seed": 42
        },

        "output": {
            "output_dir": "../models/eastern_llm",
            "model_card": "../models/generated_model_card.md",
            "save_total_limit": 2,
            "save_strategy": "steps",
            "eval_strategy": "steps"
        },

        "offline": {
            "tokenizer_cache": "../tokenizer/",
            "model_cache": "../models/base/",
            "allow_offline_mode": True
        },

        "evaluation": {
            "enabled": True,
            "notebook": "../notebooks/5_evaluation_metrics.ipynb",
            "metrics": [
                "exact_match",
                "morpheme_accuracy",
                "prefix_precision",
                "custom_speaker_validation"
            ]
        },

        "ethics": {
            "worksheet_path": "../ethics-protocols/ethics_team_input.csv",
            "respect_data_sovereignty": True,
            "require_contributor_consent": True,
            "dialect_guidelines_path": "../ethics-protocols/dialect_ethics.md"
        },

        "collaboration": {
            "contributors_file": str(metadata_path),
            "editable_notes": "../ethics-protocols/notes_by_team.csv",
            "session_tracking": "enabled"
        }
    }

    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        yaml.dump(config, f, sort_keys=False, allow_unicode=True)

    print(f"✅ training_config.yaml written to {output_path}")

if __name__ == "__main__":
    generate_config()
