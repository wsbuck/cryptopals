#!../bin/python

import base64
import sys

from Crypto.Cipher import AES

def main():
    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        print("Usage: challenge7.py ciphertext key")
    filename = sys.argv[1]
    key = bytes(sys.argv[2], 'ascii')

    with open(filename) as f:
        ciphertext = base64.b64decode(f.read())
    
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    print(plaintext)
    return 0

if __name__ == "__main__":
    main()