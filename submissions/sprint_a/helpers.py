import os
import json
import random
from sprint_a import app, RESOURCES_ROOT

json_path = os.path.join(RESOURCES_ROOT, 'data.json')

class FileManager:
    """Handle local file system IO."""

    @staticmethod
    def get_extension(path):
        """Get file extension from file path."""
        return os.path.splitext(path)[-1][1:]

    @staticmethod
    def read_json(path, mode='r', *args, **kwargs):
        """Read json file from file path."""
        with open(path, mode=mode, *args, **kwargs) as handle:
            return json.load(handle)


class Vocabulary:
    """Standardize vocabulary representation from multiple sources."""
    files = FileManager()
    

    @classmethod
    def from_file(cls, path, *args, **kwargs):
        """ """
        extension = cls.files.get_extension(path)
        representation = cls.strategies(extension)(path, *args, **kwargs)
        return representation

    @classmethod
    def from_json(cls, path, fields=True, *args, **kwargs):
        """ """
        data = cls.files.read_json(path, *args, **kwargs)
        if fields:
            representation = (data, data.keys())
        else:
            representation = data
        # print('representation: {}'.format(representation))
        return representation

    @classmethod
    def strategies(cls, file_extension, intent='read'):
        """ """
        input_strategies = {'json': cls.from_json}
        if intent is 'read':
            return input_strategies[file_extension]


class EpithetGenerator:
    """Generate epithet from dictionary of adjectives & nouns."""

    data, column_names = Vocabulary.from_file(json_path)

    @classmethod
    def random_words(cls):
        """Select one random word from each column of the list."""
        """random.choice() & Map()"""
        # map through the keys in the list then random.choice through each list associated with each key/column & append to words list
        # print(random.choice()) # enter in data from each separate column
        words = [random.choice(cls.data[i]) for i in cls.column_names]

        print('data: {}'.format(cls.data))
        print('column_names: {}'.format(cls.column_names))
        print('words: {}'.format(words))
        return words

    @classmethod
    def epithet_vocabulary(cls, data, column_names):
        """Return vocabulary available to the epithet generator """
        return cls.data
        
    @classmethod
    def generate_epithet(cls, path, quantity=1):
        """Generate a single epithet from 3 randomly selected vocabulary words"""
        epithet_words = cls.random_words()
        epithet = ("Thou {}, {} {}!".format(epithet_words[0], epithet_words[1], epithet_words[2]))
        return epithet

    @classmethod
    def multiple_epithets(cls, path, quantity=3):
        """Generate a quantity of epithets based on the quantity provided"""
        multi_epithets = []
        i = 1
        while i<= quantity:
            multi_epithets.append(cls.generate_epithet(path))
            i += 1
        return multi_epithets
