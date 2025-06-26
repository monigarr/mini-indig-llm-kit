# ============================================================================
#
# test_tokenizer.py
# RUN WITH: # python tokenizer/test_tokenizer.py
# Load the trained tokenizer and segment a test sentence.
# Useful for checking if known prefixes and roots are retained.
# Use model_type=unigram for morphologically rich, low-resource languages.
# This tokenizer is compatible with HuggingFace models (via PreTrainedTokenizerFast).
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

import sentencepiece as spm

model_path = "kanienkeha_tokenizer.model"
sp = spm.SentencePieceProcessor()
sp.load(model_path)

test_sentences = [
    "Kenòn:we’s tsi ní:io?",
    "Wari’kó:wa iontáhkwa ní:se.",
    "Iakoia’takarénies tsi ní:ioht ne ó:nen."
]

for sentence in test_sentences:
    pieces = sp.encode(sentence, out_type=str)
    print(f"\n📘 Original: {sentence}")
    print(f"🧩 Segmented: {' | '.join(pieces)}")
