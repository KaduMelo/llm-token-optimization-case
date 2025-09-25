import subprocess

def run_script(script):
    result = subprocess.run(["python", script], capture_output=True, text=True)
    return result.stdout.strip()

def main():
    print("🔎 Comparing token counts...\n")
    raw = run_script("scripts/count_tokens_json.py")
    formatted = run_script("scripts/count_tokens_custom_format.py")

    print(raw)
    print(formatted)

    raw_tokens = int(raw.split(":")[1].split()[0])
    formatted_tokens = int(formatted.split(":")[1].split()[0])
    reduction = (raw_tokens - formatted_tokens) / raw_tokens * 100

    print(f"\n💡 Savings: {reduction:.2f}% fewer tokens")

if __name__ == "__main__":
    main()
