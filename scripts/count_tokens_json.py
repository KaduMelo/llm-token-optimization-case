import json
import tiktoken
from pathlib import Path

def count_tokens(text: str, model: str = "gpt-4o-mini"):
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))

def main():
    path = Path(__file__).parent.parent / "data" / "transcript.json"
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()

    tokens = count_tokens(data)
    print(f"Raw JSON: {tokens} tokens")

if __name__ == "__main__":
    main()
