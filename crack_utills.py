import hashlib
from utills import kor_to_eng


def normal_crack(file, password, hash_name):
    for line in file:
        text = line.strip()
        text = kor_to_eng(text)
        if (hash_name == "SHA-1"):
            hashed_text = hashlib.sha1(text.encode()).hexdigest()
        elif (hash_name == "SHA-256"):
            hashed_text = hashlib.sha256(text.encode()).hexdigest()
        elif (hash_name == "SHA-512"):
            hashed_text = hashlib.sha512(text.encode()).hexdigest()
        elif (hash_name == "MD5"):
            hashed_text = hashlib.md5(text.encode()).hexdigest()
        else:
            hashed_text = None

        if (hashed_text == password):
            return {"ok": True, "password": text, "hash": hashed_text}

        return {"ok": False, "hash": password, "error": "password not found"}
