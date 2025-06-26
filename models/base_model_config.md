# Base Model Configuration for Kanien’kéha Verb Conjugation Project

## Project Overview
This project focuses on generating, analyzing, and visualizing Kanien’kéha (Mohawk) verb conjugations, specifically targeting the verb root **nòn:we’s** ("to like"). The model aims to assist language learners and revitalization efforts by producing accurate conjugation forms, educational charts, and practice materials.

---

## Model Purpose
- Automate generation of Kanien’kéha verb conjugations based on pronominal prefixes, roots, and suffixes.
- Provide color-coded, clear visualizations of conjugation components (prefixes, roots, suffixes).
- Support creation of printable educational materials such as charts and worksheets.
- Enable learners to understand and practice complex polysynthetic verb forms.

---

## Model Architecture
- Rule-based morphological generation system driven by Kanien’kéha grammar rules.
- Custom prefix and suffix tagging for color coding in output.
- Template-based text rendering for printable outputs (PDF, HTML).
- Extendable for additional verb roots, tenses, and moods.

---

## Input Data
- Verb root: `nòn:we’s`
- Pronominal prefixes (subject/object markers)
- Tense markers (present, past, future)
- Person and number markers (singular, dual, plural)
- Sample conjugations for training and validation

---

## Output Formats
- Color-coded conjugation tables (PDF)
- Blank practice worksheets (PDF)
- Exportable datasets for further NLP or educational tool integration

---

## Usage Instructions
- Update the morphological rules in the configuration file `/config/training_config.yaml` for new verbs.
- Add new prefix/suffix sets for additional tenses or moods.
- Use template scripts to regenerate charts and worksheets as needed.
- Integrate with language learning platforms or classroom tools.

---

## Maintenance and Contributions
- Repository: https://www.github.com/monigarr/mini_indig_llm_kit 
- Contributions are welcome for:
  - Expanding verb root datasets
  - Enhancing morphological accuracy
  - Adding interactive web visualizations
- Please follow the code of conduct and contribution guidelines.

---

## Contact
- Maintainer: MoniGarr (monigarr@monigarr.com)
- Affiliation: Akwesasne | MoniGarr.com LLC |  MohawkLanguage.ca

---

*This configuration file is part of the Kanien’kéha Verb Conjugation Project focused on Kanien’kéha Revival & Retention through Onkwehonweheha AI techniques (Ancient Intelligence collaborating with Artificial Intelligence*
