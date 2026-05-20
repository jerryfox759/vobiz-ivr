from flask import Flask, request, Response

app = Flask(__name__)

BASE_URL = "https://vobiz-ivr.onrender.com"

# Your Vobiz Number
CALLER_ID = "918065480651"

# Your Mobile Number
FORWARD_NUMBER = "917595989813"


@app.route("/")
def home():
    return "Vobiz IVR Running"


# =====================================
# MAIN IVR
# =====================================
@app.route("/answer", methods=["GET", "POST"])
def answer():

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>

<Speak>
    Welcome to our company.
</Speak>

<Gather
    action="{BASE_URL}/select-language"
    method="POST"
    inputType="dtmf"
    executionTimeout="10">

    <Speak>
        For Hindi, press 1.
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


# =====================================
# LANGUAGE SELECTION
# =====================================
@app.route("/select-language", methods=["GET", "POST"])
def select_language():

    print("Language Selection:", request.form)

    digit = request.form.get("Digits")

    # HINDI
    if digit == "1":

        xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>

<Gather
    action="{BASE_URL}/select-department"
    method="POST"
    inputType="dtmf"
    executionTimeout="10">

    <Speak>
        Sales ke liye 1 press karein.
        Support ke liye 2 press karein.
    </Speak>

</Gather>

</Response>
"""

    # ENGLISH
    elif digit == "2":

        xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>

<Gather
    action="{BASE_URL}/select-department"
    method="POST"
    inputType="dtmf"
    executionTimeout="10">

    <Speak>
        Press 1 for Sales.
        Press 2 for Support.
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


# =====================================
# DEPARTMENT SELECTION
# =====================================
@app.route("/select-department", methods=["GET", "POST"])
def select_department():

    print("Department Selection:", request.form)

    digit = request.form.get("Digits")

    # SALES
    if digit == "1":

        xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>

<Speak>
    Connecting your call to Sales.
</Speak>

<Dial callerId="{CALLER_ID}">
    <Number>{FORWARD_NUMBER}</Number>
</Dial>

</Response>
"""

    # SUPPORT
    elif digit == "2":

        xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>

<Speak>
    Connecting your call to Support.
</Speak>

<Dial callerId="{CALLER_ID}">
    <Number>{FORWARD_NUMBER}</Number>
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