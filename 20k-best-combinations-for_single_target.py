# -*- coding: utf-8 -*-

def generate_password_patterns(name, dob=None):
    """
    Generates a list of password patterns based on a name and optional date of birth,
    including lowercase, uppercase, and capitalized variations.

    Args:
        name (str): The base name to generate patterns from.
        dob (str, optional): The date of birth in 'DDMMYYYY' format. Defaults to None.

    Returns:
        list: A list of unique password strings.
    """
    if not name:
        print("❌ Error: Name cannot be empty.")
        return []

    # --- Define Core Components for Patterns ---

    # 1. Number sequences
    number_sequences = [
        '1', '12', '123', '1234', '12345', '123456', '123456789', '21', '321', 
        '4321', '54321', '654321', '987654321', '123321', '786', '007', '69', '00', 
        '11', '22', '33', '44', '55', '66', '77', '88', '99', '000', '111', 
        '222', '333', '444', '555', '666', '777', '888', '999', '0000', '1111', 
        '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99','1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050',
    ]

    # 2. Special character patterns
    special_chars = ['', '@', '!', '#', '$', '*', '@#', '!@#', '#*', '*#', '##', '@@', '#@']

    # 3. Date patterns
    date_patterns = []
    if dob and len(dob) == 8 and dob.isdigit():
        d, m, yyyy = dob[0:2], dob[2:4], dob[4:8]
        yy = yyyy[2:4]
        date_patterns.extend([
            d, m, yy, yyyy, f"{d}{m}", f"{m}{d}", f"{m}{yy}", f"{m}{yyyy}",
            f"{d}{yy}", f"{d}{yyyy}", f"{d}{m}{yy}", f"{d}{m}{yyyy}", f"{m}{d}{yy}",
            f"{m}{d}{yyyy}"
        ])
    
    full_numeric_list = list(set(number_sequences + date_patterns))
    
    # --- ⭐ Create Name Variations (lowercase, UPPERCASE, Capitalized) ---
    name_variations = set([
        name.lower(),   # e.g., test
        name.upper(),   # e.g., TEST
        name.capitalize() # e.g., Test
    ])
    
    passwords = set()

    # --- Generate Patterns for each Name Variation ---
    for current_name in name_variations:
        # Pattern Group 1: Name + Special Chars + Numbers
        for num in full_numeric_list:
            for char_combo in special_chars:
                passwords.add(f"{current_name}{char_combo}{num}")

        # Pattern Group 2: Name + Numbers + Special Chars
        for num in full_numeric_list:
            for char_combo in special_chars:
                if char_combo:
                    passwords.add(f"{current_name}{num}{char_combo}")

    # --- Generate Leet Speak Variations (based on lowercase) ---
    leet_name = name.lower().replace('a', '@').replace('e', '3').replace('i', '1').replace('o', '0')
    if leet_name != name.lower():
        for num in full_numeric_list:
            for char_combo in special_chars:
                passwords.add(f"{leet_name}{char_combo}{num}")
                if char_combo:
                    passwords.add(f"{leet_name}{num}{char_combo}")
    
    # --- Add specific, complex patterns (based on Capitalized name) ---
    capitalized_name = name.capitalize()
    passwords.add(f"{capitalized_name.replace('a', '@').replace('e', '3')}@1996")
    passwords.add(f"{capitalized_name}@!@#")
    passwords.add(f"{capitalized_name}#@!23")

    return sorted(list(passwords))

# --- Example Usage ---
if __name__ == "__main__":
    input_name = input("Enter a base name (e.g., 'test'): ")
    input_dob = input("Enter a date of birth in DDMMYYYY format (or press Enter to skip): ")

    generated_passwords = generate_password_patterns(input_name, input_dob)

    if generated_passwords:
        print(f"\n✅ Successfully generated {len(generated_passwords)} password patterns for '{input_name}'.")
        
        save_file = input("Do you want to save the list to a file? (y/n): ").lower()
        if save_file == 'y':
            file_name = f"{input_name}_patterns.txt"
            with open(file_name, 'w', encoding='utf-8') as f:
                for pwd in generated_passwords:
                    f.write(pwd + '\n')
            print(f"📄 Patterns saved to {file_name}")
        else:
            print("\n--- Example Patterns (showing different cases) ---")
            # Show a few examples to demonstrate the new variations
            examples_to_find = [
                f"{input_name.lower()}123",
                f"{input_name.upper()}@123",
                f"{input_name.capitalize()}#123",
            ]
            for p in examples_to_find:
                 if p in generated_passwords:
                    print(f"FOUND: {p}")

            print("\n--- Preview of All Patterns ---")
            for pwd in generated_passwords[:20]:
                print(pwd)
            if len(generated_passwords) > 20:
                print(f"... and {len(generated_passwords) - 20} more.")