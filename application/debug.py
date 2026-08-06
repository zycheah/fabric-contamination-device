import os

def print_total_lines():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Scanning directory: {base_dir}\n")

    rp2040 = 100

    total_lines = rp2040
    for fname in os.listdir(base_dir):
        fullpath = os.path.join(base_dir, fname)
        if os.path.isfile(fullpath):
            try:
                # 3) Open and count lines
                with open(fullpath, 'r', encoding='utf-8') as f:
                    count = sum(1 for _ in f)
                print(f"{fname:<30} : {count:>5} lines")
                total_lines += count
            except Exception:
                # skip files that aren’t text‐readable
                print(f"{fname:<30} : (skipped)")
                continue

    print(f"\nTotal number of lines across all files: {total_lines}")

if __name__ == "__main__":
    print_total_lines()