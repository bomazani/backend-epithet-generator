from flask import Flask, render_template, jsonify

from sprint_a import app #??????

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def generate_epithets():
    return jsonify({"epithets":[]})

@app.route('/vocabulary')
def vocabulary():
    return jsonify({"vocabulary": {}})

if __name__ == '__main__':
    app.run()
