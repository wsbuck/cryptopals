size_t b64_decoded_size(const char *in);
int b64_isvalidchar(char c);
int b64_decode(const char *in, unsigned char *out, size_t outlen);
int get_char_count(FILE *inptr, int count_nl);
char *b64_encode(const unsigned char *in, size_t len);
size_t b64_encoded_size(size_t inlen);