import sys, os
import binascii
import base64
import time

sys.path.append("..")

from crypto_tools.AES import EncryptionOracle, AES
from random import randint

def main():
    target_encoded = """
        Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
        aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
        dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
        YnkK
        """.strip()
    target = base64.b64decode(target_encoded)
    random = bytes([randint(0, 255) for _ in range(randint(1, 100))])

    random_n = find_n_rand(random, target)
    print(len(random))
    print("random length: {}".format(random_n))


    oracle = EncryptionOracle()
    rand_and_target = random + target
    print(len(rand_and_target))
    rand_and_target = oracle.pkcs7_pad(rand_and_target)
    print(len(rand_and_target))
    block_size = oracle.find_block_size(rand_and_target)
    print("block size: {}".format(block_size))

    my_string = "A" * len(rand_and_target)
    my_bytes = bytes(my_string, "ascii")

    print(len(rand_and_target) - random_n)


    # for block_num in range(0, len(rand_and_target) - random_n, block_size):
    block_num = random_n
    # print(len(rand_and_target))
    while block_num < len(rand_and_target) - 1:
        found = bytearray(block_size)

        for i in range(block_size):

            # print(block_num)
            unk_block = (
                bytes(my_bytes[:block_size - i - 1]) + 
                bytes(found[:i]) +
                bytes([rand_and_target[block_num + i]]))
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
        block_num += 16
        print(found.decode("ascii"), end="")
    block_num += block_size



def find_n_rand(random, target):
    oracle = EncryptionOracle(mode="ECB")
    last_round_blocks = {}
    static_blocks = []
    for i in range(32):
        os.system("clear")
        complete = random + bytes("A" * i, "ascii") + target
        enc_complete = oracle.encrypt(complete).hex()

        for j in range(0, len(enc_complete), 32):
            if i == 1:
                if enc_complete[j:j + 32] == last_round_blocks.get(j // 32):
                    static_blocks.append(j // 32)
            else:
                if enc_complete[j:j + 32] == last_round_blocks.get(j // 32):
                    if not (j // 32) in static_blocks:
                        n = i - 1
                        return (16 * len(static_blocks)) + (16 - n)
                        return i - 1
            last_round_blocks[j // 32] = enc_complete[j: j + 32]



if __name__ == "__main__":
    main()