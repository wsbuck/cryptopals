#include <stdio.h>
#include <aes.h>
#include <b64.h>

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
            // printf("%s\n", state);
            for (int x = 0; x < 4; x++)
            {
                for (int y = 0; y < 4; y++)
                {
                    decrypted_arr[(i - 16) + ((x * 4) + y)] = state[x + (y * 4)];
                }
            }
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