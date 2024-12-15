from flask import *


app = Flask("Shop")
db_name = "Site.db"

@app.route("/")
def index():
    return render_template("index.html")

app.run()