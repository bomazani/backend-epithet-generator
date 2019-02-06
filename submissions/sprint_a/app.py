from flask import Flask, render_template, jsonify

from sprint_a import app #??????

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def generate_epithets():
    # return render_template('insults.html')
    return jsonify({"epithets":[]})

@app.route('/vocabulary')
def vocabulary():
    # return render_template('vocab.html')
    return jsonify({"vocabulary": {}})

if __name__ == '__main__':
    app.run()
