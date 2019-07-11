import sys

sys.path.append("..")

from crypto_tools.AES import EncryptionOracle, detect_mode

def main():
    oracle = EncryptionOracle()
    plaintext = """
    11111111111111111111111111111111111111111111111111111
    11111111111111111111111111111111111111111111111111111
    11111111111111111111111111111111111111111111111111111
    11111111111111111111111111111111111111111111111111111
    11111111111111111111111111111111111111111111111111111
    11111111111111111111111111111111111111111111111111111
    """
    inpt = bytearray(plaintext, "ascii")
    for i in range(1000):
        oracle = EncryptionOracle()
        oracle_mode = oracle.mode
        cipher = oracle.encrypt(inpt)
        detected_mode = detect_mode(cipher)
        assert(oracle_mode == detected_mode)

if __name__ == "__main__":
    main()