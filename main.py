from flask import Flask,request
from crack import crack_password

app = Flask("passcrack_backend")

@app.route("/api/text-crack", methods=["GET",'POST'])
def crack_text():
    if(request.method == "POST"):
        passwords = []
        result = request.get_json()
        hashed_passwords = result["values"]
        mode = result["mode"]
        for hashed_password in hashed_passwords:
            password = crack_password(hashed_password,mode)
            passwords.append(password)
        return {"ok":True,"passwords":passwords}
    else:
        return "GET"

@app.route("/api/file-crack", methods=["GET",'POST'])
def crack_file():
    if(request.method == "POST"):
        result = request.form.get("mode")
        file2 = request.files["file2"]
        file = request.files["file"]
        print(result)
        for line in file:
            print(line.decode("utf-8").strip())
        return "zczczczxc"
    else:
        return "GET"

app.run(debug=True)
