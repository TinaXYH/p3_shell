import unittest
from src.apps.uniq import Uniq
from src.utils import InputInterface, OutputInterface


class MyTestCase(unittest.TestCase):
    def test_something(self):
        uniq = Uniq(["temp.txt"], InputInterface(), OutputInterface())
        oi = uniq.eval()
        output = "".join(oi.capture_content()).strip().split('\n')
        self.assertEqual(["AAA", "aaa", "BBB", "aaa"], output)

    def test_another_thing(self):
        uniq = Uniq(["-i", "temp.txt"], InputInterface(), OutputInterface())
        oi = uniq.eval()
        output = "".join(oi.capture_content()).strip().split('\n')
        self.assertEqual(["AAA", "BBB", "aaa"], output)


if __name__ == '__main__':
    unittest.main()
