#include <stdio.h>
#include <string.h>

// #include <aes.h>

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Usage: ./challenge input-file\n");
        return 1;
    }

    char *input = argv[1];
    FILE *inptr = fopen(input, "r");
    if (inptr == NULL)
    {
        perror("Error in opening file");
        return -1;
    }

    char *line = NULL;
    size_t len;
    int i, f;
    int z = 0;
    int ret;
    int lines[250];

    while (getline(&line, &len, inptr) != -1)
    {
        z++;
        char buffer1[17];
        char buffer2[17];

        lines[z] = 0;
        buffer1[16] = '\0';
        buffer2[16] = '\0';

        // Compare blocks
        for (i = 0; i < len - 32; i += 16)
        {
            memcpy(buffer1, line + i, 16);

            for (f = 16; f + i < len; f += 16)
            {
                memcpy(buffer2, line + i + f, 16);
                if (!strcmp(buffer1, buffer2))
                {
                    lines[z] += 1;
                }
            }
        }
    }

    int num_reps = 0;
    int most_reps;

    for (i = 0; i < z; i++)
    {
        // printf("lines[%i] = %i\n", i, lines[i]);
        if (lines[i] > num_reps)
        {
            num_reps = lines[i];
            most_reps = i;
        }
    }

    printf("Line %i with %i block repititions\n", most_reps, num_reps);

    return 0;

}