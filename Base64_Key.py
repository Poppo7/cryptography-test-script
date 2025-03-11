import base64

key = b'YOUR-32-BYTE-SECRET-KEY'
encoded_key = base64.urlsafe_b64encode(key)
print(encoded_key)

# decoded_key = base64.urlsafe_b64decode(encoded_key)

# decode key when needed