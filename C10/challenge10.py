import sys
import base64

sys.path.append("..")

from crypto_tools.AES import AES


def main():
    with open("10.txt") as f:
        cipher_encoded = bytearray(f.read(), "ascii")

    cipher = base64.b64decode(cipher_encoded)

    key = bytearray("YELLOW SUBMARINE", "ascii")
    iv = bytes(16)

    aes = AES(mode="CBC", iv=iv)
    plaintext = aes.decrypt(cipher, key)
    print(plaintext.decode())


if __name__ == "__main__":
    main()
