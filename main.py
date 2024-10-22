# Import flask to use multiple HTML web pages
from flask import Flask, render_template

app = Flask(__name__)


# the next line is connected to home function because of the @ symbol
@app.route("/")
def home():
    return render_template("home.html")


# Special syntax around station and date
@app.route("/api/v1/<word>")
def about(word):
    uppercase = word.upper()
    result = {"definition": uppercase, "word": word}
    return result


# Only runs the website if this script is run directly from this file
if __name__ == "__main__":
    # Adding debug=True allows us to see errors on the web page
    app.run(debug=True)
