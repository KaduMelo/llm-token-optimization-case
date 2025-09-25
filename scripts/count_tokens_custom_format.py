import json
import tiktoken
from pathlib import Path

def count_tokens(text: str, model: str = "gpt-4o-mini"):
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))

def main():
    path = Path(__file__).parent.parent / "data" / "transcript.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Create header + formatted rows
    header = "speaker | confidence | text | start | end"
    rows = [
        f"{item['speaker']} | {item['confidence']} | {item['text']} | {item['start']} | {item['end']}"
        for item in data
    ]
    formatted = header + "\n" + "\n".join(rows)

    tokens = count_tokens(formatted)
    print(f"Custom format: {tokens} tokens")

if __name__ == "__main__":
    main()
