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

@app.route("/register",methods=['GET','POST'])
def register():
    if request.methods =="GET":
        return render_template("register.html")
    else:
         user = requests.form.get("account")
         print(user)

#
# @app.route("/post/reg",methods=["POST"])
# def post_register():
#     print(request.form)
#     return "注册成功"

# @app.route("/do/reg" ,methods=["GET"])
#
# def do_register():
#     # print(request.args)
#     return "注册成功"


if __name__ == '__main__':
    app.run()