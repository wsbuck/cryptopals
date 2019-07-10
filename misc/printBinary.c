#include <stdio.h>

int power(int base, unsigned int exp);
int b64_to_int(char *b64);

int main(void)
{
    char *b64 = "TWFu";
    char encrypted[3];

    int dec = b64_to_int(b64);
    printf("%i\n", dec);
    printf("%X\n", dec);

    for (int i = 0; i < 3; i++)
    {
        encrypted[2 - i] = dec & 255;
        dec >>= 8;
    }

    printf("%s\n", encrypted);
}

int b64_to_int(char *b64)
{
    int temp;
    char c;
    int final = 0;
    for (int i = 0; i < 4; i++)
    {
        c = b64[i];
        if (c >= 'A' && c <= 'Z')
            temp = c - 65;
        else if (c >= 'a' && c <= 'z')
            temp = c - 97 + 26;
        else if (c == '+')
            temp = 62;
        else
            temp = 63;

        final += temp * (power(64, (3 - i)));
    }
    return final;
}

int power(int base, unsigned int exp)
{
    int i, result = 1;
    for (i = 0; i < exp; i++)
        result *= base;
    return result;
}