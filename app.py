from flask import Flask, render_template, request

from google import genai

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

client = genai.Client()


@app.route("/grade", methods=["POST"])
def grade():
    worksheet_text = request.form["worksheet"]

    prompt = "You are a teacher grading a student's worksheet. The worksheet contains the following text:\n\n" + worksheet_text + "\n\nPlease provide a grade out of 10 and feedback for the student."

    grade = "Grade this text out of 100"

    response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=prompt
    )

    response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=grade
    )


    # TEMPORARY FAKE RESPONSE
    grade = f"{grade} out of 100"
    feedback = response.txt

    return render_template("results.html", grade=grade, feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)