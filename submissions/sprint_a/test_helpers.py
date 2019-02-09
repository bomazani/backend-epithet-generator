import unittest
# import pytest
from sprint_a import helpers

path =  "/Users/roberthunt/python/backend-epithet-generator/submissions/sprint_a/test_helpers.py"
quantity = 3
vocab = ['a flesh wound']
class TestHelpers(unittest.TestCase):

    def test_get_extension(self):
        result = helpers.get_extension(path)
        self.assertEqual(result, 'blancmange')
    

    def test_read_json(self):
        resut = helpers.read_json(path, mode='r', *args, **kwargs)
        self.assertEqual(result, 'albatross')


    def test_from_file(self):
        result = helpers.from_file(path, *args, **kwargs) 
        self.assertEqual(result, 'Dennis Moore')


    def test_from_json(self):
        result = helpers.from_json(path, fields=True, *args, **kwargs) 
        self.assertEqual(result, 'Comfy chair')


    def test_strategies(self):
        result = helpers.strategies(file_extension, intent='read') 
        self.assertEqual(result, 'lupins')


    def test_random_words(self):
        result = helpers.random_words(vocab) 
        self.assertEqual(result, 'village idiot')


    def test_generate_epithet(self):
        result = helpers.generate_epithet(vocab, quantity) 
        self.assertEqual(result, 'a flesh wound')
