# Key Generator

A simple Python tool to generate RSA key pairs (private and public), format them for various uses, and save them in a designated directory.

---

## Project Structure

```
key-generator/           # Project root
├── generated_keys/      # Output directory for generated keys
├── venv/                # Python virtual environment
├── key_generator.py     # Module for key generation, formatting, saving
├── main.py              # CLI entry point
├── requirements.txt     # Project dependencies
└── README.md            # This documentation
```

---

## Prerequisites

- Python 3.8+ installed on your system
- `venv` module available (standard in Python 3)

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repo-url> key-generator
   cd key-generator
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate    # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Run the main script:
   ```bash
   python3 main.py
   ```

2. Follow the prompts:
   - **Base name**: Enter a name for the key files (e.g., `my_key`).
   - **Passphrase**: Choose whether to encrypt the private key; if yes, enter a secure passphrase.

3. After execution, the `generated_keys/` directory will contain:
   - `<base_name>_private.pem` : Encrypted (or plain) private key in PEM format with `\n` literals.
   - `<base_name>_public.pem`  : Public key in standard PEM format.
   - `<base_name>_public`      : Public key as a single-line Base64 string.

---

## Examples

```bash
$ python3 main.py
Enter the base name for the keys (without extension): my_key
Do you want to use a passphrase for the private key? (y/N): N

Keys have been saved in the 'generated_keys' directory:
 - my_key_private.pem
 - my_key_public.pem
 - my_key_public
```

---

## License

MIT License © 2025

