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
    if (argc < 4)
    {
        printf("Usage: ./decrypt input-file output-file key\n");
        return 1;
    }

    char *input_filename = argv[1];
    char *output_filename = argv[2];
    unsigned char key[strlen(argv[3])];
    read_key(argv[3], key);

    size_t inlen = get_char_count(input_filename, 1);
    unsigned char input[inlen];
    read_file(input_filename, input);

    size_t decoded_len = b64_decoded_size(input, inlen);
    unsigned char b64_decoded[decoded_len];
    b64_decode(input, b64_decoded, inlen, decoded_len);

    unsigned char plaintext_padded[decoded_len];
    unsigned char plaintext[decoded_len];

    aes_decrypt(b64_decoded, plaintext_padded, key, decoded_len);
    pkcs7_unpad(plaintext_padded, plaintext, decoded_len);
    write_file(output_filename, plaintext, decoded_len);


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