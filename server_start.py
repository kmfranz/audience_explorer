from flask import Flask

app = Flask("server")

@app.route("/")
def hello():
    return "Hello"



app.run(threaded = True)
