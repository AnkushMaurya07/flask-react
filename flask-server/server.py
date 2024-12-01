# route named members  which returns json array 
from flask import Flask

app = Flask(__name__)

#Members api route
@app.route("/members")
def memebers():
    return {"members":["Member1", "Member2", "Member3"]}

if __name__ == "__main__":
    app.run(debug=True)
    