from crypto_tools.AES import AES

from Crypto.Cipher import AES as _AES

#plaintext = b"hello this is a test i want to see if this works doinker donker doinker doinker doinker doinker hello goodbyte"

plaintext = b"YELLOW SUBMARINE"

key = bytes(AES().generate_random_bytes())
iv = bytes(AES().generate_random_bytes())

print("iv: {}".format(iv))

a = AES("CBC", iv)
b = _AES.new(key, _AES.MODE_CBC, iv)

plaintext = bytes(a.pkcs7_pad(plaintext))

cipher_a = bytes(a.encrypt(plaintext, key))
plain_a = a.decrypt(cipher_a, key)

#cipher_b = b.encrypt(plaintext)
plain_b = b.decrypt(cipher_a)

#plain_b = a.decrypt(cipher_b, key)

print(plain_b)
