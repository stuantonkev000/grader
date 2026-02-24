from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/grade", methods=["POST"])
def grade():
    worksheet_text = request.form["worksheet"]

    # TEMPORARY FAKE RESPONSE
    grade = "8/10"
    feedback = "This is a test response."

    return render_template("results.html", grade=grade, feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)