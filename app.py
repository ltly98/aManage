from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/anime")
def anime():
    return render_template('anime.html')


@app.route("/t_anime")
def t_anime():
    return render_template('t_anime.html')


@app.route("/setting")
def setting():
    return render_template('setting.html')


if __name__ == "__main__":
    app.run()
