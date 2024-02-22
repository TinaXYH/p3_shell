import unittest
from src.apps.sort import Sort
from src.exceptions import InvalidArgumentError
from src.utils import InputInterface, OutputInterface


class TestSort(unittest.TestCase):

    def test_sort(self):
        sort = Sort(["sort/sort1.txt"], InputInterface(), OutputInterface())
        oi = sort.eval()
        content = "".join(oi.capture_content()).strip().split('\n')
        self.assertEqual(content, ["111", "222", "333"])

    def test_sort_reverse(self):
        sort = Sort(["-r", "sort/sort1.txt"],
                    InputInterface(), OutputInterface())
        oi = sort.eval()
        content = "".join(oi.capture_content()).strip().split('\n')
        self.assertEqual(content, ["333", "222", "111"])

    def test_sort_empty_file(self):
        sort = Sort(["sort/emptyfilesort.txt"],
                    InputInterface(), OutputInterface())
        oi = sort.eval()
        content = "".join(oi.capture_content()).strip().split('\n')
        self.assertEqual(content, [])

    def test_sort_file_invalid_flag(self):
        with self.assertRaises(InvalidArgumentError):
            sort = Sort(["-b", "sort/sort1.txt"],
                        InputInterface(), OutputInterface())
            sort.eval()

    def test_sort_invalid_filename(self):
        with self.assertRaises(FileNotFoundError):
            sort = Sort(["invalid_filename.txt"],
                        InputInterface(), OutputInterface())
            sort.eval()

    def test_sort_too_many_arguments(self):
        with self.assertRaises(InvalidArgumentError):
            sort = Sort(["-r", "-r", "-r"],
                        InputInterface(), OutputInterface())
            sort.eval()


if __name__ == '__main__':
    unittest.main()
