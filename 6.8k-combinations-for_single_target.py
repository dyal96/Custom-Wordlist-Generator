import re
from datetime import datetime

INPUT_FILE = "names.txt"
OUTPUT_FILE = "smart_passwords.txt"

NUM_SUFFIXES = ["123", "1234", "12345", "123456", "111", "1111", "007", "786", "0000", "9999"]
REPEAT_SEQ = ["111", "2222", "3333"]
YEARS = [str(y) for y in range(1990, datetime.now().year + 1)]
MONTHS = [f"{m:02d}" for m in range(1, 13)]
SYMBOLS = ["@", "!", "#", "$"]
COMMON_WORDS = ["india", "king", "queen", "boss", "love", "pass"]
LENGTH_MIN = 8
LENGTH_MAX = 18  # WPA2/3 sweet spot

def all_casings(name):
    return {name.lower(), name.capitalize(), name.upper()}

def build_variants(name):
    # Handles core and extended patterns based on leaks and common tendencies.
    variants = set()
    casings = all_casings(name)
    for base in casings:
        # Suffixes and Symbol+Suffix
        for s in NUM_SUFFIXES:
            variants.add(f"{base}{s}")
            for sym in SYMBOLS:
                variants.add(f"{base}{sym}{s}")
                variants.add(f"{base}{s}{sym}")
                variants.add(f"{sym}{base}{s}")
                variants.add(f"{s}{base}{sym}")

        # Years, years with symbol, MMYYYY
        for year in YEARS:
            variants.add(f"{base}{year}")
            variants.add(f"{base}@{year}")
            variants.add(f"{year}{base}")
            for sym in SYMBOLS:
                variants.add(f"{base}{year}{sym}")
                variants.add(f"{base}{sym}{year}")
                variants.add(f"{year}{sym}{base}")

            # MMYYYY combos
            for m in MONTHS:
                variants.add(f"{base}@{m}{year}")
                variants.add(f"{base}{m}{year}")
                variants.add(f"{m}{year}{base}")
                variants.add(f"{m}{year}@{base}")

        # Prefix numbers to name
        for s in NUM_SUFFIXES:
            variants.add(f"{s}{base}")
        # Prefix years
        for year in YEARS:
            variants.add(f"{year}{base}")

        # Repetition and special additions
        for r in REPEAT_SEQ:
            variants.add(f"{base}{r}")

        # Common words as suffix and @suffix
        for word in COMMON_WORDS:
            variants.add(f"{base}{word}")
            variants.add(f"{base}@{word}")

        # Symbol only
        for sym in SYMBOLS:
            variants.add(f"{base}{sym}")
            variants.add(f"{sym}{base}")

        # Number and symbol together
        for s in NUM_SUFFIXES:
            for sym in SYMBOLS:
                variants.add(f"{base}{sym}{s}")
                variants.add(f"{base}{s}{sym}")
                variants.add(f"{sym}{base}{s}")

        # Optional: 2-layer patterns (slower, combinatoric)
        variants.add(f"{base}12345678")
        variants.add(f"{base}@123456")
        variants.add(f"{base}@1234")
        variants.add(f"{base}@{base}")

    # Filter: Length
    return set(p for p in variants if LENGTH_MIN <= len(p) <= LENGTH_MAX)

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        names = {line.strip() for line in file if line.strip()}
    print(f"Loaded {len(names)} names. Generating pattern-based dictionary...")

    all_passwords = set()
    for name in names:
        all_passwords.update(build_variants(name))
    print(f"Generated {len(all_passwords)} passwords. Writing...")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        for pwd in sorted(all_passwords):
            file.write(pwd + "\n")
    print(f"✅ Optimized wordlist written to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
