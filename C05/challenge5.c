#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int get_bytes_count(FILE *inptr);
void dec_to_hex(char *hex, char byte);

int main(int argc, char *argv[])
{
    if (argc < 4) {
        printf("Usage: ./challenge5 input-file output-file key\n");
        return 1;
    }

    char *filename = argv[1];
    char *output_name = argv[2];
    char *key = argv[3];
    int i = 0;
    int num_bytes;
    char hex[2];

    FILE *inptr = fopen(filename, "r");
    if (inptr == NULL)
    {
        perror("Error in opening file");
        return -1;
    }

    num_bytes = get_bytes_count(inptr);
    // array to load to be encrypted file
    char byte_array[num_bytes];

    fseek(inptr, 0, SEEK_SET);
    do {
        byte_array[i] = fgetc(inptr);
        i++;
        if (feof(inptr)) {
            // byte_array[i] = '\0';
            break;
        }
    } while(1);
    fclose(inptr);
    FILE *outptr = fopen(output_name, "w");
    for (int i = 0; i < num_bytes; i++)
    {
        byte_array[i] = byte_array[i] ^ key[i % 3];
        dec_to_hex(hex, byte_array[i]);
        fputc(hex[0], outptr);
        fputc(hex[1], inptr);
    }
    fclose(outptr);
    printf("\n");
    return 0;
}

int get_bytes_count(FILE *inptr)
{
    char c;
    int i = 0;
    do
    {
        c = fgetc(inptr);
        i++;
        if (feof(inptr))
        {
            i--;
            break;
        }
    } while (1);
    return i;
}

void dec_to_hex(char *hex, char byte)
{
    char *hextable = "0123456789abcdef";
    int sixteens = byte / 16;
    int ones = byte % 16;
    hex[0] = hextable[sixteens];
    hex[1] = hextable[ones];
}

int power(int base, unsigned int exp)
{
    int i, result = 1;
    for (i = 0; i < exp; i++)
    {
        result *= base;
    }
    return result;
}