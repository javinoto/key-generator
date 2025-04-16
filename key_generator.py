"""
key_generator.py

This module contains utility functions for generating RSA keys, formatting them,
and saving the keys to files in a designated directory.
"""

import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def generate_keys(passphrase: str = None):
    """
    Generate an RSA key pair (2048 bits).

    :param passphrase: Optional passphrase to encrypt the private key.
    :return: Tuple containing the private key bytes and public key bytes.
    """
    # Generate the private key using RSA with a key size of 2048 bits and public exponent 65537.
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    # Choose the encryption algorithm based on whether a passphrase was provided.
    encryption_algorithm = (
        serialization.BestAvailableEncryption(passphrase.encode())
        if passphrase
        else serialization.NoEncryption()
    )

    # Serialize the private key in PEM format using PKCS#8.
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=encryption_algorithm
    )

    # Serialize the public key in PEM format (SubjectPublicKeyInfo).
    public_key = private_key.public_key()
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_key_bytes, public_key_bytes


def format_key(key_bytes: bytes) -> str:
    """
    Convert key bytes to a string and replace actual newline characters with the literal '\\n'.

    This formatting is particularly useful for storage systems like AWS Secrets Manager.

    :param key_bytes: The key in bytes.
    :return: The formatted key string.
    """
    key_str = key_bytes.decode("utf-8")
    return key_str.replace("\n", "\\n")


def extract_base64_key(public_key_bytes: bytes) -> str:
    """
    Extract the Base64 encoded part of the public key from a PEM-formatted key.

    This function removes the header, footer, and any newline characters,
    returning a continuous Base64 string.

    :param public_key_bytes: The PEM-formatted public key bytes.
    :return: A clean, continuous Base64 string representing the public key.
    """
    public_key_str = public_key_bytes.decode("utf-8")
    lines = public_key_str.splitlines()
    base64_lines = [line for line in lines if not (line.startswith("-----BEGIN") or line.startswith("-----END"))]
    return "".join(base64_lines)


def save_keys(key_base_name: str, private_key: str, public_key: str, public_key_clean: str, directory: str = "generated_keys"):
    """
    Save the private and public keys to separate files within a specified directory.

    The files will be named as <key_base_name>_private.pem and <key_base_name>_public.pem.

    :param key_base_name: The base name to use for the key files.
    :param private_key: The formatted private key as a string.
    :param public_key: The formatted public key as a string.
    :param public_key_clean: The Base64 public key as a string.
    :param directory: The directory where the keys will be saved (default: generated_keys).
    """
    # Create the directory if it does not exist.
    if not os.path.exists(directory):
        os.makedirs(directory)

    private_key_filename = os.path.join(directory, f"{key_base_name}_private.pem")
    public_key_filename = os.path.join(directory, f"{key_base_name}_public.pem")
    public_key_clean_filename = os.path.join(directory, f"{key_base_name}_public")

    with open(private_key_filename, "w") as priv_file:
        priv_file.write(private_key)

    with open(public_key_filename, "w") as pub_file:
        pub_file.write(public_key)

    with open(public_key_clean_filename, "w") as pub_file:
        pub_file.write(public_key_clean)
