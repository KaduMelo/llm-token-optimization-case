# 📉 LLM Token Optimization Case

This repository demonstrates how **data formatting** can dramatically impact token usage when working with LLMs.

## 🚀 Scenario
We have a meeting transcript stored in JSON.  
It’s tempting to pass the raw JSON directly to the LLM — but that **doubles the token cost** compared to a lean, optimized format.

### Example with the dataset in this repo:
- Raw JSON: **1026 tokens**
- Custom format: **634 tokens**
- 💡 Savings: ~40%

## 🛠️ How to run

1. Clone the repository:
```bash
git clone https://github.com/KaduMelo/llm-token-optimization-case
cd llm-token-optimization-case
```

2. Create a virtual environment (recommended)
```bash
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the comparison
```bash
python scripts/compare.py
```