from base64 import b64decode

def main():
    byte_list = read_text('./6.txt')
    probable_keysizes = get_probable_keysizes(byte_list)
    blocks = keysize_blocks(byte_list, list(probable_keysizes)[0])
    transposed_blocks = transpose_blocks(blocks)
    key = [break_single_xor(block) for block in transposed_blocks]
    key = ''.join([chr(key_i) for key_i in key])
    decoded_message = decode(byte_list, key)
    print(decoded_message)


def read_text(filename):
    byte_list = []
    block = ''
    with open(filename) as f:
        while True:
            temp_char = f.read(1)
            if not temp_char:
                break
            if temp_char != '\n':
                block += temp_char
            if len(block) == 4:
                #print("B64: %s" % block)
                for byte in b64decode(block):
                    #print("hex: %s" % hex(byte))
                    byte_list.append(byte)
                block = ''
    return byte_list


def hamming_dist(a, b):
    char_length = len(a)
    count = 0
    for i in range(char_length):
        count += bin(a[i] ^ b[i]).count('1')
    return count


def decode(bytes, key):
    i = 0
    key = [ord(k_i) for k_i in key]
    key_len = len(key)
    decoded = []
    for byte in bytes:
        decoded.append(byte ^ key[i])
        i += 1
        i = 0 if (i >= key_len) else i
    return ''.join([chr(c_i) for c_i in decoded])


def keysize_blocks(byte_list, keysize):
    blocks = []
    block = []
    for byte in byte_list:
        block.append(byte)
        if (len(block) % keysize == 0):
            blocks.append(block)
            block = []
    if len(block) > 0:
        blocks.append(block)
    return blocks


def break_single_xor(blocks):
    max_metric = 0
    new_blocks = []
    for k in range(1, 256):
        for byte in blocks:
            new_blocks.append(byte ^ k)
        metric = calc_metric(new_blocks)
        new_blocks = []
        if metric > max_metric:
            max_metric = metric
            key = k
    return key


def calc_metric(blocks):
    metric = 0
    common = ['e', 't', 'a', 'o', 'i', 'n', 's',
              'h', 'r', 'd', 'l', 'u', ' ']
    common = [ord(c_i) for c_i in common]
    for byte in blocks:
        if byte in common:
            metric += 1
    return metric


def transpose_blocks(blocks):
    n_internal = len(blocks[0])
    transpose = []
    t_internal = []
    for i in range(n_internal):
        for b_i in blocks:
            if i < len(b_i):
                t_internal.append(b_i[i])
        transpose.append(t_internal)
        t_internal = []
    return transpose


def get_probable_keysizes(byte_list):
    hamm_dists = {}
    for keysize in range(2, 41):
        a_bytes = []
        b_bytes = []
        c_bytes = []
        d_bytes = []
        temp_dist = 0
        for i in range(keysize):
            a_bytes.append(byte_list[i])
            b_bytes.append(byte_list[keysize + i])
            c_bytes.append(byte_list[2 * keysize + i])
            d_bytes.append(byte_list[3 * keysize + i])
        temp_dist += hamming_dist(a_bytes, b_bytes) / keysize
        temp_dist += hamming_dist(a_bytes, c_bytes) / keysize
        temp_dist += hamming_dist(a_bytes, d_bytes) / keysize
        temp_dist += hamming_dist(b_bytes, c_bytes) / keysize
        temp_dist += hamming_dist(b_bytes, d_bytes) / keysize
        temp_dist += hamming_dist(c_bytes, d_bytes) / keysize
        temp_dist /= 6
        hamm_dists[keysize] = temp_dist
        # print("keysize: %i Distance: %f" % (keysize, current_dist))
    best_dists = {}
    for key in sorted(hamm_dists, key=hamm_dists.get)[:3]:
        best_dists[key] = hamm_dists[key]
    return best_dists


if __name__ == "__main__":
    main()
