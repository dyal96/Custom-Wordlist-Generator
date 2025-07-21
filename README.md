
# 🔐 Password Pattern Generator

A Python script designed to generate a comprehensive yet optimized list of potential password patterns based on target names and a specified range of birth years.  
This tool is useful for **security research**, **penetration testing**, or understanding **common password construction methods**.

---

## ✨ Features

- **Name-Based Patterns**  
  Generates variations of a given name (lowercase, uppercase, capitalized, simple leet speak, truncations).

- **Numeric & Special Character Combinations**  
  Intelligently combines name variations with common number sequences and special characters.

- **Date of Birth (DOB) Integration**  
  Incorporates common date formats from a user-defined range of years (defaulting to 1990–2050) into generated patterns.

- **Optimized Output**  
  Focuses on relevant and commonly observed password patterns, avoiding less effective combinations.

- **File-Based Input/Output**  
  Reads target names from an input text file and writes all unique generated password patterns to an output text file.

- **Uniqueness**  
  Ensures all generated patterns in the output file are unique.

---

## 🚀 Usage

### ✅ Prerequisites

- Python 3.x installed on your system

### 📦 Installation

This is a single-file script, so no special installation is required.  
Just download the `password_generator.py` file.

### ▶️ Running the Script

1. **Save the Script**  
   Save the provided Python code as `password_generator.py`.

2. **Create Input File**  
   In the same directory as the script, create a text file (e.g., `names.txt`) with one name per line.

   **Example `names.txt`:**
```

Alice
Bob Smith
Charlie

````

3. **Execute the Script**  
Open your terminal or command prompt and run:

```bash
python password_generator.py
````

4. **Provide File Names When Prompted:**

   ```
   Enter the input file name (e.g., names.txt): names.txt
   Enter the output file name (e.g., generated_passwords.txt): generated_passwords.txt
   ```

5. **View Output**
   A file named `generated_passwords.txt` will be created with all unique patterns.

---

## 📥 Input File (`names.txt`) Format

* Each line should contain **one target name**.
* Leading/trailing whitespace will be removed.
* Empty lines are ignored.

---

## 📤 Output File (`generated_passwords.txt`) Format

* Contains **one unique password pattern per line**.
* Patterns are **sorted alphabetically** for consistency.

---

## 💡 How It Works

The script combines multiple components to generate realistic password patterns:

### 🔁 Name Variations

* `name`, `NAME`, `Name`
* Removed spaces: `NameWithoutSpaces`
* Simple leet speak: `n@me`
* Short forms: First 3 letters (e.g., `nam`)

### 🔢 Numeric Patterns

* Common sequences: `123`, `786`, etc.
* Repeating digits: `11`, `222`
* Range from `0–99`

### 🔣 Special Characters

* Frequently used: `@`, `!`, `#`, `$`, etc.

### 📅 Date Patterns

* Formats like `DDMMYYYY`, `MMDDYY`, `YYYY`, `MMDD`
* Years from **1990 to 2050**

### 🔗 Combinations

* `Name + Numbers` (e.g., `Alice123`)
* `Name + SpecialChar + Numbers` (e.g., `Bob!1990`)
* `Name + Numbers + SpecialChar` (e.g., `Charlie123@`)
* Leet speak + combinations
* Hardcoded common patterns: `Name@123`, `Name!@#`

### 🧠 Uniqueness

All patterns are stored in a **Python set** to remove duplicates before writing to the output.

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes**, **security research**, and **ethical penetration testing only**.
Do **not** use it against systems without **explicit permission**—doing so is **illegal and unethical**.

The generated patterns are based on common trends and **do not guarantee** matching any specific password.
Use responsibly.

---

## 📄 License

This project is licensed under the **MIT License**.
See the `LICENSE` file (if applicable) for details.

```

Let me know if you'd like this as a downloadable `.md` file or if you want it styled for GitHub with badges, headers, or collapsible sections.
```
