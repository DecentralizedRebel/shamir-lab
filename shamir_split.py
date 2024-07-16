#!/usr/bin/env python3
# An example where 3 people share a secret.
# Two shares are sufficient to reassemble it.

from Crypto.Hash import SHA256
from Cryptodome.Protocol.SecretSharing import Shamir

# Input string
words = "This is a secret message with 24 words that needs to be protected"

def encode_to_16_bytes(words: str) -> bytes:
    if not isinstance(words, str):
        raise TypeError("Input must be a string")
    hash_obj = SHA256.new()

    # Encode input string to bytes and update hash object
    hash_obj.update(words.encode('utf-8'))

    # Get the hash digest
    hash_digest = hash_obj.digest()

    # Truncate the hash to 16 bytes
    truncated_digest = hash_digest[:16]

    return truncated_digest


encoded_words = encode_to_16_bytes(words)

# Split words into 3 shares, where 2 is needed to recombine the secret
shares = Shamir.split(2, 3, encoded_words)

# Determine the number of shares
num_shares = len(shares)

# Persist each share to a textfile
for i, share in enumerate(shares, start=1):
    filename = f"share{i}.txt"
    with open(filename, 'w') as file:
        file.write(f"{share[0]},{share[1].hex()}") # Convert bytes to hex for writing
        print(f"wrote {filename}.")
