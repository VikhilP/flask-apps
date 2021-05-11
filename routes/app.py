from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/num')
def num():
    return 'Add a number to the URL'

@app.route('/num/<int:nums>')
def square(nums):
    return f"{nums} squared is {nums*nums}"

if __name__ == "__main__":
    app.run(debug=True)