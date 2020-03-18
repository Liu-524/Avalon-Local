from flask import Flask
from flask import render_template
from flask import current_app

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/init")
def init():
    current_app.c_pass = 0
    current_app.c_deny = 0
    return render_template("success_page.html")

@app.route("/vote")
def vote():
    return render_template("vote.html")

@app.route("/agree")
def agree():
    current_app.c_pass += 1
    return render_template("success_page.html")

@app.route("/deny")
def deny():
    current_app.c_deny += 1
    return render_template("success_page.html")

@app.route("/clear")
def clear():
    current_app.c_pass = 0
    current_app.c_deny = 0
    return render_template("success_page.html")

@app.route("/display")
def display():
    return "通过：" + str(current_app.c_pass) + "\n" + "反对：" + str(current_app.c_deny)  + "\n"

if __name__ == "__main__":
    app.run("0.0.0.0", 5002,debug=True)