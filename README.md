# Password Generator

<p align="center">
  <strong>Secure • Customizable • Minimal</strong>
</p>

<p align="center">
  A modern command-line password generator built with Python, designed for reliability and ease of use.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Version-1.1-informational?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/CLI-Tool-black?style=flat-square">
  <img src="https://img.shields.io/badge/Security-Focused-blue?style=flat-square">
  <img src="https://img.shields.io/badge/Beginner-Friendly-lightgrey?style=flat-square">
</p>

---

## Table of Contents

* Overview
* Key Features
* Architecture
* Password Complexity Levels
* Getting Started
* Usage Example
* Project Structure
* Design Principles
* Roadmap
* Contributing
* License
* Contact

---

## Overview

**Password Generator** is a lightweight and efficient command-line application written in Python, focused on generating secure and customizable passwords.

The application enhances traditional password generation by integrating **real-world words** with randomized character sequences, improving usability without compromising security.

---

## Key Features

* Configurable password length with validation
* Enforced minimum length (≥ 8 characters)
* Five selectable complexity levels
* Integration of random dictionary words
* Secure random character generation
* Clean and intuitive CLI interaction
* Deterministic and maintainable logic structure

---

## Architecture

The application follows a simple and modular flow:

1. **Input Validation Layer**
   Ensures valid numeric input and enforces constraints

2. **Configuration Layer**
   Maps user-selected complexity levels to character sets

3. **Generation Engine**

   * Selects a random word
   * Generates random characters
   * Combines both into a final password

4. **Output Layer**
   Displays the generated password clearly to the user

---

## Password Complexity Levels

| Level | Composition                  |
| ----- | ---------------------------- |
| 1     | Letters (A–Z, a–z)           |
| 2     | Numbers (0–9)                |
| 3     | Letters and Numbers          |
| 4     | Letters and Symbols          |
| 5     | Letters, Numbers and Symbols |

---

## Getting Started

### Clone Repository

```bash id="aa12xz"
git clone https://github.com/yourusername/password-generator.git
cd password-generator
```

### Run Application

```bash id="bb98kl"
python main.py
```

---

## Usage Example

```text id="cc73pl"
Enter the password length: 14
Enter the password level (1-5): 5

Your password is: riverX#9kL!2pQ
MAKE SURE YOU SAVED THE CODE!
```

---

## Project Structure

```id="dd19op"
password-generator/
│
├── main.py        # Core application logic
└── README.md      # Project documentation
```

---

## Design Principles

* **Simplicity**
  Minimal dependencies and straightforward logic

* **Security**
  Strong randomness using Python standard libraries

* **Usability**
  Readable passwords through word integration

* **Maintainability**
  Clean structure and easily extendable code

---

## Roadmap

* Desktop GUI interface
* Web-based version (Flask / FastAPI)
* Password strength evaluation module
* Clipboard auto-copy functionality
* Custom dictionary support
* Randomized word placement

---

## Contributing

Contributions are encouraged.

To contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

## License

Distributed under the MIT License.

---

## Contact

Email: [arko-group@hotmail.com](mailto:arko-group@hotmail.com)
GitHub: https://github.com/IsarBit
