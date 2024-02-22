import unittest
from src.apps.cut import Cut
from src.exceptions import InvalidArgumentError
from src.utils import InputInterface, OutputInterface, File


class TestCut(unittest.TestCase):
    # cut -b 1-2 cut/cut1.txt > cut/example1.txt
    def test_cut1_1(self):
        cut = Cut(['-b', '1-2', 'cut/cut1.txt'], InputInterface(), OutputInterface())
        io = cut.eval()
        content = io.capture_content()
        out = File('cut/cut.temp')
        out.writelines(content)
        example = File('cut/example1.txt').read()
        actual_out = out.read()
        self.assertEqual(example, actual_out)

    # cut -b 1 cut/cut1.txt > cut/example2.txt
    def test_cut1_2(self):
        cut = Cut(['-b', '1', 'cut/cut1.txt'], InputInterface(), OutputInterface())
        io = cut.eval()
        content = io.capture_content()
        out = File('cut/cut.temp')
        out.writelines(content)
        example = File('cut/example2.txt').read()
        actual_out = out.read()
        self.assertEqual(example, actual_out)

    # cut -b -2 cut/cut1.txt > cut/example3.txt
    def test_cut1_3(self):
        cut = Cut(['-b', '-2', 'cut/cut1.txt'], InputInterface(), OutputInterface())
        io = cut.eval()
        content = io.capture_content()
        out = File('cut/cut.temp')
        out.writelines(content)
        example = File('cut/example3.txt').read()
        actual_out = out.read()
        self.assertEqual(example, actual_out)

    # cut -b 1,2,3 cut/cut2.txt > cut/example4.txt
    def test_cut2_1(self):
        cut = Cut(['-b', '1,2,3', 'cut/cut2.txt'], InputInterface(), OutputInterface())
        io = cut.eval()
        content = io.capture_content()
        out = File('cut/cut.temp')
        out.writelines(content)
        example = File('cut/example4.txt').read()
        actual_out = out.read()
        self.assertEqual(example, actual_out)

    # cut -b 1-3,5-7 cut/cut2.txt > cut/example5.txt
    def test_cut2_2(self):
        cut = Cut(['-b', '1-3,5-7', 'cut/cut2.txt'], InputInterface(), OutputInterface())
        io = cut.eval()
        content = io.capture_content()
        out = File('cut/cut.temp')
        out.writelines(content)
        example = File('cut/example5.txt').read()
        actual_out = out.read()
        self.assertEqual(example, actual_out)

    # cut -b 1- cut/cut2.txt > cut/example6.txt
    def test_cut2_3(self):
        cut = Cut(['-b', '1-', 'cut/cut2.txt'], InputInterface(), OutputInterface())
        io = cut.eval()
        content = io.capture_content()
        out = File('cut/cut.temp')
        out.writelines(content)
        example = File('cut/example6.txt').read()
        actual_out = out.read()
        self.assertEqual(example, actual_out)

    # cut -b -3 cut/cut2.txt > cut/example7.txt
    def test_cut2_4(self):
        cut = Cut(['-b', '-3', 'cut/cut2.txt'], InputInterface(), OutputInterface())
        io = cut.eval()
        content = io.capture_content()
        out = File('cut/cut.temp')
        out.writelines(content)
        example = File('cut/example7.txt').read()
        actual_out = out.read()
        self.assertEqual(example, actual_out)

    # cut -b -3,5- cut/cut2.txt > cut/example8.txt
    def test_cut2_5(self):
        cut = Cut(['-b', '-3,5-', 'cut/cut2.txt'], InputInterface(), OutputInterface())
        io = cut.eval()
        content = io.capture_content()
        out = File('cut/cut.temp')
        out.writelines(content)
        example = File('cut/example8.txt').read()
        actual_out = out.read()
        self.assertEqual(example, actual_out)

    # cut -b -3,7- cut/cut_chinese.txt > cut/example_chinese_1.txt
    def test_cut_chinese_1(self):
        cut = Cut(['-b', '-3,7-', 'cut/cut_chinese.txt'], InputInterface(), OutputInterface())
        io = cut.eval()
        content = io.capture_content()
        out = File('cut/cut.temp')
        out.writelines(content)
        example = File('cut/example_chinese_1.txt').read()
        actual_out = out.read()
        self.assertEqual(example, actual_out)

    # cut -b 1-4,11- cut/cut_chinese.txt > cut/example_chinese_2.txt
    def test_cut_chinese_2(self):
        cut = Cut(['-b', '1-4,11-', 'cut/cut_chinese.txt'], InputInterface(), OutputInterface())
        io = cut.eval()
        content = io.capture_content()
        out = File('cut/cut.temp')
        out.writelines(content)
        example = File('cut/example_chinese_2.txt').read()
        actual_out = out.read()
        self.assertEqual(example, actual_out)

    # cut -b 1-3,33- cut/cut_chinese.txt > cut/example_chinese_3.txt
    def test_cut_chinese_3(self):
        cut = Cut(['-b', '1-3,33-', 'cut/cut_chinese.txt'], InputInterface(), OutputInterface())
        io = cut.eval()
        content = io.capture_content()
        out = File('cut/cut.temp')
        out.writelines(content)
        example = File('cut/example_chinese_3.txt').read()
        actual_out = out.read()
        self.assertEqual(example, actual_out)

    def test_exception_1(self):
        with self.assertRaises(FileNotFoundError):
            cut = Cut(['-b', '-3,5-', 'aba'], InputInterface(), OutputInterface())
            cut.eval()

    def test_exception_2(self):
        with self.assertRaises(InvalidArgumentError):
            cut = Cut(['-b', '1-2-3', 'cut/cut2.txt'], InputInterface(), OutputInterface())
            cut.eval()

    def test_exception_3(self):
        with self.assertRaises(InvalidArgumentError):
            cut = Cut(['-b', '1-3,2-4', 'cut/cut2.txt'], InputInterface(), OutputInterface())
            cut.eval()


if __name__ == '__main__':
    unittest.main()
