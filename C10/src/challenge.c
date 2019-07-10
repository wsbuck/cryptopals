#include <stdio.h>
#include <string.h>
#include <stdint.h>

#include <aes.h>
#include <b64.h>

void read_key(char *input, unsigned char *key);
void read_file(char *filename, unsigned char *input);
void write_file(char *filename, unsigned char *input, size_t inlen);
int get_char_count(char *filename, int count_newline);


int main(int argc, char *argv[])
{
    if (argc < 5)
    {
        printf("Usage: ./challenge input-file output-file key IV\n");
        return 1;
    }

    char *input_filename = argv[1];
    char *output_filename = argv[2];
    unsigned char key[strlen(argv[3])];
    unsigned char IV[strlen(argv[4])];
    read_key(argv[3], key);
    reak_key(argv[4], IV);

    size_t inlen = get_char_count(input_filename, 1);
    size_t pad = (inlen % 16) > 0 ? 16 - (inlen % 16) : 0;
    size_t padded_len = inlen + pad;
    size_t encoded_len = b64_encoded_size(padded_len);

    unsigned char input[inlen];
    unsigned char input_padded[padded_len];
    unsigned char cipher_padded[padded_len];
    unsigned char b64_encoded[encoded_len];
    read_file(input_filename, input);
    pkcs7_pad(input, input_padded, inlen);
    aes_cbc_encrypt(input_padded, cipher_padded, key, IV, padded_len);
    b64_encode(cipher_padded, b64_encoded, padded_len);
    write_file(output_filename, b64_encoded, encoded_len);

}

void read_key(char *input, unsigned char *key)
{
    size_t key_len = strlen(input);
    for (int i = 0; i < key_len; i++)
    {
        key[i] = input[i];
    }
}

void read_file(char *filename, unsigned char *input)
{
    FILE *inptr = fopen(filename, "r");
    unsigned char c;
    int i = 0;

    if (inptr == NULL)
    {
        perror("Error in opening file");
        return;
    }

    do
    {
        c = fgetc(inptr);
        if (!feof(inptr))
        {
            input[i++] = c;
        }
        else
        {
            break;
        }
    } while (1);

    fclose(inptr);
}

void write_file(char *filename, unsigned char *input, size_t inlen)
{
    FILE *outptr = fopen(filename, "w");
    for (int i = 0; i < inlen; i++)
    {
        fputc(input[i], outptr);
    }
    fclose(outptr);
}

int get_char_count(char *filename, int count_newline)
{
    // if count_newline == 1 then count '\n' else don't
    FILE *inptr = fopen(filename, "r");
    int i = 0;
    char c;
    do
    {
        c = fgetc(inptr);
        if (c != '\n' || count_newline)
            i++;
        if (feof(inptr))
        {
            i--;
            break;
        }
    } while (1);
    fclose(inptr);
    return i;
}