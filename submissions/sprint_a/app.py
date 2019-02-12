import os
import unittest

from flask import Flask, render_template, jsonify

from sprint_a import app, RESOURCES_ROOT
from sprint_a.helpers import EpithetGenerator as Epgen
# from sprint_a.helpers import data, column_names

data = Epgen.data
column_names = Epgen.column_names
json_path = os.path.join(RESOURCES_ROOT, 'data.json')


@app.route('/')
def generate_epithets():
    return jsonify(Epgen.generate_epithet(json_path))


@app.route('/vocabulary')
def vocabulary():
    # vocab = Epgen.epithet_vocabulary(data, column_names)
    return jsonify(Epgen.epithet_vocabulary(data, column_names))


@app.route('/epithets/<int:quantity>')
# @app.route('/epithets/<quantity>')
def epithet_quantity(quantity):
    print('QUANTITY: {}'.format(type(quantity)))
    return jsonify(Epgen.multiple_epithets(json_path))


# @app.route('/number', defaults={'my_num' : '1'})
# @app.route('/number/<int:my_num>')
# def number(my_num):
#     return 'The number is: ' + str(my_num)


if __name__ == '__main__':
    unittest.app()
