"""
main.py

This is the main module that interacts with the user, generates RSA keys,
formats them with literal '\\n' for newlines, and saves the keys in a designated directory.
"""

import getpass
from key_generator import generate_keys, format_key, save_keys, extract_base64_key

def main():
    # Ask the user for the base name for the keys.
    key_base_name = input("Enter the base name for the keys (without extension): ").strip()

    # Ask whether the user wants to encrypt the private key using a passphrase.
    use_passphrase = input("Do you want to use a passphrase for the private key? (y/N): ").lower().strip()
    if use_passphrase in ['y', 'yes']:
        passphrase = getpass.getpass("Enter passphrase: ")
    else:
        passphrase = None

    # Generate RSA keys.
    private_key_bytes, public_key_bytes = generate_keys(passphrase)

    # Format keys so that newlines are represented as literal '\\n'.
    private_key_str = format_key(private_key_bytes)
    public_key_str = format_key(public_key_bytes)
    public_key_clean = extract_base64_key(public_key_bytes)

    # Save the keys to the "generated_keys" directory.
    save_keys(key_base_name, private_key_str,public_key_str, public_key_clean)

    print("\nKeys have been saved in the 'generated_keys' directory:")
    print(f" - {key_base_name}_private.pem")
    print(f" - {key_base_name}_public.pem")
    print(f" - {key_base_name}_public")

if __name__ == "__main__":
    main()
