import json
import sys

sys.path.append("..")

from crypto_tools.AES import AES

def main():
    # profile = profile_for("          foo@bar.com     admin           ")
    e = AES(mode="ECB")
    key = e.generate_random_bytes()
    # email=XXXXXXXXXX XXXXXXXXXXXXXXXX XXXXXXXXXXXXXXXX XXXXXXXXXXXXXXXX
    # email=jerryseinf eld@gmail.com@gm ail.com&uid=10&r ole=user88888888
    # email=tempuser12 333333333@gmail. com&uid=10&role= usercccccccccccc
    # email=tempusr12@ gmail.com=uid=10 &role=admin55555

    # email=redballoon adminbbbbbbbbbbb @gmail.com&uid=1 &role=user666666
    # email=fuzz@buzz. com&uid=10&role= adminBBBBBBBBBBB
    # email=fuzz@buzz. com&uid=10&role= userCCCCCCCCCCCC
    email = (b"redballoonadmin" + bytes([11 for _ in range(11)])).decode()
    admin_block = e.encrypt(profile_for(email), key)[16:32]

    email = "fuzz@buzz.com"
    encrypted_email = e.encrypt(profile_for(email), key)
    encrypted_email = encrypted_email[:32] + admin_block

    d = AES(mode="ECB")
    decrypted_profile = d.decrypt(encrypted_email, key).decode()
    print(decrypted_profile)
    print(parse_kv(decrypted_profile))





def parse_kv(params):
    params = params.split("&")
    kv = {}
    for p in params:
        p_i = p.split("=")
        kv[p_i[0]] = p_i[1]
    return kv


def profile_for(email):
    email = email.replace('=', '').replace('&', '')
    data = {
        "email": email,
        "uid": 10,
        "role": "user"
    }
    encoded_data = ""
    for key in data:
        temp = "{}={}&".format(key, data[key])
        encoded_data += temp
    return encoded_data[:-1]


    


if __name__ == "__main__":
    main()