from flask import Flask,request,jsonify

app=Flask(__name__)


@app.get("/user")
def get_data():
    return "fetched user data"

@app.post("/save_user")
def save_data():
    data=request.get_json()
    name=data["name"]
    phone=data["phone"]

    return jsonify({"name": name, "phone": phone})

@app.post("/user/<int:id>")
def func(id):
    try:
        print(f"Id is:  {id}")
    except KeyError:
        return "id not found in request"

    return f"Id is:  {id}"