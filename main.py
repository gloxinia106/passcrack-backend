from flask import Flask, request
from crack import crack_password, make_dic, bruteforce_attack
from flask_cors import CORS
import json

app = Flask("passcrack_backend")
CORS(app, resources={
     r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)


@app.route("/api/text-crack", methods=["GET", 'POST'])
def crack_text():
    if (request.method == "POST"):
        passwords = []
        result_json = request.get_json()
        hashed_passwords = result_json["values"]
        mode = result_json["mode"]
        if (mode == "custom"):
            person = result_json["person"]
            make_dic(person["first_name"], person["last_name"], person["birth_year"],
                     person["birth_month"], person["birth_day"], person["phone_number"])
        for hashed_password in hashed_passwords:
            result = crack_password(hashed_password, mode)
            passwords.append(result)
        return {"ok": True, "passwords": passwords}
    else:
        return "404 not Found"


@app.route("/api/file-crack", methods=["GET", 'POST'])
def crack_file():
    if (request.method == "POST"):
        passwords = []
        mode = request.form.get("mode")
        file = request.files["file"]
        if (mode == "custom"):
            person = request.form.get("person")
            json_data = json.loads(person)
            make_dic(json_data["first_name"], json_data["last_name"], json_data["birth_year"],
                     json_data["birth_month"], json_data["birth_day"], json_data["phone_number"])
        for line in file:
            hashed_password = line.decode("utf-8").strip()
            result = crack_password(hashed_password, mode)
            passwords.append(result)
        return {"ok": True, "passwords": passwords}
    else:
        return "404 not Found"


@app.route("/api/bruteforce", methods=["GET", 'POST'])
def bruteforce():
    if (request.method == "POST"):
        passwords = []
        result_json = request.get_json()
        hashed_passwords = result_json["values"]
        for hashed_password in hashed_passwords:
            result = bruteforce_attack(hashed_password)
            passwords.append(result)
        return {"ok": True, "passwords": passwords}
    else:
        return "404 not Found"


app.run(debug=True)
