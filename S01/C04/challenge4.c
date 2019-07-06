#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CHAR_LEN 61
#define BYTE_LEN 31

typedef unsigned char byte;

byte hex_to_dec(char hex_char);
int calc_freq_metric(char *arr);
void hex_to_byte(char *hex_string, char *byte_arr);
void copy_string(char *dest_str, const char *copy_str);
int decrypt_arr(const char *byte_arr, char *decrypted);

int main(int argc, char *argv[])
{
    char *filename = argv[1];
    FILE *inptr = fopen(filename, "r");
    char encrypted[CHAR_LEN];
    char byte_arr[BYTE_LEN];
    char temp_arr[BYTE_LEN];
    char decrypted[BYTE_LEN];
    int temp_metric = 0;
    int metric = 0;

    if (inptr == NULL)
    {
        printf("Could not open.\n");
        return 2;
    }

    while (fscanf(inptr, "%s", encrypted) == 1)
    {
        hex_to_byte(encrypted, byte_arr);
        temp_metric = decrypt_arr(byte_arr, temp_arr);
        if (temp_metric > metric)
        {
            metric = temp_metric;
            copy_string(decrypted, temp_arr);
            // printf("%s\n", decrypted);
        }
    }
    fclose(inptr);
    printf("%s\n", decrypted);
} 

byte hex_to_dec(char hex_char)
{
    byte n = hex_char - 48;
    if (n > 9)
    {
        n -= 39;
    }
    return n;
}

int calc_freq_metric(char *arr)
{
    // etaoin shrdlu
    int len = strlen(arr);
    int metric = 0;
    char c;
    for (int i = 0; i < len; i++) {
        c = arr[i];
        if (
            c == 'e' || c == 't' || c == 'a' || c == 'o' || c == 'i' ||
            c == 'n' || c == 's' || c == 'h' || c == 'r' || c == 'd' ||
            c == 'l' || c == 'u' || c == ' '
        )
        {
            metric += 1;
        }
    }
    return metric;
}

void hex_to_byte(char *hex_string, char *byte_arr)
{
    int i = 0;
    int j = 0;
    int temp;
    byte val = 0;
    for (int i = 0; hex_string[i]; i++)
    {
        temp = hex_to_dec(hex_string[i]);
        val += i % 2 == 0 ? temp * 16 : temp;
        if (i % 2 == 1)
        {
            byte_arr[j] = val;
            val = 0;
            j++;
        }
    }
}

void copy_string(char *dest_str, const char *copy_str)
{
    int length = strlen(copy_str);
    for (int i = 0; i < length; i++)
    {
        // printf("%i: %c\n", i, copy_str[i]);
        dest_str[i] = copy_str[i];
    }
}

int decrypt_arr(const char *byte_arr, char *decrypted)
{
    int temp_metric = 0;
    int current_metric = 0;
    char temp_arr[BYTE_LEN];
    for (int i = 0; i < 256; i++)
    {
        for (int j = 0; j < BYTE_LEN; j++)
        {
            temp_arr[j] = byte_arr[j] ^ i;
        }
        temp_metric = calc_freq_metric(temp_arr);
        if (temp_metric > current_metric)
        {
            current_metric = temp_metric;
            strcpy(decrypted, temp_arr);
        }
    }

    return current_metric;
}