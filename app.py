from flask import Flask, Response

app = Flask(__name__)

@app.route("/answer", methods=["GET", "POST"])
def answer():
    xml = """<?xml version="1.0"?>
<Response>
    <Speak>Hello</Speak>
</Response>
"""
    return Response(xml, mimetype="application/xml")

@app.route("/")
def home():
    return "Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)