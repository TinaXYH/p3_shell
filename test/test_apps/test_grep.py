import unittest
from src.exceptions import InvalidArgumentError
from src.utils import InputInterface, OutputInterface
from src.apps.grep import Grep


class TestGrep(unittest.TestCase):

    def test_grep_no_match(self):
        grep = Grep(["AAA", "grep/grep1.txt"],
                    InputInterface(), OutputInterface())
        oi = grep.eval()
        content = oi.capture_content()
        self.assertEqual(content, [])

    def test_grep_single_match(self):
        grep = Grep(["AAA", "grep/grep2.txt"],
                    InputInterface(), OutputInterface())
        oi = grep.eval()
        content = oi.capture_content()
        self.assertEqual(content, ["AAA\n"])

    def test_grep_multiple_match(self):
        grep = Grep(["AAA", "grep/grep3.txt"],
                    InputInterface(), OutputInterface())
        oi = grep.eval()
        content = oi.capture_content()
        self.assertEqual(content, ["AAA\n", "AAA\n"])

    def test_grep_single_match_re(self):
        grep = Grep(["A..", "grep/grep3.txt"],
                    InputInterface(), OutputInterface())
        oi = grep.eval()
        content = oi.capture_content()
        self.assertEqual(content, ["AAA\n", "AAA\n"])

    def test_globbing(self):
        grep = Grep(["AAA", "grep/grep*.txt"],
                    InputInterface(), OutputInterface())
        oi = grep.eval()
        content = oi.capture_content()
        self.assertEqual(content, ["grep/grep2.txt:AAA\n",
                                   "grep/grep3.txt:AAA\n",
                                   "grep/grep3.txt:AAA\n",
                                   "grep/grep4.txt:AAA\n"])

    def test_grep_multiple_files(self):
        grep = Grep(["AAA", "grep/grep3.txt", "grep/grep4.txt"],
                    InputInterface(), OutputInterface())
        oi = grep.eval()
        content = oi.capture_content()
        self.assertEqual(content, ["grep/grep3.txt:AAA\n",
                                   "grep/grep3.txt:AAA\n",
                                   "grep/grep4.txt:AAA\n"])

    def test_grep_multiple_files_re(self):
        grep = Grep(["...", "grep/grep3.txt", "grep/grep4.txt"],
                    InputInterface(), OutputInterface())
        oi = grep.eval()
        content = "".join(oi.capture_content()).strip().split('\n')
        self.assertEqual(content, ["grep/grep3.txt:This test case 3 for grep function.",
                                   "grep/grep3.txt:AAA",
                                   "grep/grep3.txt:AAA",
                                   "grep/grep3.txt:wil be found in this line the second time.",
                                   "grep/grep4.txt:This test case 4 for grep function, copy of grep3.txt",
                                   "grep/grep4.txt:AAA",
                                   "grep/grep4.txt:RRR"])

    def test_invalid_argument(self):
        with self.assertRaises(InvalidArgumentError):
            grep = Grep(["AAA", "grep/grep2.txt", "ababab"],
                        InputInterface(), OutputInterface())
            grep.eval()

    def test_invalid_globbing(self):
        with self.assertRaises(InvalidArgumentError):
            grep = Grep(["AAA", "grep/*asdasdsadad"],
                        InputInterface(), OutputInterface())
            grep.eval()


if __name__ == '__main__':
    unittest.main()
