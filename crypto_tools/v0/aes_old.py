class AES:
    sbox = [
        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5,
        0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0,
        0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc,
        0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a,
        0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0,
        0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
        0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85,
        0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5,
        0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17,
        0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88,
        0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c,
        0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9,
        0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6,
        0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e,
        0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94,
        0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68,
        0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
    ]

    rsbox = [
        0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38,
        0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
        0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87,
        0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
        0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d,
        0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
        0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2,
        0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
        0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16,
        0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
        0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda,
        0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
        0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a,
        0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
        0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02,
        0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
        0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea,
        0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
        0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85,
        0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
        0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89,
        0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
        0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20,
        0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
        0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31,
        0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
        0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d,
        0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
        0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0,
        0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
        0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26,
        0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
    ]

    rcon = [
        0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
        0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a,
        0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a,
        0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39,
        0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25,
        0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a,
        0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08,
        0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8,
        0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6,
        0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef,
        0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61,
        0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc,
        0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01,
        0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b,
        0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e,
        0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3,
        0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4,
        0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94,
        0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8,
        0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20,
        0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d,
        0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35,
        0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91,
        0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f,
        0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d,
        0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04,
        0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c,
        0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63,
        0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa,
        0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd,
        0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66,
        0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb
    ]

    def __init__(mode: str = 'ECB'):
        yo = 'hello'

    def rotate(self, word: str):
        c = word[0]
        for i in range(3):
            word[i] = word[i + 1]
        word[3] = c

    def core(self, word, iteration):
        self.rotate(word)
        for i in range(4):
            word[i] = self.get_s_box_value(word[i])
        word[0] = word[0] ^ self.get_rcon_value(iteration)

    def expand_key(self, expanded_key, key):
        current_size = 0
        rcon_iteration = 1
        t = [0] * 4
        size = 16
        expanded_key_size = 176

        for i in range(size):
            expanded_key[i] = key[i]

        current_size += size

        while (current_size < expanded_key_size):
            for i in range(4):
                t[i] = expanded_key[(current_size - 4) + i]

            if (current_size % size == 0):
                self.core(t, rcon_iteration)
                rcon_iteration += 1

            for i in range(4):
                expanded_key[current_size] = (expanded_key[current_size - size]
                                              ^ t[i])
                current_size += 1

    def get_s_box_value(self, num):
        return self.sbox[num]

    def get_s_box_invert(self, num):
        return self.rsbox[num]

    def get_rcon_value(self, num):
        return self.rcon[num]

    def galois_multiplication(self, a, b):
        p = 0
        for counter in range(8):
            if ((b & 1) == 1):
                p ^= a
            hi_bit_set = (a & 0x80)
            a <<= 1
            if (hi_bit_set == 0x80):
                a ^= 0x1b
            b >>= 1
        return p

    def inv_sub_bytes(self, state):
        for i in range(16):
            state[i] = self.get_s_box_invert(state[i])

    def inv_shift_rows(self, state):
        for i in range(4):
            self.inv_shift_row(state + i * 4, i)

    def inv_shift_row(self, state, nbr):
        for i in range(nbr):
            tmp = state[3]
            for j in range(3, 0, -1):
                state[j] = state[j - 1]
            state[0] = tmp

    def inv_mix_columns(self, state):
        column = [0] * 4
        for i in range(4):
            for j in range(4):
                column[j] = state[(j * 4) + i]

            self.inv_mix_column(column)

            for j in range(4):
                state[(j * 4) + i] = column[j]

    def inv_mix_column(self, column):
        cpy = [0] * 4
        for i in range(4):
            cpy[i] = column[i]
        column[0] = (self.galois_multiplication(cpy[0], 14) ^
                     self.galois_multiplication(cpy[3], 9) ^
                     self.galois_multiplication(cpy[2], 13) ^
                     self.galois_multiplication(cpy[1], 11))

        column[1] = (self.galois_multiplication(cpy[1], 14) ^
                     self.galois_multiplication(cpy[0], 9) ^
                     self.galois_multiplication(cpy[3], 13) ^
                     self.galois_multiplication(cpy[2], 11))

        column[2] = (self.galois_multiplication(cpy[2], 14) ^
                     self.galois_multiplication(cpy[1], 9) ^
                     self.galois_multiplication(cpy[0], 13) ^
                     self.galois_multiplication(cpy[3], 11))

        column[3] = (self.galois_multiplication(cpy[3], 14) ^
                     self.galois_multiplication(cpy[2], 9) ^
                     self.galois_multiplication(cpy[1], 13) ^
                     self.galois_multiplication(cpy[0], 11))

    def aes_inv_round(self, state, round_key):
        self.inv_shift_rows(state)
        self.inv_sub_bytes(state)
        self.add_round_key(state, round_key)
        self.inv_mix_columns(state)

    def create_round_key(self, expanded_key, round_key):
        for i in range(4):
            for j in range(4):
                round_key[(i + (j * 4))] = expanded_key[(i * 4) + j]

    def add_round_key(self, state, round_key):
        for i in range(16):
            state[i] ^= round_key[i]

    def aes_inv_main(self, state, expanded_key, nbr_rounds):
        round_key = [0] * 16
        # self.create_round_key(expanded_key + 16 * nbr_rounds, round_key)
        round_key = expanded_key[nbr_rounds * 16: nbr_rounds * 16 + 1]
        self.add_round_key(state, round_key)

        for i in range(nbr_rounds, 0, -1):
            round_key = expanded_key[i * 16: i * 16 + 16]
            # self.create_round_key(expanded_key + 16 * i, round_key)
            self.aes_inv_round(state, round_key)

        self.create_round_key(expanded_key, round_key)
        self.inv_shift_rows(state)
        self.inv_sub_bytes(state)
        self.add_round_key(state, round_key)

    def shift_rows(self, state):
        for i in range(4):
            # self.shift_row(state + i * 4, i)
            self.shift_row(state[i * 4: i * 4 + 4])

    def shift_row(self, state, nbr):
        for i in range(nbr):
            tmp = state[0]
            for j in range(3):
                state[j] = state[j + 1]
            staet[3] = tmp

    def mix_columns(self, state):
        column = [0] * 4
        for i in range(4):
            for j in range(4):
                column[j] = state[(j * 4) + i]

            self.mix_column(column)

            for j in range(4):
                state[(j * 4) + i] = column[j]

    def mix_column(self, column):
        cpy = [0] * 4
        for i in range(4):
            cpy[i] = column[i]

        column[0] = (self.galois_multiplication(cpy[0], 2) ^
                     self.galois_multiplication(cpy[3], 1) ^
                     self.galois_multiplication(cpy[2], 1) ^
                     self.galois_multiplication(cpy[1], 3))

        column[1] = (self.galois_multiplication(cpy[1], 2) ^
                     self.galois_multiplication(cpy[0], 1) ^
                     self.galois_multiplication(cpy[3], 1) ^
                     self.galois_multiplication(cpy[2], 3))

        column[2] = (self.galois_multiplication(cpy[2], 2) ^
                     self.galois_multiplication(cpy[1], 1) ^
                     self.galois_multiplication(cpy[0], 1) ^
                     self.galois_multiplication(cpy[3], 3))

        column[3] = (self.galois_multiplication(cpy[3], 2) ^
                     self.galois_multiplication(cpy[2], 1) ^
                     self.galois_multiplication(cpy[1], 1) ^
                     self.galois_multiplication(cpy[0], 3))

    def sub_bytes(self, state):
        for i in range(16):
            state[i] = self.get_s_box_value(state[i])

    def aes_round(self, state, round_key):
        self.sub_bytes(state)
        self.shift_rows(state)
        self.mix_columns(state)
        self.add_round_key(state, round_key)

    def aes_main(self, state, expanded_key, nbr_rounds):
        round_key = [0] * 16
        self.create_round_key(expanded_key, round_key)
        self.add_round_key(state, round_key)

        for i in range(1, nbr_rounds, 1):
            # self.create_round_key(expanded_key + 16 * i, round_key)
            round_key = expanded_key[i * 16: (i * 16) + 16]
            self.aes_round(state, round_key)

        # self.create_round_key(expanded_key + 16 * nbr_rounds, round_key)
        round_key = expanded_key[nbr_rounds * 16: (nbr_rounds * 16) + 16]
        self.sub_bytes(state)
        self.shift_rows(state)
        self.add_round_key(state, round_key)

    def aes_encrypt(self, inpt, key):
        nbr_rounds = 10
        expanded_key_size = (16 * (nbr_rounds + 1))
        expanded_key = [0] * expanded_key_size
        block = [0] * 16
        state = [0] * 16
        counter = 0
        inlen = len(inpt)
        output = [0] * inlen

        self.expand_key(expanded_key, key)

        for i in range(0, inlen + 1, 1):
            if (i % 16 == 0 and i > 0):
                for x in range(4):
                    for y in range(4):
                        c = block[(x * 4) + y]
                        # print(c)
                        state[(x + (y * 4))] = c

                print(x + y * 4)
                print("state", state)
                print("expanded key", expanded_key)
                print("nbr_rounds", nbr_rounds)
                self.aes_main(state, expanded_key, nbr_rounds)

                for x in range(4):
                    for y in range(4):
                        c = state[x + (y * 4)]
                        output[counter] = c
                        counter += 1

            block[i % 16] = inpt[i]

        return str(output)

    def aes_decrypt(self, inpt, key):
        nbr_rounds = 10
        expanded_key_size = 16 * (nbr_rounds + 1)
        expanded_key = [0] * expanded_key_size
        block = [0] * 16
        state = [0] * 16
        counter = 0
        inlen = len(inpt)
        output = [0] * inlen

        self.expand_key(expanded_key, key)

        for i in range(0, inlen + 1, 1):
            if (i % 16 == 0 and i > 0):
                for x in range(4):
                    for y in range(4):
                        c = block[(x * 4) + y]
                        state[x + (y * 4)] = c

                self.aes_inv_main(state, expanded_key, nbr_rounds)

                for x in range(4):
                    for y in range(4):
                        c = state[x + (y * 4)]
                        output[counter] = c
                        counter += 1

            block[i % 16] = inpt[i]

        return str(output)

    def pkcs7_pad(self, inpt):
        inlen = len(inpt)
        pad_len = 0 if (inlen % 16 == 0) else (16 - (inlen % 16))
        outlen = inlen + pad_len
        output = [0] * outlen

        for i in range(outlen):
            if i >= inlen:
                output[i] = pad_len
            else:
                output[i] = inpt[i]

        return output

    def pkcs7_unpad(self, inpt):
        val_len = len(inpt)
        inlen = len(inpt)
        output = [0] * inlen

        if inpt[inlen - 1] < 16:
            pad_len = inpt[inlen - 1]
            if self.check_same(inpt, inlen - pad_len, inlen - 1):
                val_len = inlen - pad_len

        for i in range(inlen):
            if i < val_len:
                output[i] = inpt[i]
            else:
                output[i] = 0

    def check_same(self, inpt, start, end):
        check = inpt[start]
        for i in range(check, end + 1, 1):
            if inpt[i] != check:
                return False
        return True


def main():
    plaintext = [ord(c) for c in "YELLOW SUBMARINE"]
    key = plaintext.copy()

    aes = AES()
    output = aes.aes_encrypt(plaintext, key)
    print(output)


if __name__ == "__main__":
    main()
