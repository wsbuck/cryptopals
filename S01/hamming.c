#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int hamming_dist(char *word1, char *word2);
int countBits(int n);

int main(void)
{
    // char *word1 = argv[1];
    // char *word2 = argv[2];
    char *word1 = "this is a test";
    char *word2 = "wokka wokka!!!";
    printf("Hamming Distance: %i\n", hamming_dist(word1, word2));

}

int hamming_dist(char *word1, char *word2)
{
    int dist = 0;
    int len = strlen(word1);
    for (int i = 0; i < len; i++)
    {
        dist += countBits(word1[i] ^ word2[i]);
    }
    return dist;
}

int countBits(int n)
{
    int count = 0;
    while (n)
    {
        count += n & 1;
        n >>= 1;
    }
    return count;
}