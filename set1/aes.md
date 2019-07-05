# AES
### Electronic Code Block (ECB)
The most strightforward way to encrypt with AES.


### Steps
1. KeyExpansion
Round keys are derived from the cipher key using Rijndael's key schedule.
AES requires a seperate 128-bit round key block for each round plus one more.
2. Initial round key addition
  1. AddRoundKey
    Each byte of the state is combined with a block of the round key using
    bitwise xor.
3. 9, 11 or 13 rounds:
  1. SubBytes
    a non-linear substitution step where each byte is replaced with another 
    according to a lookup table.
  2. ShiftRows
    a transposition step where the last three rows of the state are shifted
    cyclically a certain number of steps.
  3. MixColumns
    a linear mixing operation which operates on the columns of the state,
    combining the four bytes in each column.
  4. AddRoundKey
4. Final Round (making 10, 12 or 14 rounds in total)
  1. SubBytes
  2. ShiftRows
  3. AddRoundKey

### SubBytes
In the SubBytes step, we replace each byte of the state with another byte
depending on the key. The substitutions are usually presented as a Look-up
table called the Rijndael S-box. The S-box consists of 256 byte substitutions
arranged in a 16x16 grid.

### Shift Rows
The shift rows step shifts the rows of the state to the left. The first row is not
shifted. The second row is shifted by 1 byte to the left. The third row is 
shifted by two bytes, and the final row is shifted by three bytes.

As bytes are shifted out on the left, they reappear on the right. This operation
is sometimes called rotation.

### Add Round Key
The Add Round Key in two places. It's used in the whitening step, and it's
also a step in the inner loop. This step involves adding the state and the
round key using a special type of arithmetic.

The state and round keys are added as Galois fields (sometimes called finite
fields). The arithmetic used is binary addition mod 2. This means every bit in the
input is added to the corresponding bit in the round key, and the result MOD 2
is stored in the state.

This is very convenient because Binary Addition MOD 2 happens to exactly match XOR.
