#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define KEYSIZE_MIN 2
#define KEYSIZE_MAX 40

float hamming_dist(char *word1, char *word2, int len);
int countBits(int n);
int get_char_count(FILE *inptr);
int b64_to_int(const char *b64);
int power(int base, unsigned int exp);
void b64arr_to_bytearr(char *b64, char *byte_arr, int b64_len);

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Usage: ./challenge6 input-file\n");
        return -1;
    }

    char *filename = argv[1];
    int num_char;

    FILE *inptr = fopen(filename, "r");
    if (inptr == NULL)
    {
        perror("Error in opening file");
        return -1;
    }
    char c;
    num_char = get_char_count(inptr);
    // printf("get_char_count = %i ", num_char);

    char b64_array[num_char];
    char byte_array[num_char / 4 * 3];

    fseek(inptr, 0, SEEK_SET);
    int i = 0;
    int temp;
    do
    {
        c = fgetc(inptr);
        if (c != '\n')
        {
            b64_array[i] = c;
            i++;
        }
        if (feof(inptr))
        {
            break;
        }
    } while (1);
    fclose(inptr);
    b64arr_to_bytearr(b64_array, byte_array, num_char);

    float hamming_dists[KEYSIZE_MAX - KEYSIZE_MIN + 1];
    float min_dist = 2000.0;
    int optimal_keysize;
    float ham_dist;

    for (int KEYSIZE = KEYSIZE_MIN; KEYSIZE <= KEYSIZE_MAX; KEYSIZE++)
    {
        // printf("KEYSIZE: %i\n", KEYSIZE);
        char first_bytes[KEYSIZE + 1];
        char second_bytes[KEYSIZE + 1];
        for (int i = 0; i < KEYSIZE; i++)
        {
            // printf("first: %i\n", byte_array[i]);
            first_bytes[i] = byte_array[i];
        }
        first_bytes[KEYSIZE] = '\0';
        for (int j = KEYSIZE; j < (2 * KEYSIZE); j++)
        {
            // printf("second: %i\n", byte_array[j]);
            second_bytes[j - KEYSIZE] = byte_array[j];
        }
        second_bytes[KEYSIZE] = '\0';
        ham_dist = hamming_dist(first_bytes, second_bytes, KEYSIZE) / KEYSIZE;
        printf("keysize: %i dist: %f\n", KEYSIZE, ham_dist);
        // hamming_dists[KEYSIZE - KEYSIZE_MIN] = ham_dist;
        // max_dist = (ham_dist > max_dist) ? ham_dist : max_dist;
        if (ham_dist < min_dist)
        {
            min_dist = ham_dist;
            optimal_keysize = KEYSIZE;
        }
    }
    printf("\nFINAL: keysize: %i min dist: %.6f\n", optimal_keysize, min_dist);
    return 0;

    // printf("%c %c %c %c\n", b64_array[0], b64_array[1],
    //  b64_array[2], b64_array[3]);
    // printf("%i %i %i\n", byte_array[0], byte_array[1], byte_array[2]);
}

void b64arr_to_bytearr(char *b64, char *byte_arr, int b64_len)
{
    char c[5];
    c[4] = '\0';
    int num_chunks = b64_len / 4;
    int num_bytes = b64_len / 4 * 3;
    int threebyte_array[num_chunks];
    int i = 0;
    while(b64[i])
    {
        c[i % 4] = b64[i];
        if (i % 4 == 3)
        {
            // printf("B64: %s\n", c);
            threebyte_array[(i / 4)] = b64_to_int(c);
        }
        i++;
    }
    for (int i = 0; i < num_bytes; i+= 3)
    {
        for (int j = 2; j >= 0; j--)
        {
            byte_arr[i + j] = threebyte_array[(i + j) / 3] & 255;
            threebyte_array[(i + j) / 3] >>= 8;
        }
    }
}

int get_char_count(FILE *inptr)
{
    char c;
    int i = 0;
    do
    {
        c = fgetc(inptr);
        if (c != '\n')
        {
            i++;
        }
        if (feof(inptr))
        {
            i--;
            break;
        }
    } while (1);
    return i;
}

float hamming_dist(char *word1, char *word2, int len)
{
    float dist = 0;
    // printf("len: %i\n", len);
    for (int i = 0; i < len; i++)
    {
        // printf("%i %i\n", word1[i], word2[i]);
        dist += countBits(word1[i] ^ word2[i]);
    }
    return dist;
}

int countBits(int n)
{
    int count = 0;
    // printf("%i\n", n);
    while (n)
    {
        // printf("%i\n", n);
        count += n & 1;
        n >>= 1;
    }
    return count;
}

int b64_to_int(const char *b64)
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
        else if (c == '/')
            temp = 63;
        else
            temp = 0;

        final += temp * (power(64, (3 - i)));
    }
    // printf("%s\n", b64);
    // printf("%i\n", final);
    // printf("final: %i\n", final);
    // if (final < 0)
    // {
    //     printf("%s %i\n", b64, final);
    // }
    return final;
}

int power(int base, unsigned int exp)
{
    int i, result = 1;
    for (i = 0; i < exp; i++)
        result *= base;
    return result;
}