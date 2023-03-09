from flask import Flask,render_template
app = Flask(__name__)

@app.route("/get/info")


def index():
    return render_template("index.html")

@app.route("/get/news")

def get_news():
    "ghello"
    return  "ghello"

if __name__ == '__main__':
    app.run()