import requests
from flask import Flask, render_template, redirect, url_for

from flask import request
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
       if request.method== 'GET' :
           return render_template("register.html")
       else :
           print(request.form)
           user = request.form.get("account")
           pwd = request.form.get("pwd")
           print(user,pwd)

           return  "注册成功"




@app.route("/do/reg" ,methods=["GET"])

def do_register():
    # print(request.args)
    return "注册成功"
@app.route("/login",methods=['GET'])
def Login():
    print("登入成功")

@app.route("/xiaomi",methods=['GET'])
def xiaomi():
    return render_template("xiaomi.html")


if __name__ == '__main__':
    app.run()
