#include <stdio.h>
#include <stdlib.h>
#include <aes.h>
#include <b64.h>

void pkcs7_unpad(unsigned char *block, unsigned char *padded_block, size_t block_size);


int main(int argc, char *argv[])
{
    if (argc < 4)
    {
        printf("Usage: ./challenge input-file output-file key\n");
        return 1;
    }

    char *input = argv[1];
    char *output = argv[2];
    char *key = argv[3];

    FILE *inptr = fopen(input, "r");
    if (inptr == NULL)
    {
        perror("Error in opening file");
        return -1;
    }

    int num_char = get_char_count(inptr);
    fseek(inptr, 0, SEEK_SET);

    char char_arr[num_char + 1];
    int i = 0;
    char c;

    do
    {
        c = fgetc(inptr);
        if (c != '\n' && c != -1)
        {
            // printf("%i\n", c);
            char_arr[i++] = c;
        }
        if (feof(inptr))
        {
            char_arr[i] = '\0';
            break;
        }
    } while (1);

    size_t outlen = b64_decoded_size(char_arr);
    unsigned char decoded_arr[outlen];

    b64_decode(char_arr, decoded_arr, outlen);

    unsigned char expandedKey[176];
    unsigned char state[16];
    unsigned char block[16];
    // unsigned char *unpadded_block = malloc(sizeof(char));
    unsigned char padded_block[16];
    unsigned char unpadded_block[16];
    unsigned char decrypted_arr[outlen + 1];

    expandKey(expandedKey, key);

    for (int i = 0; i < outlen + 1; i++)
    {
        if (i % 16 == 0 && i > 0)
        {
            for (int x = 0; x < 4; x++)
            {
                for (int y = 0; y < 4; y++)
                {
                    state[(x + (y * 4))] = block[(x * 4) + y];
                }
            }
            // printf("\n");
            aes_invMain(state, expandedKey, 10);
            // pkcs7_unpad(unpadded_block, state, 16);
            // printf("%s\n", state);
            for (int x = 0; x < 4; x++)
            {
                for (int y = 0; y < 4; y++)
                {
                    c = state[x + (y * 4)];
                    // printf("%c ", c);
                    // c = unpadded_block[x + (y * 4)];
                    // printf("%c \n", c);
                    // printf("%02x ", c);
                    padded_block[(x * 4) + y] = c;
                    // decrypted_arr[(i - 16) + ((x * 4) + y)] = c;
                }
            }
            pkcs7_unpad(unpadded_block, padded_block, 16);
            int j = 0;
            while (unpadded_block[j] != '\0' && j < 16)
            {
                decrypted_arr[(i - 16) + j] = unpadded_block[j];
                // printf("%02x ", unpadded_block[j]);
                j++;
            }
            // for (int j = 0; j < 16; j++)
            // {
            //     decrypted_arr[(i - 16) + j] = unpadded_block[j];
            // }
        }
        block[i % 16] = decoded_arr[i];
    }

    FILE *outptr = fopen(output, "w");
    for (int i = 0; i < outlen; i++)
    {
        fputc(decrypted_arr[i], outptr);
        // printf("%c", decrypted_arr[i]);
    }
    fclose(outptr);
    return 0;
}

void pkcs7_unpad(unsigned char *block, unsigned char *padded_block, size_t block_size)
{
    // for (int i = 0; i < 16; i++)
    // {
    //     printf("%02x ", padded_block[i]);
    // }
    // printf("\n");
    for (int i = block_size - 1; i >= 0; i--)
    {
        if (padded_block[i] > 16)
            break;
        else
        {
            for (int j = block_size - padded_block[i]; j < block_size; j++)
            {
                // printf("%02x vs %02x\n", padded_block[j], padded_block[i]);
                if (padded_block[j] != padded_block[i])
                    return;
            }
            for (int k = 0; k < block_size; k++)
            {
                if (k < block_size - padded_block[i])
                    block[k] = padded_block[k];
                else
                    block[k] = 0;
            }
            block[i] = '\0';
            return;
        }
    }
    for (int q = 0; q < block_size; q++)
    {
        block[q] = padded_block[q];
    }
}