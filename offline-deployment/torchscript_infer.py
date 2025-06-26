# ============================================================================
#
# ../offline-deployment/torchscript_infer.py
#
# Helper to load and run a TorchScript .pt model on plain text inputs 

# ../offline-deployment/torchscript_exporter.py
# torchscript_infer.py#
# Run inference from a TorchScript-compiled Mini-Indig-LLM-Kit model offline.
# Usage:
#   python torchscript_infer.py --model_path eastern_llm_torchscript.pt --prompt "Kenòn:we’s"
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

import argparse
import torch
from transformers import AutoTokenizer

def run_inference(model_path, tokenizer_path, prompt, max_tokens=50):
    print(f"📦 Loading TorchScript model: {model_path}")
    model = torch.jit.load(model_path)
    model.eval()

    print(f"📚 Loading tokenizer from: {tokenizer_path}")
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)

    input_ids = tokenizer(prompt, return_tensors="pt").input_ids

    with torch.no_grad():
        output_ids = model.generate(input_ids, max_length=max_tokens, do_sample=True)

    decoded = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    print(f"🗣️ Output:\n{decoded}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str, required=True, help="Path to the .pt TorchScript file.")
    parser.add_argument("--tokenizer_path", type=str, required=True, help="Path to tokenizer directory or file.")
    parser.add_argument("--prompt", type=str, required=True, help="Text prompt to generate from.")
    parser.add_argument("--max_tokens", type=int, default=50, help="Maximum number of tokens to generate.")
    args = parser.parse_args()

    run_inference(args.model_path, args.tokenizer_path, args.prompt, args.max_tokens)
