import os
from flask import Flask, render_template

try:
    from my_config import API_KEY

except ImportError:
    API_KEY= os.environ.get('API_KEY')

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/candidates")
def candi():
    return render_template("Candidates.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/proposal")
def proposal():
    return render_template("proposal.html")

@app.route("/aboutUs")
def aboutUs():
    return render_template("aboutUs.html")

@app.route("/credit")
def credit():
    return render_template("credit.html")

@app.route("/where")
def where():
    return render_template("where.html", API_KEY=API_KEY)


@app.route("/candidates/joe_biden")
def Biden():
    return render_template("Biden.html")

@app.route("/candidates/bernie_sanders")
def Sanders():
    return render_template("Sanders.html")

@app.route("/candidates/donald_trump")
def donald_trump():
    return render_template("Trash.html")

@app.route("/candidates/kamala_harris")
def Harris():
    return render_template("Harris.html")

@app.route("/candidates/elizabeth_warren")
def Warren():
    return render_template("Warren.html")

@app.route("/candidates/pete_buttigieg")
def Buttigieg():
    return render_template("Buttigieg.html")



if __name__=="__main__":
    app.run()
