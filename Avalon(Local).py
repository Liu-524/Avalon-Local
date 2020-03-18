from flask import Flask
from flask import render_template
from flask import current_app as c_a
import random
import time
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/init")
def init():
    c_a.c_pass = 0
    c_a.c_deny = 0
    #8 人 局
    character = ["莫德雷德(坏人举手不举)", "梅林(看到坏人除了莫德雷德)",
                    "奥伯伦(看不到坏人队友)", "派西维尔(看梅林和莫甘娜)", 
                    "村民", "村民", "莫甘娜(与梅林一同被派西维尔看到)", 
                    "刺客(坏人失败是刺杀梅林)"]
    random.seed(time.time())
    random.shuffle(character)
    c_a.character = character
    return render_template("success_page.html")

@app.route("/<player>")
def result(player):
    return render_template("player.html", player_char = c_a.character[int(player)])

@app.route("/vote")
def vote():
    return render_template("vote.html")

@app.route("/agree")
def agree():
    c_a.c_pass += 1
    return render_template("success_page.html")

@app.route("/deny")
def deny():
    c_a.c_deny += 1
    return render_template("success_page.html")

@app.route("/clear")
def clear():
    c_a.c_pass = 0
    c_a.c_deny = 0
    return render_template("success_page.html")

@app.route("/display")
def display():
    return render_template("display.html", hao = c_a.c_pass, huai = c_a.c_deny)

if __name__ == "__main__":
    app.run("0.0.0.0", 5002,debug=True)