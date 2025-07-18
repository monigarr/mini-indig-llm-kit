# ============================================================================
#
# vocab_builder.py
#  Load a text corpus (sample_corups.txt)
#  tokenize it using whiespace or custom tokenizer
#  count and visualize: 
#  word / token frequency
#  character n-grams (roots, affixes, suffixes)
#  estimated morphemes using simple rules
#  Save Output to:
#  .csv files for further analysis
#  .png plots for fast visualization
# Analyze a polysynthetic language corpus to extract and visualize:
#  Token frequencies
#  Character n-grams
#  Estimated morphemes
# Designed for Indigenous languages with complex morphology.
# 
# OUTPUT DIRECTORY: datasets/vocab_analysis
# - token_frequencies.csv  top words / tokens
# - top_tokens.png  bar chart of token freq
# - char_ngrams.csv  most common character n-grams
# - top_char_ngrams.png  bar chart of n-gram freq
# - estimated_morphemes.csv  long complex token candidates
# 
# POLYSYNTHETIC CONSIDERATIONS
# - this script uses basic heuristics ideal for early exploratory analysis
# - can swap in your custom tokenizer (SentencePiece, Unigram or BPE)
# - extend morpheme logic by including language-specific suffix / prefix lists """
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

import os
import re
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from pathlib import Path

# Set paths
input_file = "sample_corpus.txt"
output_dir = "vocab_analysis/"
Path(output_dir).mkdir(parents=True, exist_ok=True)

# Load corpus
with open(input_file, "r", encoding="utf-8") as f:
    corpus_lines = [line.strip().lower() for line in f if line.strip()]

# Tokenization (basic whitespace; you can customize for BPE or morphemes)
tokens = []
for line in corpus_lines:
    tokens.extend(re.findall(r"\b\w+\b", line))

# Token frequency
token_counts = Counter(tokens)
most_common_tokens = token_counts.most_common(50)

# Save token freq to CSV
df_tokens = pd.DataFrame(most_common_tokens, columns=["token", "count"])
df_tokens.to_csv(f"{output_dir}token_frequencies.csv", index=False)

# Plot token frequencies
plt.figure(figsize=(12, 6))
df_tokens.plot(kind="bar", x="token", y="count", legend=False)
plt.title("Top 50 Most Common Tokens")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f"{output_dir}top_tokens.png")
plt.close()

# Extract character n-grams (potential roots, affixes, etc.)
char_ngrams = Counter()
for token in tokens:
    token = f"_{token}_"  # padding for affix detection
    for n in range(2, 6):  # bigrams to 5-grams
        for i in range(len(token) - n + 1):
            char_ngrams[token[i:i+n]] += 1

common_ngrams = char_ngrams.most_common(50)
df_ngrams = pd.DataFrame(common_ngrams, columns=["ngram", "count"])
df_ngrams.to_csv(f"{output_dir}char_ngrams.csv", index=False)

# Plot n-gram frequencies
plt.figure(figsize=(12, 6))
df_ngrams.plot(kind="bar", x="ngram", y="count", legend=False)
plt.title("Top Character N-Grams (Affixes, Roots, Morphemes)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f"{output_dir}top_char_ngrams.png")
plt.close()

# Estimate morphemes (simplified heuristic: hyphenated/long tokens)
morpheme_like = [token for token in tokens if "-" in token or len(token) > 8]
morpheme_counts = Counter(morpheme_like).most_common(30)

df_morphemes = pd.DataFrame(morpheme_counts, columns=["morpheme_candidate", "count"])
df_morphemes.to_csv(f"{output_dir}estimated_morphemes.csv", index=False)

# Log summary
print("✅ Vocabulary analysis complete.")
print(f"- Token frequency CSV: {output_dir}token_frequencies.csv")
print(f"- Top token plot: {output_dir}top_tokens.png")
print(f"- Char n-gram CSV: {output_dir}char_ngrams.csv")
print(f"- Morpheme candidates: {output_dir}estimated_morphemes.csv")
