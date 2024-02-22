import unittest
from src.apps.uniq import Uniq
from src.exceptions import InvalidArgumentError
from src.utils import InputInterface, OutputInterface


class TestUniq(unittest.TestCase):

    # case-sensitive
    def test_uniq(self):
        uniq = Uniq(["uniq/uniq1.txt"], InputInterface(), OutputInterface())
        oi = uniq.eval()
        content = "".join(oi.capture_content()).strip().split('\n')
        self.assertEqual(content, ["AAA", "aaa", "AAA"])

    # OPTION: -i   case-insensitive
    def test_uniq_case_insensitive(self):
        uniq = Uniq(["-i", "uniq/uniq1.txt"],
                    InputInterface(), OutputInterface())
        oi = uniq.eval()
        content = "".join(oi.capture_content()).strip().split('\n')
        self.assertEqual(content, ["AAA"])

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            uniq = Uniq(["-i", "notuniq.txt"],
                        InputInterface(), OutputInterface())
            uniq.eval()

    def test_uniq_file_invalid_flag(self):
        with self.assertRaises(InvalidArgumentError):
            uniq = Uniq(["-b", "uniq/uniq1.txt"],
                        InputInterface(), OutputInterface())
            uniq.eval()

    def test_uniq_too_many_arguments(self):
        with self.assertRaises(InvalidArgumentError):
            uniq = Uniq(["-i", "-i", "-i"],
                        InputInterface(), OutputInterface())
            uniq.eval()


if __name__ == '__main__':
    unittest.main()
