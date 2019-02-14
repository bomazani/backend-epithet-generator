import os
import pytest
import random
from . import helpers
from .app import app
from .helpers import json_path, FileManager

quantity = 3
column_names = ["Column 1", "Column 2", "Column 3"]
path = json_path

""" To run tests: $ pytest --disable-warnings """
class TestHelpers:

    def test_random_words(self):
        result = helpers.EpithetGenerator.random_words()
        assert result[0] in FileManager.read_json(path)['Column 1']
        assert result[1] in FileManager.read_json(path)['Column 2']
        assert result[2] in FileManager.read_json(path)['Column 3']

    def test_random_words_fail(self):
        result = helpers.EpithetGenerator.random_words()
        assert result[0] not in FileManager.read_json(path)['Column 2']
        assert result[1] not in FileManager.read_json(path)['Column 3']
        assert result[2] not in FileManager.read_json(path)['Column 1']

    def test_epithet_vocabulary(self):
        result = helpers.EpithetGenerator.epithet_vocabulary(json_path, column_names) 
        assert result == FileManager.read_json(path)

    def test_epithet_vocabulary_fail(self):
        result = helpers.EpithetGenerator.epithet_vocabulary(json_path, column_names) 
        assert result != FileManager.read_json(path)['Column 1']
        assert result != FileManager.read_json(path)['Column 2']
        assert result != FileManager.read_json(path)['Column 3']

    def test_generate_epithet(self):
        result = helpers.EpithetGenerator.generate_epithet(json_path)
        result = result.replace(',', '')
        result = result.replace('!', '')
        assert result.split(' ')[1] in FileManager.read_json(json_path)['Column 1']
        assert result.split(' ')[2] in FileManager.read_json(json_path)['Column 2']
        assert result.split(' ')[3] in FileManager.read_json(json_path)['Column 3']

    def test_generate_epithet_fail(self):
        result = helpers.EpithetGenerator.generate_epithet(json_path)
        result = result.replace(',', '')
        result = result.replace('!', '')
        assert result.split(' ')[1] not in FileManager.read_json(json_path)['Column 2']
        assert result.split(' ')[2] not in FileManager.read_json(json_path)['Column 3']
        assert result.split(' ')[3] not in FileManager.read_json(json_path)['Column 1']

    def test_multiple_epithets(self):
        result = helpers.EpithetGenerator.multiple_epithets(path, quantity) 
        assert len(result) == quantity

    def test_multiple_epithets_fail(self):
        result = helpers.EpithetGenerator.multiple_epithets(path, quantity) 
        assert len(result) != quantity + 1


class TestRoutes:
    client = app.test_client()

    def test_root(self):
        result = self.client.get('/')
        assert result.status_code == 200

    def test_root_fail(self):
        result = self.client.get('/')
        assert result.status_code != 404

    def test_multiple_epithets(self):
        result = self.client.get('/epithets/4')
        assert result.status_code == 200

    def test_multiple_epithets_fail(self):
        result = self.client.get('/epithets/4')
        assert result.status_code != 404

    def test_multiple_epithets_default(self):
        result = self.client.get('/epithets')
        assert result.status_code == 200

    def test_multiple_epithets_default_fail(self):
        result = self.client.get('/epithets')
        assert result.status_code != 404

    def test_vocabulary(self):
        result = self.client.get('/vocabulary')
        assert result.status_code == 200

    def test_vocabulary_fail(self):
        result = self.client.get('/vocabulary')
        assert result.status_code != 404
