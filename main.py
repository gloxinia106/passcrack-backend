from flask import Flask,request

app = Flask("passcrack_backend")

@app.route("/api/text-crack", methods=["GET",'POST'])
def crack_text():
    if(request.method == "POST"):
        result = request.get_json()
        print(result)
        return "asdasd"
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
