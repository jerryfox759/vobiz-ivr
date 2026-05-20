from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/answer", methods=["GET", "POST"])
def answer():
    xml = """
<Response>
    <Gather numDigits="1" action="/select-language" method="POST">
        <Speak>
            Hindi ke liye 1 dabayein. For English, press 2.
        </Speak>
    </Gather>
</Response>
"""
    return Response(xml, mimetype='text/xml')


@app.route("/select-language", methods=["GET", "POST"])
def select_language():
    digit = request.form.get("Digits")

    if digit == "1":
        xml = """
<Response>
    <Gather numDigits="1" action="/select-department?lang=hi" method="POST">
        <Speak language="hi-IN">
            Sales ke liye 1 dabayein, Support ke liye 2 dabayein.
        </Speak>
    </Gather>
</Response>
"""
    elif digit == "2":
        xml = """
<Response>
    <Gather numDigits="1" action="/select-department?lang=en" method="POST">
        <Speak>
            For Sales, press 1. For Support, press 2.
        </Speak>
    </Gather>
</Response>
"""
    else:
        xml = """
<Response>
    <Speak>Invalid option. Let us try again.</Speak>
    <Redirect>/answer</Redirect>
</Response>
"""

    return Response(xml, mimetype='text/xml')


@app.route("/select-department", methods=["GET", "POST"])
def select_department():
    digit = request.form.get("Digits")
    lang = request.args.get("lang", "en")

    if digit == "1":
        xml = """
<Response>
    <Dial>+917595989813</Dial>
</Response>
"""
    elif digit == "2":
        xml = """
<Response>
    <Dial>+917595989813</Dial>
</Response>
"""
    else:
        if lang == "hi":
            xml = """
<Response>
    <Speak language="hi-IN">A-vaidh vikalp. Kripya phir se koshish karein.</Speak>
    <Redirect>/answer</Redirect>
</Response>
"""
        else:
            xml = """
<Response>
    <Speak>Invalid option. Please try again.</Speak>
    <Redirect>/answer</Redirect>
</Response>
"""

    return Response(xml, mimetype='text/xml')


if __name__ == "__main__":
    app.run()