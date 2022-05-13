from AYA import AyA
from flask import Flask, render_template,jsonify
app = Flask(__name__)


@app.get('/')
def home():

    return render_template('Random-Aya.html')

@app.get('/api')
def api():
    aya = AyA.get_aya()
    return jsonify(**aya)
