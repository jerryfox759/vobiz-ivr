from flask import Flask, request, Response

app = Flask(__name__)

BASE_URL = "https://vobiz-ivr.onrender.com"


@app.route("/")
def home():
    return "IVR Running"


@app.route("/answer", methods=["GET", "POST"])
def answer():

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>

<Gather
    action="{BASE_URL}/select-language"
    method="POST"
    inputType="dtmf"
    executionTimeout="10">

    <Speak>
        Hindi ke liye 1 dabayein.
        For English, press 2.
    </Speak>

</Gather>

<Speak>
    No input received.
</Speak>

</Response>
"""

    return Response(
        xml,
        content_type="text/xml; charset=utf-8"
    )


@app.route("/select-language", methods=["GET", "POST"])
def select_language():

    digit = request.form.get("Digits")

    if digit == "1":

        xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>

<Gather
    action="{BASE_URL}/select-department?lang=hi"
    method="POST"
    inputType="dtmf"
    executionTimeout="10">

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

<Gather
    action="{BASE_URL}/select-department?lang=en"
    method="POST"
    inputType="dtmf"
    executionTimeout="10">

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

    return Response(
        xml,
        content_type="text/xml; charset=utf-8"
    )


@app.route("/select-department", methods=["GET", "POST"])
def select_department():

    digit = request.form.get("Digits")

    if digit == "1":

        xml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>

<Dial>
    <Number>+917595989813</Number>
</Dial>

</Response>
"""

    elif digit == "2":

        xml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>

<Dial>
    <Number>+917595989813</Number>
</Dial>

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

    return Response(
        xml,
        content_type="text/xml; charset=utf-8"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)