from name_that_hash import runner
import hashlib
from itertools import product, permutations
from utills import kor_to_eng
import pickle
from passlib.hash import sha256_crypt, sha1_crypt, sha512_crypt, md5_crypt


def hash(password, hash_name):
    if (hash_name == "SHA-1"):
        hashed_text = hashlib.sha1(password.encode()).hexdigest()
    elif (hash_name == "SHA-256"):
        hashed_text = hashlib.sha256(password.encode()).hexdigest()
    elif (hash_name == "SHA-512"):
        hashed_text = hashlib.sha512(password.encode()).hexdigest()
    elif (hash_name == "MD5"):
        hashed_text = hashlib.md5(password.encode()).hexdigest()
    return hashed_text


def make_dic(firt_name, last_name, birth_year, birth_month, birth_day, phone_number):
    full_name = firt_name + last_name
    names = [kor_to_eng(firt_name), kor_to_eng(
        last_name), kor_to_eng(full_name)]
    special_characters = ["!", "@", "#"]
    splited_phone = phone_number.split("-")
    others = [birth_year, birth_month, birth_day,
              splited_phone[1], splited_phone[2]]
    file = open("dic/custom_dic.txt", "w")
    for combination in product(names, others):
        for permutation in permutations(combination):
            file.write("".join(permutation) + "\n")

    for combination in product(names, others, special_characters):
        for permutation in permutations(combination):
            file.write("".join(permutation) + "\n")

    file.close()
    for hash_name in ["SHA-1", "SHA-256", "SHA-512", "MD5"]:
        with open(f"dic/hash/custom_{hash_name}.pkl", 'wb') as f:
            hash_table = {}
            for combination in product(names, others):
                for permutation in permutations(combination):
                    hashed_text = hash("".join(permutation), hash_name)
                    hash_table[hashed_text] = "".join(permutation)

            for combination in product(names, others, special_characters):
                for permutation in permutations(combination):
                    hashed_text = hash("".join(permutation), hash_name)
                    hash_table[hashed_text] = "".join(permutation)
            pickle.dump(hash_table, f)


def crack_salt(password, hash_name, salt, mode):
    if (mode == "english"):
        file = open(f"dic/en_dic.txt", "r", encoding="UTF8")
    elif (mode == "korean"):
        file = open(f"dic/ko_dic.txt", "r", encoding="UTF8")
    elif (mode == "custom"):
        file = open("dic/custom_dic.txt", "r", encoding="UTF8")

    result = {}

    for line in file:
        text = line.strip()
        text = kor_to_eng(text)
        if (hash_name == "SHA-1"):
            hashed_text = sha1_crypt.using(rounds=5000, salt=salt).hash(text)
        elif (hash_name == "SHA-256"):
            hashed_text = sha256_crypt.using(rounds=5000, salt=salt).hash(text)
        elif (hash_name == "SHA-512"):
            hashed_text = sha512_crypt.using(rounds=5000, salt=salt).hash(text)
        elif (hash_name == "MD5"):
            hashed_text = md5_crypt.using(rounds=5000, salt=salt).hash(text)
        else:
            hashed_text = None

        if (hashed_text == password):
            result = {"ok": True, "password": text, "hash": hashed_text}
            break
    if (result != {}):
        return result
    else:
        return {"ok": False, "hash": password, "error": "password not found"}


def crack_password(password, mode):
    hash_names = runner.api_return_hashes_as_dict(
        [password], {"popular_only": True})
    if (hash_names.get(password)):
        hash_name = hash_names.get(password)[0].get("name")
    else:
        hash_name = "MD5"

    if (mode == "english"):
        file = open(f"dic/hash/en_{hash_name}.pkl", "rb")
    elif (mode == "korean"):
        file = open(f"dic/hash/ko_{hash_name}.pkl", "rb")
    elif (mode == "custom"):
        file = open(f"dic/hash/custom_{hash_name}.pkl", "rb")

    loaded_dict = pickle.load(file)
    try:
        crached_text = loaded_dict[password]
        return {"ok": True, "password": crached_text, "hash": password}
    except:
        return {"ok": False, "hash": password, "error": "password not found"}


def bruteforce_attack(password):
    chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
    hash_names = runner.api_return_hashes_as_dict(
        [password], {"popular_only": True})
    hash_name = hash_names.get(password)[0].get("name")
    attempts = 0
    for i in range(1, 20):
        for letter in product(chars, repeat=i):
            attempts += 1
            letter = ''.join(letter)
            if (hash_name == "SHA-1"):
                hashed_text = hashlib.sha1(letter.encode()).hexdigest()
            elif (hash_name == "SHA-256"):
                hashed_text = hashlib.sha256(letter.encode()).hexdigest()
            elif (hash_name == "SHA-512"):
                hashed_text = hashlib.sha512(letter.encode()).hexdigest()
            elif (hash_name == "MD5"):
                hashed_text = hashlib.md5(letter.encode()).hexdigest()
            if hashed_text == password:
                return {"ok": True, "password": letter, "hash": password}
