
import re
import unittest

from src.github import query
from python_colors import colors

class TestQuery(unittest.TestCase):
    generator = ['Python', 'C++', 'JavaScript']

    def test_empty_search(self):
        """
        Test for an empty result search
        """
        result = query.search(self.generator, 'Kotlin')
        self.assertEqual(list(result), [], 'Generator should be empty')

    def test_invalid_regex_pattern(self):
        """
        Test for a search with an invalid pattern
        """
        result = query.search(self.generator, 'C++', options=['e'])

        with self.assertRaises(re.error):
            list(result)

    def test_multiple_match_search(self):
        """
        Test for a search with multiple match
        """
        result = query.search(self.generator, '[\w\+]+', options=['e'])
        result_list = list(result)

        for i in range(len(result_list)):
            self.assertEqual(result_list[i], colors.red(self.generator[i]))

    def test_multiple_match_search2(self):
        """
        Test for a search with different matches in the same line
        """
        generator = [
            'no match',
            'still no match',
            'data-structures data_structures'
        ]

        result = query.search(generator, 'data[-_]structures', options=['e'])
        result_list = list(result)

        match_one = colors.red('data-structures')
        match_two = colors.red('data_structures')

        self.assertEqual(len(result_list), 1, 'The size should be equal to one')
        self.assertEqual(result_list[0], "{} {}".format(match_one, match_two))

if __name__ == '__main__':
    unittest.main()
