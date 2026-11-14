from flask import Flask

app = Flask(__name__)

@app.route("/alkuluku/<int:luku>")
def tarkista(luku):
    for i in range(2, luku):
        if luku % i == 0:
            return {"Number": luku, "isPrime": False}

    return {"Number": luku, "isPrime": True}

app.run(port=3000)