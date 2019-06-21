#include <stdio.h>
#include <string.h>

typedef unsigned char byte;

byte hex_to_dec(char hex_char);
int calc_freq_metric(char *arr);
void hex_to_byte(char *hex_string, char *byte_arr);

int main(int argc, char *argv[])
{
    char *hex_string = argv[1];
    int hex_len = strlen(hex_string);
    int byte_len = hex_len / 2;
    int current_metric = 0;
    int new_metric = 0;

    char char_arr_encrypted[byte_len];
    char char_arr_temp[byte_len];
    char char_arr_decrypted[byte_len];

    hex_to_byte(hex_string, char_arr_encrypted);
    for (int i = 0; i < 256; i++)
    {
        for (int j = 0; j < byte_len; j++)
        {
            char_arr_temp[j] = char_arr_encrypted[j] ^ i;
        }
        new_metric = calc_freq_metric(char_arr_temp);
        if (new_metric > current_metric)
        {
            current_metric = new_metric;
            strcpy(char_arr_decrypted, char_arr_temp);
        }
    }
    printf("Result: %s\n", char_arr_decrypted);
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
            c == 'l' || c == 'u'
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