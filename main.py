from flask import Flask, render_template, request, make_response


app = Flask(__name__)


@app.route("/")
def scryp():
    return render_template("index.html")


@app.route("/setcookie", methods=["POST", "GET"])
def setcookie():
    if request.method == "POST":
        name = request.form["name"]

        response = make_response(render_template("cookie.html"))
        response.set_cookie("NAME", name)

    return response


@app.route("/getcookie")
def getcookie():
    name = request.cookies.get("NAME")
    return f"<h1>Welcome {name} </h1>" + render_template("language.html")


@app.route("/language", methods=["POST", "GET"])
def language():
    if request.method == "POST":
        selected_language = request.form.get("language")
        if selected_language == "en":
            return "Вы выбрали английский язык."
        elif selected_language == "ru":
            return "Вы выбрали русский язык."


app.run(debug=True, host="0.0.0.0")
