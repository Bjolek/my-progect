from flask import *


app = Flask("Shop")
db_name = "Site.db"

@app.route("/")
def base():
    return render_template("base.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/products")
def products():
    return render_template("products.html")

app.run()