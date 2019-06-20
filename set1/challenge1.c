#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef unsigned char byte;

byte hex_to_dec(char hex_char);
int power(int base, unsigned int exp);
void concat_bits(bool *bit_arr, byte val, int start_i);
void convert_to_b64(bool *bit_arr, byte *b64_arr, int bit_len);

int main(int argc, char *argv[])
{
    char *hex_string = argv[1];
    int hex_len = strlen(hex_string);
    int bit_len = hex_len * 4;
    int b64_len = bit_len / 6;
    if (bit_len % 6 > 0)
    {
        b64_len += 1;
    }

    byte hex_arr[hex_len];
    bool bit_arr[bit_len];
    byte b64_arr[b64_len];

    for (int i = 0; i < hex_len; i++)
    {
        byte val = hex_to_dec(hex_string[i]);
        hex_arr[i] = val;
        concat_bits(bit_arr, val, 4 * i);
    }

    convert_to_b64(bit_arr, b64_arr, bit_len);

    // printf("Binary: ");
    // for (int i = 0; i < bit_len; i++)
    // {
    //     printf("%i ", bit_arr[i]);
    // }
    // printf("\n");
    printf("B64: ");
    for (int i = 0; i < b64_len; i++)
    {
        printf("%c", b64_arr[i]);
    }
    printf("\n");
}

byte hex_to_dec(char hex_char)
{
    // char *hex_table = "0123456789ABCDEF";
    byte n = hex_char - 48;
    if (n > 9)
    {
        n -= 7;
    }
    return n;
}

int power(int base, unsigned int exp)
{
    int i, result = 1;
    for (i = 0; i < exp; i++)
        result *= base;
    return result;
}

void concat_bits(bool *bit_arr, byte val, int start_i)
{
    for (int j = 0; j < 4; j++)
    {
        bit_arr[start_i + j] = val / (power(2, (3 - j)));
        val = val % (power(2, (3 - j)));
    }
}

void convert_to_b64(bool *bit_arr, byte *b64_arr, int bit_len)
{
    char *b64_table =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk"
        "lmnopqrstuvwxyz0123456789+/";
    
    int i = 0;
    int temp_val = 0;
    for (int i = 0; i < bit_len;)
    {
        for (int j = 0; j < 6; j++)
        {
            temp_val += (bit_arr[i + j] * power(2, 5 - j));
        }
        b64_arr[i / 6] = b64_table[temp_val];
        temp_val = 0;
        i += 6;
    }
}