from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_url_path="/static")

app.static_folder = "templates/static/"

app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0


@app.route("/")
def index():
    return render_template("index.html")
