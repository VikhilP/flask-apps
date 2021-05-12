from flask import Flask, render_template

app = Flask(__name__)

@app.route('/vikhil')
def vikhil():
    return render_template('vikhil.html')

@app.route('/sugon')
def sugon():
    return render_template('sugon.html')

@app.route("/bnames")
def bnames():
    return render_template("bnames.html", names = ["ben", "harry", "bob", "jay", "matt", "bill"])

if __name__ == "__main__":
    app.run(debug=True)