from flask import Flask,url_for
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/test")
def abc():
    return "test page"

@app.route("/style")
@app.route("/style2/<name>")
def style(name="lsx"):

    return url_for('static', filename="style.css")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
