# simple_hash_cracker

This Python script attempts to find the original password from a given hash by performing a dictionary attack using a user-provided wordlist.

## Features

- Supports multiple hashing algorithms: MD5, SHA1, SHA224, SHA3_224, SHA256, SHA3_256
- Automatically suggests possible algorithms based on the hash length
- Reads passwords from a dictionary file and compares their hashes with the target hash
