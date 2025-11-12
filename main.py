from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/<color>")
def page_color(color):
    if color == "green":
        return render_template("green.html")
    elif color == "blue":
        return render_template("blue.html")
    elif color == "red":
        return render_template("red.html")
    else:
        return "Color not found", 404



