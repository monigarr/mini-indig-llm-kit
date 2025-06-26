# 🪶 Run Mini-Indig-LLM-Kit from a USB Drive  
## Community-Friendly Guide for Offline Use

---

### 🌍 Purpose

This guide explains how to run the **Mini-Indig-LLM-Kit** completely from a USB stick, portable SSD, or external hard drive — **with no internet required**.

This enables:
- Language learners, speakers, readers, writers and elders in remote regions to use the model.
- Onkwehonwe-led teams to keep data and tools portable and private.
- Safe experimentation on multiple computers (Windows, macOS, or Linux).

---

### 🧰 What You Need

| Resource                  | Description |
|---------------------------|-------------|
| USB drive or external SSD | Minimum 32GB (64GB+ recommended) |
| Offline copy of repository | `mini-indig-llm-kit/` cloned or zipped |
| Python 3.9+ installer     | For each target computer (or use portable Python) |
| Optional: Wheels folde

---

### 📁 USB Folder Structure

Your USB drive should look like this:

USB_DRIVE/
└── mini-indig-llm-kit/
├── offline-deployment/
│ ├── cpu_inference.py
│ ├── run_on_usb_instructions.md
│ └── low_resource_run_guide.md
├── tokenizer/
│ └── custom_tokenizer.json
├── models/
│ └── eastern_llm/
│ ├── config.json
│ ├── adapter_model.bin
│ └── tokenizer_config.json
├── notebooks/
├── datasets/
├── requirements.txt
└── README.md


> 📝 Tip: You can zip this whole project into `mini-indig-llm-kit.zip` before placing it on the USB to make copying easier.

---

### 🧪 Step-by-Step Instructions (Any Computer)

#### 1. Plug In USB

- Insert the USB drive into the computer.
- Open a terminal or command prompt.
- Navigate to the project folder on the USB:

```bash
cd /media/USERNAME/USB_DRIVE/mini-indig-llm-kit

(On Windows, it may be something like E:\mini-indig-llm-kit\)

2. Set Up Python Environment
If not already installed:

Install Python 3.9+ from the offline installer on the USB, or use portable Python if available.

Create a virtual environment on the USB (recommended):

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies
pip install --no-index --find-links=offline-deployment/wheels -r requirements.txt

🧠 If you don't have the wheels folder, ask your tech support lead to export one for offline install.

3. Run the LLM on CPU
Use the preloaded script to generate text in Kanien’kéha or other supported dialects:

python offline-deployment/cpu_inference.py \
  --model_path models/eastern_llm \
  --tokenizer_path tokenizer/custom_tokenizer.json \
  --prompt "Kenòn:we’s" \
  --max_tokens 50

  🔐 Offline-Only Mode
This project is fully runnable without the internet:

No server connection

No cloud services

Your language data stays local

If internet is accidentally enabled, the model will still run offline.

🧼 Cleaning Up / Moving USB
To safely eject your USB after use:

Exit the terminal or close Python

Use your system’s “eject” feature before removing the USB drive

🧭 Optional: Copy to Local Computer
If a user wants to install the full kit permanently:

cp -r /media/USB_DRIVE/mini-indig-llm-kit ~/Documents/

Or unzip mini-indig-llm-kit.zip and run setup there.

💬 Contact & Support
For updates, questions, or help preparing USB distributions for your region, contact:
MoniGarr.com LLC  |  MohawkLanguage.ca
Email: monigarr@monigarr.com
Website: https://www.MoniGarr.com 
Website: https://www.MohawkLanguage.ca
Text:  315-726-4058

🧡 Final Note
We believe every Onkwehonwe deserves tools to speak, teach, learn, practice, communicate with and share their languages — even without stable internet or new hardware. Without requiring your community’s sacred stories to be uploaded to the internet without your cultural protocols and practices being respected.

This project is for you.

Nia:wen kó:wa — Thank you for keeping the language alive.