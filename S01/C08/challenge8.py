#!../bin/python

def main():
    chunk_size = 16
    filename = '8.txt'
    ciphertexts = []

    with open(filename) as f:
        for line in f:
            ciphertexts.append(bytes.fromhex(line.strip()))
    
    # List to keep track of multiple occurences (patterns) in each ciphertext
    repetitions = []
    for ciphertext in ciphertexts:
        chunks = [
            ciphertext[i:i + chunk_size] 
            for i in range(0, len(ciphertexts), chunk_size)
        ]
        repetitions.append(len(chunks) - len(set(chunks)))
    
    print(repetitions)
    print(repetitions.index(max(repetitions)))

if __name__ == "__main__":
    main()