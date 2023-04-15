from flask import Flask,request
from crack import crack_password, make_dic, bruteforce_attack
import json

app = Flask("passcrack_backend")

@app.route("/api/text-crack", methods=["GET",'POST'])
def crack_text():
    if(request.method == "POST"):
        passwords = []
        result = request.get_json()
        hashed_passwords = result["values"]
        mode = result["mode"]
        person = result["person"]
        if(mode == "custom"):
            make_dic(person["first_name"],person["last_name"],person["birth_year"],person["birth_month"],person["birth_day"],person["phone_number"])
        for hashed_password in hashed_passwords:
            result_password = crack_password(hashed_password,mode,person)
            if(result_password["ok"]):
                passwords.append(result_password["password"])
            else:
                passwords.append(result_password["error"])
        return {"ok":True,"passwords":passwords}
    else:
        return "GET"

@app.route("/api/file-crack", methods=["GET",'POST'])
def crack_file():
    if(request.method == "POST"):
        passwords = []
        mode = request.form.get("mode")
        person = request.form.get("person")
        file = request.files["file"]
        if(mode == "custom"):
            json_data = json.loads(person)
            make_dic(json_data["first_name"],json_data["last_name"],json_data["birth_year"],json_data["birth_month"],json_data["birth_day"],json_data["phone_number"])
        for line in file:
            hashed_password = line.decode("utf-8").strip()
            password = crack_password(hashed_password,mode)
            passwords.append(password)
        return {"ok":True,"passwords":passwords}
    else:
        return "GET"

@app.route("/api/bruteforce", methods=["GET",'POST'])
def bruteforce():
    if(request.method == "POST"):
        passwords = []
        result = request.get_json()
        hashed_passwords = result["values"]
        for hashed_password in hashed_passwords:
            result_password = bruteforce_attack(hashed_password)
            if(result_password["ok"]):
                passwords.append(result_password["password"])
            else:
                passwords.append(result_password["error"])
        return {"ok":True,"passwords":passwords}
    else:
        return "GET"

app.run(debug=True)
