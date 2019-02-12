import os
import unittest

from flask import Flask, render_template, jsonify

from sprint_a import app, RESOURCES_ROOT
from sprint_a.helpers import EpithetGenerator as Epgen

json_path = os.path.join(RESOURCES_ROOT, 'data.json')

@app.route('/')
def generate_epithets():
    return jsonify(Epgen.generate_epithet(json_path))

@app.route('/vocabulary')
def vocabulary():
    return jsonify({"vocabulary": {}})

@app.route('/epithets/<quantity>')
def epithet_quantity():
    return

if __name__ == '__main__':
    unittest.app()
