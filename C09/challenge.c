#include <stdio.h>
#include <string.h>

void pkcs7_pad(char *block, char *padded_block, size_t block_size);

int main(void)
{
    size_t block_size = 20;
    char *block = "YELLOW SUBMARINE";
    char padded_block[block_size];

    pkcs7_pad(block, padded_block, block_size);

    for (int i = 0; i < block_size; i++)
    {
        printf("%i ", padded_block[i]);
    }
    printf("\n");

}

void pkcs7_pad(char *block, char *padded_block, size_t block_size)
{

    size_t block_len = strlen(block);
    // size_t padded_len = strlen(padded_block);
    size_t n_padded = block_size - block_len;

    for (int i = 0; i < block_size; i++)
    {
        if (i >= block_len)
            padded_block[i] = n_padded;
        else
            padded_block[i] = block[i];
    }
    return;
}