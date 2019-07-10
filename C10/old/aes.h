void expandKey(unsigned char *expandedKey, char *key);
unsigned char getSBoxValue(unsigned char num);
unsigned char getSBoxInvert(unsigned char num);
void rotate(unsigned char *word);
unsigned char getRconValue(unsigned char num);
void core(unsigned char *word, int iteration);
void invSubBytes(unsigned char *state);
void invShiftRows(unsigned char *state);
void invShiftRow(unsigned char *state, unsigned char nbr);
void invMixColumns(unsigned char *state);
void invMixColumn(unsigned char *column);
void aes_invRound(unsigned char *state, unsigned char *roundKey);
void createRoundKey(unsigned char *expandedKey, unsigned char *roundKey);
unsigned char galois_multiplication(unsigned char a, unsigned char b);
void addRoundKey(unsigned char *state, unsigned char *roundKey);
void aes_invMain(unsigned char *state, unsigned char *expandedKey, int nbrRounds);

void aes_main(unsigned char *state, unsigned char *expandedKey, int nbrRounds);
void aes_round(unsigned char *state, unsigned char *roundKey);
void mixColumn(unsigned char *column);
void mixColumns(unsigned char *state);
void shiftRow(unsigned char *state, unsigned char nbr);
void shiftRows(unsigned char *state);
void subBytes(unsigned char *state);
int aes_encrypt(unsigned char *input, unsigned char *output, char *key, size_t len);

void pkcs7_pad(char *block, char *padded_block, size_t block_size);
void pkcs7_unpad(char *block, char *padded_block, size_t block_size);