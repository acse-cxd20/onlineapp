from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def root():
    a = request.args.get('a', default=0, type=int)
    b = request.args.get('b', default=0, type=int)

    return f"<b>Hello</b> World! The sum of {a} + {b} = {a + b}"