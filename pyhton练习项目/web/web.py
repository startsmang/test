import requests
from flask import Flask,render_template

from requests import request
app = Flask(__name__)

@app.route("/get/info")


def index():
    return render_template("index.html")

@app.route("/get/news")

def get_news():
    "ghello"
    return  "ghello"

@app.route("/register",methods=['GET'])
def register():
        return render_template("register.html")

#
# @app.route("/post/reg",methods=["POST"])
# def post_register():
#     print(request.form)
#     return "注册成功"

@app.route("/do/reg" ,methods=["GET"])

def do_register():
    # print(request.args)
    return "注册成功"
@app.route("/login",methods=['GET'])
def Login():
    print("登入成功")


if __name__ == '__main__':
    app.run()