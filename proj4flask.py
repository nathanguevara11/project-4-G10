from flask import Flask, render_template, jsonify
import requests



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/one')
def one():
    return render_template('one.html')
@app.route('/two')
def two():
    return render_template('two.html')
@app.route('/three')
def three():
    return render_template('three.html')
@app.route('/four')
def four():
    return render_template('four.html')
@app.route('/five')
def five():
    return render_template('five.html')
if __name__ == "__main__":
    app.run(debug = True)