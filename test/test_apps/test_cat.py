import unittest
from src.apps.cat import Cat
from src.exceptions import InvalidArgumentError
from src.utils import InputInterface, OutputInterface, File


class TestCat(unittest.TestCase):
    def test_cat1(self):
        cat = Cat(["cat/cat1.txt"], InputInterface(), OutputInterface())
        oi = cat.eval()
        content = oi.capture_content()
        f = File('cat/cat.temp')
        f.writelines(content)
        read_content = f.read()
        with open('cat/example1.out', 'r') as example_file:
            example_content = example_file.read()
            self.assertEqual(read_content, example_content)

    def test_cat2(self):
        cat = Cat(["cat/cat2.txt"], InputInterface(), OutputInterface())
        oi = cat.eval()
        content = oi.capture_content()
        f = File('cat/cat.temp')
        f.writelines(content)
        read_content = f.read()
        with open('cat/example2.out', 'r') as example_file:
            example_content = example_file.read()
            self.assertEqual(read_content, example_content)

    def test_cat1_cat2(self):
        cat = Cat(["cat/cat1.txt", "cat/cat2.txt"], InputInterface(), OutputInterface())
        oi = cat.eval()
        content = oi.capture_content()
        f = File('cat/cat.temp')
        f.writelines(content)
        read_content = f.read()
        with open('cat/example3.out', 'r') as example_file:
            example_content = example_file.read()
            self.assertEqual(read_content, example_content)

    def test_globbing(self):
        cat = Cat(["cat/cat*.txt"], InputInterface(), OutputInterface())
        oi = cat.eval()
        content = oi.capture_content()
        f = File('cat/cat.temp')
        f.writelines(content)
        read_content = f.read()
        with open('cat/example4.out', 'r') as example_file:
            example_content = example_file.read()
            self.assertEqual(read_content, example_content)

    def test_cat2_cat1(self):
        cat = Cat(["cat/cat2.txt", "cat/cat1.txt"], InputInterface(), OutputInterface())
        oi = cat.eval()
        content = oi.capture_content()
        f = File('cat/cat.temp')
        f.writelines(content)
        read_content = f.read()
        with open('cat/example5.out', 'r') as example_file:
            example_content = example_file.read()
            self.assertEqual(read_content, example_content)

    def test_invalid_argument(self):
        with self.assertRaises(InvalidArgumentError):
            cat = Cat(["cat/cat2.txt", "ababab"], InputInterface(), OutputInterface())
            oi = cat.eval()

    def test_invalid_globbing(self):
        with self.assertRaises(InvalidArgumentError):
            cat = Cat(["cat/*asdasdsadad"], InputInterface(), OutputInterface())
            oi = cat.eval()


if __name__ == '__main__':
    unittest.main()