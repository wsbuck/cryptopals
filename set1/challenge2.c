#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef unsigned char byte;

void concat_bits(bool *bit_arr, byte val, int start_i);
byte hex_to_dec(char hex_char);
int power(int base, unsigned int exp);
void convert_bin_to_hex(bool *bin_arr, char *hex_arr, int bin_len);

int main(int argc, char *argv[])
{
    char *hex_string1 = argv[1];
    char *hex_string2 = argv[2];

    int hex_len = strlen(hex_string1);
    int bin_len = hex_len * 4;

    if (hex_len != strlen(hex_string2)) {
        printf("buffers must be equal length!\n");
        return 1;
    }
    
    bool bin_arr1[bin_len];
    bool bin_arr2[bin_len];
    bool xor_bin_arr[bin_len];

    char xor_hex_arr[hex_len];

    byte val1;
    byte val2;

    for (int i = 0; i < hex_len; i++)
    {
        val1 = hex_to_dec(hex_string1[i]);
        val2 = hex_to_dec(hex_string2[i]);
        concat_bits(bin_arr1, val1, 4 * i);
        concat_bits(bin_arr2, val2, 4 * i);
    }

    for (int i = 0; i < bin_len; i++)
    {
        xor_bin_arr[i] = bin_arr1[i] ^ bin_arr2[i];
    }

    convert_bin_to_hex(xor_bin_arr, xor_hex_arr, bin_len);

    // printf("Binary 1: ");
    // for (int i = 0; i < bin_len; i++)
    // {
    //     printf("%i ", bin_arr1[i]);
    // }
    // printf("\n");
    // printf("Binary 2: ");
    // for (int i = 0; i < bin_len; i++)
    // {
    //     printf("%i ", bin_arr2[i]);
    // }
    // printf("\n");
    // printf("XOR:      ");
    // for (int i = 0; i < bin_len; i++)
    // {
    //     printf("%i ", xor_bin_arr[i]);
    // }
    // printf("\n");

    printf("Results: ");
    for (int i = 0; i < hex_len; i++)
    {
        printf("%c", xor_hex_arr[i]);
    }
    printf("\n");

}

void concat_bits(bool *bit_arr, byte val, int start_i)
{
    for (int j = 0; j < 4; j++)
    {
        bit_arr[start_i + j] = val / (power(2, (3 - j)));
        val = val % (power(2, (3 - j)));
    }
}

byte hex_to_dec(char hex_char)
{
    byte n = hex_char - 48;
    if (n > 9)
    {
        n -= 7;
    }
    return n;
}

void convert_bin_to_hex(bool *bin_arr, char *hex_arr, int bin_len)
{
    char *hex_table = "0123456789abcdef";
    
    int i = 0;
    int temp_val = 0;
    for (int i = 0; i < bin_len;)
    {
        for (int j = 0; j < 4; j++)
        {
            temp_val += (bin_arr[i + j] * power(2, 3 - j));
        }
        hex_arr[i / 4] = hex_table[temp_val];
        temp_val = 0;
        i += 4;
    }
}

int power(int base, unsigned int exp)
{
    int i, result = 1;
    for (i = 0; i < exp; i++)
        result *= base;
    return result;
}