# Import flask to use multiple HTML web pages
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("dictionary.csv")


# the next line is connected to home function because of the @ symbol
@app.route("/")
def home():
    return render_template("home.html")


# Special syntax around station and date
@app.route("/api/v1/<word>")
def about(word):
    # Extract definition from the word
    # Squeeze converts definition to string
    # df.loc useful for accessing specific rows or columns
    definition = df.loc[df["word"] == word]['definition'].squeeze()
    result_dictionary = {'word': word, 'definition': definition}
    return result_dictionary


# Only runs the website if this script is run directly from this file
if __name__ == "__main__":
    # Adding debug=True allows us to see errors on the web page
    app.run(debug=True)
