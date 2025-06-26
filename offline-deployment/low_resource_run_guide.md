# Mini-Indig-LLM-Kit  
## Low Resource Offline Run Guide

---

### Purpose

This guide helps you **run and use the Mini-Indig-LLM-Kit** language model **offline** on low-resource computers (e.g., older laptops, community centers, or limited bandwidth environments).

It covers:

- Setting up the environment with minimal internet
- Running inference on CPU-only machines
- Using pretrained tokenizer and model files without cloud dependencies
- Basic troubleshooting tips

---

### Requirements

- A computer running **Linux, Windows, or macOS** (64-bit recommended)
- Python 3.9+ installed
- At least **8 GB RAM** (more is better, but 8GB can run inference at modest speed)
- Local copies of:
  - Pretrained Mini-Indig-LLM-Kit model files (from `/models/`)
  - Custom tokenizer files (from `/tokenizer/`)
  - `cpu_inference.py` script (from `/offline-deployment/`)

---

### Step 1: Setup Python Environment (Offline-Friendly)

1. Create a Python virtual environment:
   ```bash
   python3 -m venv miniindig_env
   source miniindig_env/bin/activate  # On Windows: miniindig_env\Scripts\activate

Install dependencies using offline wheels or cached packages (if internet is not available, ask your project coordinator for .whl files):
pip install torch torchvision --no-index --find-links=/path/to/wheels
pip install -r requirements.txt --no-index --find-links=/path/to/wheels

If you have internet, just run pip install -r requirements.txt

### Step 2: Setup Python Environment (Offline-Friendly)
Step 2: Prepare Model and Tokenizer Files
Ensure you have downloaded and extracted the following folders locally:

models/eastern_llm/ — Fine-tuned LLaMA 3 8B model files (4-bit QLoRA quantized)

tokenizer/ — Custom tokenizer JSON and vocab YAML files

These files must be accessible relative to the inference script, or edit paths inside cpu_inference.py.

### Step 3: Run CPU Inference
Use the provided cpu_inference.py script to run the model locally without GPU:
replace --prompt with your own Kanien’kéha phrase or question.
output will be printed in your console.

python offline-deployment/cpu_inference.py \
  --model_path ../models/eastern_llm \
  --tokenizer_path ../tokenizer/custom_tokenizer.json \
  --prompt "Tsi ní:ioht ne wa’kè:ron?" \
  --max_tokens 50

### Step 4: Customizing Prompts and Settings
You can adjust the maximum tokens generated with --max_tokens.

Use --temperature to control randomness (default 0.7).

See python offline-deployment/cpu_inference.py --help for all options.

| Problem                   | Solution                                            |
| ------------------------- | --------------------------------------------------- |
| Model loading errors      | Check model and tokenizer paths; ensure files exist |
| Out of memory errors      | Reduce batch size or max tokens; close other apps   |
| Slow performance          | Use lower `max_tokens`; run overnight if needed     |
| Python environment issues | Recreate venv; ensure Python 3.9+ and pip installed |


Additional Notes
This guide assumes no internet connection during inference.

If your system supports GPU, consider using GPU-enabled inference scripts for better speed.

Community members can share prompts and best practices via the project’s GitHub or local communication channels.

Resources
Mini-Indig-LLM-Kit GitHub Repository

/offline-deployment/cpu_inference.py — Offline inference script

/tokenizer/ — Custom tokenizer files

/models/ — Trained model files

Support & Contact
For help, reach out to your project lead or email: support@miniindigllm.org

Nia:wen kó:wa — Thank you for supporting Kanien’kéha Revival & Retention efforts!

