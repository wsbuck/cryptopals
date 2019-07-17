import sys

sys.path.append("..")

from crypto_tools.AES import EncryptionOracle

def main():
    oracle = EncryptionOracle(mode="CBC")
    first_block = bytearray("A" * oracle.size, "ascii")
    second_block = bytearray("AadminAtrueA", "ascii")
    input_string = first_block + second_block

    plaintext = prepend_and_append(input_string)
    # print(plaintext)
    ciphertext = oracle.encrypt(plaintext)

    # change first byte of first_block so we can change first byte of second_block
    ciphertext[32] = ciphertext[32] ^ (b"A"[0] ^ b";"[0])
    ciphertext[38] = ciphertext[38] ^ (b"A"[0] ^ b"="[0])
    ciphertext[43] = ciphertext[43] ^ (b"A"[0] ^ b";"[0])

    plaintext = oracle.decrypt(ciphertext)
    is_admin = b";admin=true;" in plaintext
    print(is_admin)

def prepend_and_append(input_string):
    prepend_string = b"comment1=cooking%20MCs;userdata="
    append_string = b";comment2=%20like%20a%20pound%20of%20bacon"
    input_string = input_string.replace(b';', b'').replace(b'=', b'')
    return prepend_string + input_string + append_string


def parse_kv(params):
    params = params.split(";")
    kv = {}
    for p in params:
        p_i = p.split("=")
        kv[p_i[0]] = p_i[1]
    return kv

def check_admin_status(kv_pair):
    return kv_pair.get("admin", False)

def xor(b1, b2):
    b = bytearray(len(b1))
    for i in range(len(b1)):
        b[i] = b1[i] ^ b2[i]
    return b

if __name__ == "__main__":
    main()