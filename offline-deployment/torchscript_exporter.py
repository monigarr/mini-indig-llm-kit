# ============================================================================
#
# torchscript_exporter.py
# This script exports a fine-tuned, quantized Mini-Indig-LLM-Kit model 
# to TorchScript format for offline use in low-resource environments.
# A Jupyter Notebook Version of this script is also available in this project:
# ../notebooks/torchscript_exporter.ipynb
# A Helper script of this script is also available in this project:
# ../scripts/torchscript_infer.py
# Usage: 
# * You only need to run this once per model version.
# * Resulting .pt file can be loaded directly with torch.jit.load() on any machine running PyTorch
# python torchscript_exporter.py \
#   --model_path ../models/eastern_llm \
#   --output_path ../offline-deployment/exported_torchscript.pt
#   python offline-deployment/torchscript_exporter.py \
#       --model_path models/eastern_llm \
#       --output_path offline-deployment/eastern_llm_torchscript.pt \
#       --tokenizer_path tokenizer/custom_tokenizer.json
# 📦 Output Example
#     offline-deployment/eastern_llm_torchscript.pt — 4-bit quantized, TorchScript-compatible, small-footprint model
#     Ideal for distribution via USB, kiosks, mobile apps, or Raspberry Pi """
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
from transformers import AutoModelForCausalLM, AutoTokenizer


def export_model(model_path, output_path, tokenizer_path=None, max_seq_len=128):
    print(f"🔧 Loading model from: {model_path}")
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        low_cpu_mem_usage=True,
    )
    model.eval()

    print("🔧 Building dummy input...")
    if tokenizer_path:
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
    else:
        tokenizer = AutoTokenizer.from_pretrained(model_path)

    example_input = tokenizer("Kenòn:we’s", return_tensors="pt", padding="max_length", max_length=max_seq_len)
    input_ids = example_input["input_ids"]

    print(f"📦 Tracing model and exporting to TorchScript: {output_path}")
    traced = torch.jit.trace(model, (input_ids,))
    torch.jit.save(traced, output_path)

    print(f"✅ Export complete: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export Mini-Indig-LLM-Kit to TorchScript.")
    parser.add_argument("--model_path", type=str, required=True, help="Path to the fine-tuned model directory.")
    parser.add_argument("--output_path", type=str, required=True, help="Path to save the exported TorchScript file.")
    parser.add_argument("--tokenizer_path", type=str, default=None, help="Optional path to tokenizer.")
    parser.add_argument("--max_seq_len", type=int, default=128, help="Sequence length for dummy input.")
    args = parser.parse_args()

    export_model(
        model_path=args.model_path,
        output_path=args.output_path,
        tokenizer_path=args.tokenizer_path,
        max_seq_len=args.max_seq_len
    )
