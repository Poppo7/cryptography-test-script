# Cryptography Test Script

This script is an introduction to basic cryptography concepts, focusing on Base64 encoding and Fernet encryption.

## Base64
**Base64** is a way to encode binary data in a text-friendly format. It doesn't encrypt the data but rather converts bytes (which may include unprintable characters) into ASCII characters, making it safer to store or transmit in text-based environments.

When working with **Fernet** keys, you'll often see a **32-byte key** represented in Base64 form. Decoding that Base64-encoded string returns the raw 32-byte key used for actual encryption and decryption.

## Fernet
**Fernet** is a symmetric encryption method that uses a **32-byte key** (256 bits). This key is typically shown as a Base64 string for convenience, but under the hood it is raw binary data. Fernet provides both encryption and decryption, ensuring the authenticity and confidentiality of the data it protects.

## Bytes
A **byte** consists of 8 bits. For example, `10101010` is one byte (8 bits in binary). Therefore, **32 bytes** equals:

32 bytes * 8 bits/byte = 256 bits

| Bits (8) | Example   |
|----------|-----------|
| 8        | 10101010  |

## Installation

Run the following command to install the required Python package:

`pip install cryptography`


**Linux:**

`sudo apt-get update`

`sudo apt-get install build-essential libssl-dev libffi-dev python3-dev`

## Sources
https://en.wikipedia.org/wiki/Base64

https://cryptography.io/en/latest/fernet/

**Sample Fernet Key Generator:**
https://fernetkeygen.com/
