size_t b64_decoded_size(const unsigned char *in, size_t inlen);
int b64_isvalidchar(unsigned char c);
int b64_decode(const unsigned char *in, unsigned char *out, size_t inlen, size_t outlen);
void b64_encode(const unsigned char *in, unsigned char *out, size_t len);
size_t b64_encoded_size(size_t inlen);