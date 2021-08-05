import unittest
from mdfmt.core import Formatter

class SpaceTestCase(unittest.TestCase):
    def setUp(self):
        self.formatter = Formatter()

    def test_space(self):
        raw = ""
        expected = ""
        got = self.formatter.format(raw)
        self.assertEqual(expected, got)

    def test_isupper(self):
        pass
        #self.assertTrue('FOO'.isupper())
        #self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()
