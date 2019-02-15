import os
import pytest
import random
from . import helpers
from .app import app
from .helpers import json_path, FileManager
from unittest.mock import patch

quantity = 3
column_names = ["Column 1", "Column 2", "Column 3"]
path = json_path

""" To run tests: $ pytest --disable-warnings """
class TestHelpers:

    def test_random_words(self):
        """Varify each of the 3 randomly generated words came from the appropriate vocabulary column"""
        result = helpers.EpithetGenerator.random_words()
        assert result[0] in FileManager.read_json(path)['Column 1']
        assert result[1] in FileManager.read_json(path)['Column 2']
        assert result[2] in FileManager.read_json(path)['Column 3']

    def test_random_words_fail(self):
        """Varify first two randomly generated words is not a noun from vocabulary column 3"""
        result = helpers.EpithetGenerator.random_words()
        assert result[0] not in FileManager.read_json(path)['Column 3']
        assert result[1] not in FileManager.read_json(path)['Column 3']

    def test_random_words_fail(self):
        """Varify the last randomly generated word is not an adjective from vocabulary columns 1 or 2"""
        result = helpers.EpithetGenerator.random_words()
        assert result[2] not in FileManager.read_json(path)['Column 1']
        assert result[2] not in FileManager.read_json(path)['Column 2']

    def test_epithet_vocabulary(self):
        """Varify the vocabulary returned by epithet_vocabulary method equals the vocabulary in original data file"""
        result = helpers.EpithetGenerator.epithet_vocabulary(json_path, column_names) 
        assert result == FileManager.read_json(path)

    def test_epithet_vocabulary_fail(self):
        """Varify the vocabulary returned by epithet_vocabulary method is not equal to just a portion of vocabulary in original data file"""
        result = helpers.EpithetGenerator.epithet_vocabulary(json_path, column_names) 
        assert result != FileManager.read_json(path)['Column 1']
        assert result != FileManager.read_json(path)['Column 2']
        assert result != FileManager.read_json(path)['Column 3']

    def test_generate_epithet(self):
        """Varify the vocabulary words in a generated epithet come from the 1st, 2nd & 3rd columns of vocab words (respectively)"""
        result = helpers.EpithetGenerator.generate_epithet(json_path)
        result = result.replace(',', '')
        result = result.replace('!', '')
        assert result.split(' ')[1] in FileManager.read_json(json_path)['Column 1']
        assert result.split(' ')[2] in FileManager.read_json(json_path)['Column 2']
        assert result.split(' ')[3] in FileManager.read_json(json_path)['Column 3']

    def test_generate_epithet_fail(self):
        """Varify the two random adjectives in a generated epithet did not come from the noun vocabulary (column 3)"""
        result = helpers.EpithetGenerator.generate_epithet(json_path)
        result = result.replace(',', '')
        result = result.replace('!', '')
        assert result.split(' ')[1] not in FileManager.read_json(json_path)['Column 3']
        assert result.split(' ')[2] not in FileManager.read_json(json_path)['Column 3']

    def test_generate_epithet_fail(self):
        """Varify the random adjectives in a generated epithet did not come from the adjective vocabulary (columns 1 & 2)"""
        result = helpers.EpithetGenerator.generate_epithet(json_path)
        result = result.replace(',', '')
        result = result.replace('!', '')
        assert result.split(' ')[3] not in FileManager.read_json(json_path)['Column 1']
        assert result.split(' ')[3] not in FileManager.read_json(json_path)['Column 2']

    def test_multiple_epithets(self):
        """Varify the quantity entered returns the same quantity of epithets"""
        result = helpers.EpithetGenerator.multiple_epithets(path, quantity) 
        assert len(result) == quantity

    @patch('random.randint', return_value = 5)
    def test_random_epithets(self, x):
        """Varify the random_epithets method returns the appropriate number of epithets (Substituted '5' for the random quantity)"""
        result = helpers.EpithetGenerator.random_epithets(path) 
        assert len(result) == 5

    def test_random_epithets(self):
        """Varify the random_epithet method does not return a quantity outside of a range from 1 to 50"""
        result = helpers.EpithetGenerator.random_epithets(path) 
        assert len(result) > 0 and len(result) < 51

class TestRoutes:
    client = app.test_client()

    def test_root(self):
        """Varify route '/' returns a status code of '200' """
        result = self.client.get('/')
        assert result.status_code == 200

    def test_epithets(self):
        """Varify route '/epithets/<number>' returns a status code of '200' """
        result = self.client.get('/epithets/4')
        assert result.status_code == 200

    def test_epithets_default(self):
        """Varify route '/epithets' returns a status code of '200' """
        result = self.client.get('/epithets')
        assert result.status_code == 200

    def test_random(self):
        """Varify route '/random' returns a status code of '200' """
        result = self.client.get('/random')
        assert result.status_code == 200

    def test_vocabulary(self):
        """Varify route '/vocabulary' returns a status code of '200' """
        result = self.client.get('/vocabulary')
        assert result.status_code == 200
