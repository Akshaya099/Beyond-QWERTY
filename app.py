from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        address = request.form.get("address")
        return f"Form submitted successfully! Name: {name}, Email: {email}, Phone: {phone}, Address: {address}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
