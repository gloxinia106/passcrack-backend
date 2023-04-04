from name_that_hash import runner

def find_name_that_hash(name):
    hash_names = runner.api_return_hashes_as_dict([name],{"popular_only": True})
    return hash_names.get(name)[0].get("name")

def crack_password(password, hash_name):
    pass