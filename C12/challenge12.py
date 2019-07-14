import sys
import binascii

sys.path.append("..")

from base64 import b64decode
from crypto_tools.AES import EncryptionOracle, pkcs7_pad

def main():
    unknown_encoded = """
        Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
        aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
        dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
        YnkK
        """.strip()
    unknown = pkcs7_pad(b64decode(unknown_encoded))
    unk_len = len(unknown)
    my_string = "A" * unk_len
    my_bytes = bytes(my_string, "ascii")

    oracle = EncryptionOracle(mode="ECB")
    block_size = oracle.find_block_size(unknown)
    mode = oracle.detect_mode(my_bytes)

    for block_num in range(0, unk_len, block_size):
        found = bytearray(block_size)

        for i in range(block_size):
            unk_block = (
                bytes(my_bytes[:block_size - i - 1]) + 
                bytes(found[:i]) +
                bytes([unknown[block_num + i]]))
            unk_encrypted = oracle.encrypt(unk_block)
            assert(len(unk_encrypted) == block_size)
            for j in range(1, 256):
                my_block = (
                    bytes(my_bytes[:block_size - i - 1]) + 
                    bytes(found[:i]) + 
                    bytes([j]))
                my_encrypted = oracle.encrypt(my_block)
                assert(len(my_encrypted) == block_size)
                if my_encrypted == unk_encrypted:
                    found[i] = j
                    # print(j)
                    # print(bytes([j]).decode("ascii"), end="")
                    break

        print(found.decode("ascii"), end="")


if __name__ == "__main__":
    main()