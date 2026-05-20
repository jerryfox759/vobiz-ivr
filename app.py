from flask import Flask, request, Response

app = Flask(__name__)

BASE_URL = "https://mainivr.onrender.com"


@app.route("/answer", methods=["GET", "POST"])
def answer():

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Gather numDigits="1"
            action="{BASE_URL}/select-language"
            method="POST">

        <Speak>
            Hindi ke liye 1 dabayein.
            For English, press 2.
        </Speak>

    </Gather>
</Response>
"""

    return Response(xml, mimetype="application/xml")


@app.route("/select-language", methods=["GET", "POST"])
def select_language():

    digit = request.form.get("Digits")

    if digit == "1":

        xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>

    <Gather numDigits="1"
            action="{BASE_URL}/select-department?lang=hi"
            method="POST">

        <Speak>
            Sales ke liye 1 dabayein.
            Support ke liye 2 dabayein.
        </Speak>

    </Gather>

</Response>
"""

    elif digit == "2":

        xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>

    <Gather numDigits="1"
            action="{BASE_URL}/select-department?lang=en"
            method="POST">

        <Speak>
            For Sales, press 1.
            For Support, press 2.
        </Speak>

    </Gather>

</Response>
"""

    else:

        xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Speak>
        Invalid option.
    </Speak>

    <Redirect>
        {BASE_URL}/answer
    </Redirect>

</Response>
"""

    return Response(xml, mimetype="application/xml")


@app.route("/select-department", methods=["GET", "POST"])
def select_department():

    digit = request.form.get("Digits")
    lang = request.args.get("lang", "en")

    if digit == "1":

        xml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Dial>+917595989813</Dial>
</Response>
"""

    elif digit == "2":

        xml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Dial>+917595989813</Dial>
</Response>
"""

    else:

        if lang == "hi":

            xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>

    <Speak>
        Kripya phir se koshish karein.
    </Speak>

    <Redirect>
        {BASE_URL}/answer
    </Redirect>

</Response>
"""

        else:

            xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>

    <Speak>
        Invalid option.
    </Speak>

    <Redirect>
        {BASE_URL}/answer
    </Redirect>

</Response>
"""

    return Response(xml, mimetype="application/xml")


@app.route("/")
def home():
    return "IVR Running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)