from name_that_hash import runner
import hashlib
from itertools import product,permutations
from utills import hangul2roman

def make_dic(firt_name, last_name, birth_year, birth_month, birth_day, phone_number):
    full_name = firt_name + last_name
    names = [ hangul2roman(firt_name), hangul2roman(last_name), hangul2roman(full_name)]
    special_characters = ["!","@","#"]
    splited_phone = phone_number.split("-")
    others = [birth_year, birth_month, birth_day, splited_phone[1],splited_phone[2]]
    file = open("dic/custom_dic.txt","w")

    for combination in product(names,others):
        for permutation in permutations(combination):
            file.write("".join(permutation) + "\n")
    
    for combination in product(names,others,special_characters):
        for permutation in permutations(combination):
            file.write("".join(permutation) + "\n")

    file.close()

def crack_password(password, mode):
    hash_names = runner.api_return_hashes_as_dict([password],{"popular_only": True})
    hash_name = hash_names.get(password)[0].get("name")
    cracked_passwords = []

    if(mode == "english"):
        file = open("dic/en_dic.txt","r")
    elif(mode == "korean"):
        file = open("dic/en_dic.txt","r")
    elif(mode == "custom"):
        make_dic()
        file = open("dic/custom_dic.txt","r")
    
    for line in file:
        text = line.strip()
        if(hash_name == "SHA-1"):
            hashed_text = hashlib.sha1(text.encode()).hexdigest()
        elif(hash_name == "SHA-256"):
            hashed_text = hashlib.sha256(text.encode()).hexdigest()
        elif(hash_name == "SHA-512"):
            hashed_text = hashlib.sha512(text.encode()).hexdigest()
        elif(hash_name == "MD5"):
            hashed_text = hashlib.md5(text.encode()).hexdigest()
        
        if(hashed_text == password):
            cracked_passwords.append({ "password":text,"hash":hashed_text })
    
    if(cracked_passwords != []):
        return {"ok":True,"passwords":cracked_passwords}
    else:
        return {"ok":False,"error":"password not found"}



