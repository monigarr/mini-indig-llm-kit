# ============================================================================
#
# cpu_inference.py
#
# Run a fine-tuned QLoRA LLaMA 3 model on a low-resource, offline CPU machine.
# Ensure you have manually downloaded and placed the model in /models/llama3-8b-qlora-output
# usage: python offline-deployment/cpu_inference.py
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

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Path to locally saved fine-tuned model
model_path = "../models/llama3-8b-qlora-output"

# Load tokenizer
print("🔄 Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=True)

# Load model on CPU only
print("🔄 Loading model on CPU...")
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="cpu",
    torch_dtype=torch.float32
)

# Create generation pipeline
print("✅ Model and tokenizer loaded.")
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)

# Prompt loop for user input
print("\n🧠 Indigenous Mini LLM (CPU Mode)\nType a prompt below or type 'exit' to quit.")

while True:
    prompt = input("\nEnter prompt: ").strip()
    if prompt.lower() in ["exit", "quit"]:
        break
    output = generator(prompt, max_length=128, num_return_sequences=1, do_sample=True)
    print("\n🗨️ Generated Response:\n", output[0]['generated_text'])
