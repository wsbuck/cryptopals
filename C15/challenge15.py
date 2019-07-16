import sys

sys.path.append("..")

from crypto_tools.AES import AES

def main():
    x = AES()

    valid = b"ICE ICE BABY\x04\x04\x04\x04"
    print(x.pkcs7_unpad(valid).decode())

    invalid = b"ICE ICE BABY\x05\x05\x05\x05"
    print(x.pkcs7_unpad(invalid).decode())

if __name__ == "__main__":
    main()