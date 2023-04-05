from name_that_hash import runner
import hashlib

def make_dic():
    pass

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



