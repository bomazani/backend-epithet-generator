# import unittest
import pytest
from . import helpers
from .helpers import json_path
from .app import app

# path =  "/Users/roberthunt/python/backend-epithet-generator/submissions/sprint_a/test_helpers.py"
quantity = 3
vocab = ['a flesh wound']

class TestHelpers:

    def test_random_words(self):
        result = helpers.random_words(vocab) 
        assert result == 'village idiot'

    def test_epithet_vocabulary(self):
        result = helpers.epithet_vocabulary(vocab) 
        self.assertEqual(result, 'village idiot2')

    def test_generate_epithet(self):
        result = helpers.generate_epithet(vocab, quantity) 
        self.assertEqual(result, 'a flesh wound')

    def test_multiple_epithets(self):
        result = helpers.multiple_epithets(vocab) 
        self.assertEqual(result, 'village idiot3')

    # def test_get_extension(self):
    #     result = helpers.get_extension(path)
    #     self.assertEqual(result, 'blancmange')
    
    # def test_read_json(self):
    #     resut = helpers.read_json(path, mode='r', *args, **kwargs)
    #     self.assertEqual(result, 'albatross')

    # def test_from_file(self):
    #     result = helpers.from_file(path, *args, **kwargs) 
    #     self.assertEqual(result, 'Dennis Moore')

    # def test_from_json(self):
    #     result = helpers.from_json(path, fields=True, *args, **kwargs) 
    #     self.assertEqual(result, 'Comfy chair')

    # def test_strategies(self):
    #     result = helpers.strategies(file_extension, intent='read') 
    #     self.assertEqual(result, 'lupins')

class TestRoutes:
    client = app.test_client()

    def test_root(self):
        result = self.client.get('/')
        assert result.status_code == 200
    
    def test_multiple_epithets(self):
        result = self.client.get('/epithet/4')
        assert result.status_code == 200

    def test_multiple_epithets(self):
        result = self.client.get('/epithet/')
        assert result.status_code == 200

    def test_root(self):
        result = self.client.get('/vocabulary')
        assert result.status_code == 200


# if __name__ == '__main__':
#     unittest.main()