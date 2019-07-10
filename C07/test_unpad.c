#include <stdio.h>

void pkcs7_unpad(char *block, char *padded_block, size_t block_size);

int main(void)
{
    char block[17];
    char padded_block[17] = {
        'Y', 'E', 'L', 'L', 'O', 'W', ' ',
        'S', 'U', 'B', 0x06, 0x06, 0x06, 0x06, 0x06, 0x06 
    };

    char *okblock = "YELLOW SUBMARINE";

    pkcs7_unpad(block, okblock, 16);
    printf("%s\n", block);
    // printf("%s\n", padded_block);
}

void pkcs7_unpad(char *block, char *padded_block, size_t block_size)
{
    for (int i = block_size - 1; i >= 0; i--)
    {
        if (padded_block[i] > 16)
            break;
        else
        {
            for (int j = block_size - padded_block[i]; j < block_size; j++)
            {
                printf("%02x ", padded_block[i]);
                if (padded_block[j] != padded_block[i])
                    return;
            }
            for (int k = 0; k < block_size - padded_block[i]; k++)
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
    block = padded_block;
    for (int q = 0; q < block_size; q++)
    {
        printf("%c ", block[q]);
    }
}