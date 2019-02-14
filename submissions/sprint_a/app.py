import os
import random

from flask import Flask, render_template, jsonify

from .initialize import app, RESOURCES_ROOT
from .helpers import EpithetGenerator as Epgen

data = Epgen.data
column_names = Epgen.column_names
json_path = os.path.join(RESOURCES_ROOT, 'data.json')
random_qty = random.randint(1, 50)


@app.route('/')
def generate_epithets():
    return jsonify(Epgen.generate_epithet(json_path))


@app.route('/vocabulary')
def vocabulary():
    return jsonify(Epgen.epithet_vocabulary(data, column_names))


@app.route('/epithets', defaults={'quantity' : 1})
@app.route('/epithets/<int:quantity>')
def epithet_quantity(quantity):
    return jsonify(Epgen.multiple_epithets(json_path, quantity))


@app.route('/random')
def random_epithets():
    return jsonify(Epgen.random_epithets(json_path))


if __name__ == '__main__':
    unittest.app()
