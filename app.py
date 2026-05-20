from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home():
    return "Running"


@app.route("/answer", methods=["GET", "POST"])
def answer():

    xml = """<?xml version="1.0"?>
<Response>
</Response>"""

    return Response(
        xml,
        content_type="text/xml; charset=utf-8"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)