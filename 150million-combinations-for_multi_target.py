# -*- coding: utf-8 -*-

def generate_password_patterns(name, dob_years=None):
    """
    Generates a list of optimized password patterns based on a name and optional
    list of years for DOB, including lowercase, uppercase, and capitalized variations.

    Args:
        name (str): The base name to generate patterns from.
        dob_years (list, optional): A list of years (as integers) to use for DOB patterns.
                                   Defaults to None.

    Returns:
        list: A list of unique and optimized password strings.
    """
    if not name:
        print("❌ Error: Name cannot be empty.")
        return []

    # --- Define Core Components for Optimized Patterns ---

    # 1. Number sequences (more focused and common)
    number_sequences = [
        '1', '12', '123', '1234', '12345', '123456', '786', '007', '69',
        '11', '22', '33', '44', '55', '66', '77', '88', '99',
        '000', '111', '222', '333', '444', '555', '666', '777', '888', '999',
        '123321' # A common sequence
    ]
    # Add common two-digit and single-digit numbers (0-99)
    for i in range(100):
        number_sequences.append(str(i).zfill(1)) # '0', '1', ..., '9'
        if i >= 10:
            number_sequences.append(str(i)) # '10', '11', ..., '99'

    # 2. Special character patterns (more common choices)
    special_chars = ['', '@', '!', '#', '$', '*', '~', '&', '%', '^', '_', '-']

    # 3. Date patterns (limited to common formats from specified years and months)
    date_patterns = []
    if dob_years:
        for year in dob_years:
            yyyy = str(year)
            yy = yyyy[2:4]
            # Common month variations (e.g., 01-12)
            for month in range(1, 13):
                m = f"{month:02d}"
                # Common day variations (e.g., 01-31)
                for day in range(1, 32): # Covers most days, will generate some invalid dates, but common
                    d = f"{day:02d}"
                    date_patterns.extend([
                        f"{d}{m}{yyyy}",  # DDMMYYYY
                        f"{m}{d}{yyyy}",  # MMDDYYYY
                        f"{d}{m}{yy}",    # DDMMYY
                        f"{m}{d}{yy}",    # MMDDYY
                        f"{yyyy}",        # YYYY
                        f"{yy}",          # YY
                        f"{m}",           # M or MM
                        f"{d}",           # D or DD
                        f"{d}{m}",        # DM or DDMM
                        f"{m}{d}",        # MD or MMDD
                    ])
    
    # Combine and deduplicate numeric and date patterns
    full_numeric_list = list(set(number_sequences + date_patterns))
    
    # --- ⭐ Create Name Variations (lowercase, UPPERCASE, Capitalized, etc.) ---
    name_variations = set([
        name.lower(),        # e.g., test
        name.upper(),        # e.g., TEST
        name.capitalize(),   # e.g., Test
        name.replace(" ", "") # no spaces
    ])
    # Add common name truncations/variations
    if len(name) > 3:
        name_variations.add(name[:3].lower()) # first 3 letters
        name_variations.add(name[:3].capitalize()) # First 3 capitalized
        name_variations.add(name.lower().replace('e','3')) # Simple common substitutions

    passwords = set()

    # --- Generate Optimized Patterns ---
    for current_name in name_variations:
        # Pattern Group 1: Name + Numbers (most common and effective)
        for num in full_numeric_list:
            passwords.add(f"{current_name}{num}")

        # Pattern Group 2: Name + Special Chars + Numbers
        for char_combo in special_chars:
            if char_combo: # Only add if there's a special char
                for num in full_numeric_list:
                    passwords.add(f"{current_name}{char_combo}{num}")

        # Pattern Group 3: Name + Numbers + Special Chars
        for num in full_numeric_list:
            for char_combo in special_chars:
                if char_combo: # Only add if there's a special char
                    passwords.add(f"{current_name}{num}{char_combo}")
        
        # Leet Speak Variations for common combinations (on lowercase name)
        leet_name = current_name.replace('a', '@').replace('e', '3').replace('i', '1').replace('o', '0').replace('s', '5').replace('l', '1').replace('t', '7')
        if leet_name != current_name:
             # LeetName + Numbers
            for num in full_numeric_list:
                passwords.add(f"{leet_name}{num}")
            # LeetName + SpecialChar + Numbers
            for char_combo in special_chars:
                if char_combo:
                    for num in full_numeric_list:
                        passwords.add(f"{leet_name}{char_combo}{num}")
            # LeetName + Numbers + SpecialChar
            for num in full_numeric_list:
                for char_combo in special_chars:
                    if char_combo:
                        passwords.add(f"{leet_name}{num}{char_combo}")

    # --- Add specific, highly common complex patterns ---
    # These are often seen regardless of the name's simple permutations
    passwords.add(f"{name.capitalize()}@123")
    passwords.add(f"{name.lower()}!@#")
    passwords.add(f"{name.capitalize()}#@!23")
    passwords.add(f"{name.lower()}2024") # Common current year
    passwords.add(f"{name.capitalize()}@!")
    passwords.add(f"{name.lower()}#$")
    passwords.add(f"{name.lower()}12345")
    passwords.add(f"{name.capitalize()}@1") # Name@1
    passwords.add(f"{name.capitalize()}@0") # Name@0
    passwords.add(f"{name.capitalize()}!")
    passwords.add(f"{name.capitalize()}@")


    return sorted(list(passwords))

# --- Main Execution Block ---
if __name__ == "__main__":
    all_generated_passwords = set()

    # Define the desired DOB year range
    dob_years_for_generation = list(range(1990, 2051)) # Includes 1990 to 2050

    input_file = input("Enter the input file name (e.g., names.txt): ")
    output_file = input("Enter the output file name (e.g., generated_passwords.txt): ")

    try:
        with open(input_file, 'r', encoding='utf-8') as f_names:
            target_names = [line.strip() for line in f_names if line.strip()]
    except FileNotFoundError:
        print(f"❌ Error: '{input_file}' not found. Please ensure the file exists.")
        exit()
    except Exception as e:
        print(f"❌ An error occurred while reading '{input_file}': {e}")
        exit()

    if not target_names:
        print(f"⚠️ Warning: '{input_file}' is empty. No passwords will be generated.")
    else:
        print(f"\n⚙️ Starting password generation for {len(target_names)} names from '{input_file}'...")
        for name_target in target_names:
            print(f"  Generating patterns for: {name_target}")
            generated_for_name = generate_password_patterns(name_target, dob_years=dob_years_for_generation)
            all_generated_passwords.update(generated_for_name)
            print(f"  Generated {len(generated_for_name)} patterns for '{name_target}'. Total unique patterns so far: {len(all_generated_passwords)}")

    if all_generated_passwords:
        try:
            with open(output_file, 'w', encoding='utf-8') as f_output:
                for pwd in sorted(list(all_generated_passwords)):
                    f_output.write(pwd + '\n')
            print(f"\n✅ Successfully generated {len(all_generated_passwords)} unique password patterns and saved to '{output_file}'")
        except Exception as e:
            print(f"❌ An error occurred while writing to '{output_file}': {e}")
    else:
        print("\n❌ No passwords were generated.")