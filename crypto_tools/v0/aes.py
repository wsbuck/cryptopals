import base64

class AES:
    def __init__(self):
        self.sbox = [
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

        self.rsbox = [
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

        self.rcon = [
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
        self.nbr_rounds = 10
        self.size = 16
        self.expanded_key_size = self.size * (self.nbr_rounds + 1)
        self.expanded_key = bytearray(self.expanded_key_size)
        self.block = bytearray(self.size)
        self.state = bytearray(self.size)
        self.round_key = bytearray(self.size)

    def __expand_key(self):
        current_size = 0
        rcon_iteration = 1
        t = bytearray(4)
        for i in range(self.size):
            self.expanded_key[i] = self.key[i]
        current_size += self.size

        while (current_size < self.expanded_key_size):
            for i in range(4):
                t[i] = self.expanded_key[(current_size - 4) + i]

            if current_size % self.size == 0:
                t = self.__core(t, rcon_iteration)
                rcon_iteration += 1

            for i in range(4):
                self.expanded_key[current_size] = (
                    self.expanded_key[current_size - self.size] ^ t[i]
                )
                current_size += 1
        

    def __core(self, word, iteration):
        word = self.__rotate(word)
        for i in range(4):
            word[i] = self.__get_sbox_value(word[i])

        word[0] = word[0] ^ self.__get_rcon_value(iteration)
        return word

    def __rotate(self, word):
        c = word[0]
        for i in range(3):
            word[i] = word[i + 1]
        word[3] = c
        return word

    def __get_sbox_value(self, num):
        return self.sbox[num]

    def __get_sbox_invert(self, num):
        return self.rsbox[num]

    def __get_rcon_value(self, num):
        return self.rcon[num]

    def __create_round_key(self, start):
        for i in range(4):
            for j in range(4):
                self.round_key[i + (j * 4)] = (
                    self.expanded_key[start * 16 + (i * 4) + j]
                )

    def __add_round_key(self):
        for i in range(self.size):
            self.state[i] ^= self.round_key[i]

    def __sub_bytes(self):
        for i in range(self.size):
            self.state[i] = self.__get_sbox_value(self.state[i])

    def __inv_sub_bytes(self):
        for i in range(self.size):
            self.state[i] = self.__get_sbox_invert(self.state[i])

    def __shift_row(self, nbr, start):
        for i in range(nbr):
            tmp = self.state[start]
            for j in range(3):
                self.state[start + j] = self.state[start + j + 1]
            self.state[start + 3] = tmp

    def __inv_shift_row(self, nbr, start):
        for i in range(nbr):
            tmp = self.state[start + 3]
            for j in range(3, 0, -1):
                self.state[start + j] = self.state[start + j - 1]
            self.state[start + 0] = tmp

    def __shift_rows(self):
        for i in range(4):
            self.__shift_row(i, i * 4)

    def __inv_shift_rows(self):
        for i in range(4):
            self.__inv_shift_row(i, i * 4)

    def __galois_multiplication(self, a, b):
        p = 0
        hi_bit_set = 0
        for counter in range(8):
            if ((b & 1) == 1):
                p ^= a
                p = p % 256
            hi_bit_set = (a & 0x80) % 256
            a <<= 1 % 256
            if (hi_bit_set == 0x80):
                a ^= 0x1b % 256
            b >>= 1 % 256
        return p % 256

    def __mix_column(self, column):
        cpy = bytearray(4)
        for i in range(4):
            cpy[i] = column[i]

        column[0] = (self.__galois_multiplication(cpy[0], 2) ^
                     self.__galois_multiplication(cpy[3], 1) ^
                     self.__galois_multiplication(cpy[2], 1) ^
                     self.__galois_multiplication(cpy[1], 3))
        column[1] = (self.__galois_multiplication(cpy[1], 2) ^
                     self.__galois_multiplication(cpy[0], 1) ^
                     self.__galois_multiplication(cpy[3], 1) ^
                     self.__galois_multiplication(cpy[2], 3)) 
        column[2] = (self.__galois_multiplication(cpy[2], 2) ^
                     self.__galois_multiplication(cpy[1], 1) ^
                     self.__galois_multiplication(cpy[0], 1) ^
                     self.__galois_multiplication(cpy[3], 3))
        column[3] = (self.__galois_multiplication(cpy[3], 2) ^
                     self.__galois_multiplication(cpy[2], 1) ^
                     self.__galois_multiplication(cpy[1], 1) ^
                     self.__galois_multiplication(cpy[0], 3))
        
        return column

    def __inv_mix_column(self, column):
        cpy = bytearray(4)
        for i in range(4):
            cpy[i] = column[i]
        
        column[0] = (self.__galois_multiplication(cpy[0], 14) ^
                     self.__galois_multiplication(cpy[3], 9) ^
                     self.__galois_multiplication(cpy[2], 13) ^
                     self.__galois_multiplication(cpy[1], 11))
        column[1] = (self.__galois_multiplication(cpy[1], 14) ^
                     self.__galois_multiplication(cpy[0], 9) ^
                     self.__galois_multiplication(cpy[3], 13) ^
                     self.__galois_multiplication(cpy[2], 11))
        column[2] = (self.__galois_multiplication(cpy[2], 14) ^
                     self.__galois_multiplication(cpy[1], 9) ^
                     self.__galois_multiplication(cpy[0], 13) ^
                     self.__galois_multiplication(cpy[3], 11))
        column[3] = (self.__galois_multiplication(cpy[3], 14) ^
                     self.__galois_multiplication(cpy[2], 9) ^
                     self.__galois_multiplication(cpy[1], 13) ^
                     self.__galois_multiplication(cpy[0], 11))

        return column


    def __mix_columns(self):
        column = bytearray(4)
        for i in range(4):
            for j in range(4):
                column[j] = self.state[(j * 4) + i]

            column = self.__mix_column(column)

            for j in range(4):
                self.state[(j * 4) + i] = column[j]

    def __inv_mix_columns(self):
        column = bytearray(4)
        for i in range(4):
            for j in range(4):
                column[j] = self.state[(j * 4) + i]
            
            self.__inv_mix_column(column)

            for j in range(4):
                self.state[(j * 4) + i] = column[j]

    def __aes_round(self):
        self.__sub_bytes()
        self.__shift_rows()
        self.__mix_columns()
        self.__add_round_key()

    def __aes_inv_round(self):
        self.__inv_shift_rows()
        self.__inv_sub_bytes()
        self.__add_round_key()
        self.__inv_mix_columns()

    def __aes_main(self):
        i = 0
        self.__create_round_key(0)
        self.__add_round_key()

        for i in range(1, self.nbr_rounds):
            self.__create_round_key(i)
            self.__aes_round()

        self.__create_round_key(self.nbr_rounds)
        self.__sub_bytes()
        self.__shift_rows()
        self.__add_round_key()


    def __aes_inv_main(self):
        i = 0
        self.__create_round_key(self.nbr_rounds)
        self.__add_round_key()

        for i in range(self.nbr_rounds - 1, 0, -1):
            self.__create_round_key(i)
            self.__aes_inv_round()

        self.__create_round_key(0)
        self.__inv_shift_rows()
        self.__inv_sub_bytes()
        self.__add_round_key()


    def __pkcs7_pad(self, inpt):
        input_len = len(inpt)
        pad_len = 0 if input_len % 16 == 0 else 16 - (input_len % 16)
        output_len = input_len + pad_len
        outpt = bytearray(output_len)

        for i in range(output_len):
            if i >= input_len:
                outpt[i] = pad_len
            else:
                outpt[i] = inpt[i]

        return outpt

    def __pdcs7_unpad(self, inpt):
        input_len = len(inpt)
        val_len = len(inpt)
        outpt = bytearray(input_len)

        if inpt[input_len - 1] < 16:
            pad_len = inpt[input_len - 1]
            if check_same(inpt, input_len - pad_len, input_len - 1):
                val_len = input_len - pad_len

        outpt = bytearray(val_len)
        
        for i in range(val_len):
            outpt[i] = inpt[i]

        return outpt


    def __check_same(self, inpt, start, end):
        check = inpt[start]
        for i in range(start, end + 1, 1):
            if inpt[i] != check:
                return False
        return True


    def decrypt(self, inpt: bytearray, key: bytes):
        self.key = key
        self.__expand_key()
        input_len = len(inpt)
        outpt = bytearray(input_len)
        counter = 0
        i = 0

        while i < input_len:
            self.block[i % self.size] = inpt[i]

            if (i + 1) % self.size == 0 and i > 0:
                for col in range(4):
                    for row in range(4):
                        c = self.block[(col * 4) + row]
                        self.state[col + (row * 4)] = c
                
                self.__aes_inv_main()

                for col in range(4):
                    for row in range(4):
                        c = self.state[col + (row * 4)]
                        outpt[counter] = c
                        counter += 1
            
            i += 1
        
        return outpt
        

    def encrypt(self, inpt: bytearray, key: bytes):
        self.key = key
        inpt = self.__pkcs7_pad(inpt)
        input_len = len(inpt)
        output = bytearray(input_len)
        counter = 0
        i = 0
        self.__expand_key()

        while (i < input_len):
            self.block[i % self.size] = inpt[i]

            if (i + 1) % self.size == 0 and i > 0:
                for col in range(4):
                    for row in range(4):
                        c = self.block[(col * 4) + row]
                        # print(hex(c), end=' ')
                        self.state[col + (row * 4)] = c
                
                self.__aes_main()

                for col in range(4):
                    for row in range(4):
                        c = self.state[col + (row * 4)]
                        # print(hex(c), end=' ')
                        output[counter] = c
                        counter += 1
            i += 1

        return output


def main():
    aes = AES()
    plaintext = bytearray("YELLOW SUBMARINE", "ascii")
    infile = "test.txt"
    outfile = "test_enc.txt"
    # with open(infile, "r") as f:
    #     plaintext = bytearray(f.read(), "ascii")

    key = bytearray("YELLOW SUBMARINE", "ascii")
    # key = bytearray(16)

    # cipher = aes.encrypt(plaintext, key)
    # cipher_encoded = base64.b64encode(cipher)

    # with open(outfile, "w") as f:
    #     f.write(cipher_encoded.decode())


    with open(outfile, "r") as f:
        ciphertext = base64.b64decode(f.read())


    plaintext = aes.decrypt(ciphertext, key)
    print(plaintext.decode())


    # for i in range(len(output)):
    #     if i % 16 == 0:
    #         print("\n")
    #     print(hex(output[i]), end =" ")
    
    # print("\n")


if __name__ == "__main__":
    main()
