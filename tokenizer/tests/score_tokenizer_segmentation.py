# ============================================================================
#
# score_tokenizer_segmentation.py
# 🔹 t001 | Eastern
# Input: Kenòn:we’s ne onénhste.
# Expected: ['ke-', 'nòn:', 'we', '’s', 'ne', 'onénhste', '.']
# Predicted: ['ke-', 'nòn:', 'we', '’s', 'ne', 'onénhste', '.']
# ✅ Precision: 1.00 | Recall: 1.00
# 📊 Average Precision: 0.94
# 📊 Average Recall: 0.92
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
import csv
from transformers import AutoTokenizer
from sklearn.metrics import precision_score, recall_score

def load_csv(csv_path):
    cases = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            expected = [token.strip() for token in row["expected_tokens"].split(",")]
            cases.append({
                "id": row["id"],
                "dialect": row["dialect"],
                "input": row["input"],
                "expected_tokens": expected
            })
    return cases

def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]

def calculate_token_overlap(true_tokens, predicted_tokens):
    true_set = set(true_tokens)
    pred_set = set(predicted_tokens)
    tp = len(true_set & pred_set)
    fp = len(pred_set - true_set)
    fn = len(true_set - pred_set)

    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    return precision, recall

def score_tokenizer(tokenizer_path, csv_path):
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
    test_cases = load_csv(csv_path)

    total_precision = 0
    total_recall = 0
    for case in test_cases:
        pred = tokenizer.tokenize(case["input"])
        precision, recall = calculate_token_overlap(case["expected_tokens"], pred)
        total_precision += precision
        total_recall += recall

        print(f"🔹 {case['id']} | {case['dialect']}")
        print(f"Input: {case['input']}")
        print(f"Expected: {case['expected_tokens']}")
        print(f"Predicted: {pred}")
        print(f"✅ Precision: {precision:.2f} | Recall: {recall:.2f}\n")

    avg_p = total_precision / len(test_cases)
    avg_r = total_recall / len(test_cases)
    print(f"📊 Average Precision: {avg_p:.2f}")
    print(f"📊 Average Recall: {avg_r:.2f}")

if __name__ == "__main__":
    score_tokenizer("../tokenizer/custom_tokenizer.json", "../tokenizer/tests/tokenizer_test_set.csv")
