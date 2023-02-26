import unittest

from src import keywords_in_changes_counter

keywords = ['python', 'programming', 'keyword', 'asdfsadfsadf']


class KeywordsInChangesCounterTest(unittest.TestCase):
    def test_keywords_counter(self):
        with open('resources/python.html', 'r', encoding='utf-8') as f1, \
                open('resources/python2.html', 'r', encoding='utf-8') as f2:
            page1 = f1.read()
            page2 = f2.read()

        keywords_counter = keywords_in_changes_counter.KeywordsInChangesChecker(page1, page2,
                                                                                keywords)
        keywords_in_change = keywords_counter.get_keywords_in_changed_part()
        self.assertEqual(['python', 'programming', 'keyword'], keywords_in_change)
