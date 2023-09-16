import pickle
import hashlib
from utills import kor_to_eng


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


def makeDic(hash_name):
    hash_table = {}
    with open("dic/ko_dic.txt", "r", encoding="UTF8") as f:
        for line in f:
            text = line.strip()
            text = kor_to_eng(text)
            hashed_text = hash(text, hash_name)
            hash_table[hashed_text] = text
    return hash_table


for hash_name in ["SHA-1", "SHA-256", "SHA-512", "MD5"]:
    with open(f"dic/hash/ko_{hash_name}.pkl", 'wb') as f:
        dictionary = makeDic(hash_name)
        pickle.dump(dictionary, f)

# with open('dic/hash/en_dic.pkl', 'rb') as f:
#     loaded_dict = pickle.load(f)
#     print(loaded_dict["admin"]["SHA-1"])
