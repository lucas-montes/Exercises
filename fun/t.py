import unittest
import re


def par(line: str):
    m = re.compile(r"")
    return m.search(line).groups()


class TTest(unittest.TestCase):
    def test_t(self):
        self.assertEqual(par("C"))
