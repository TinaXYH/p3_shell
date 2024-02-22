from src.apps.Application import Application
from src.exceptions import InvalidArgumentError
from src.utils import InputInterface, OutputInterface, File


class Cut(Application):
    def __init__(self, args: list[str], input_interface: InputInterface, output_interface: OutputInterface):
        super().__init__(args, input_interface, output_interface)
        self.lst_of_bytes = []
        self.contents = None

    @staticmethod
    def split_list(arg):
        first_lst = arg.split(',')
        return list(map(lambda s: s.split('-'), first_lst))

    def is_legal_list(self):
        lst_of_num = []
        for lst in self.split_list(self.args[1]):
            if len(lst) > 2:
                return False
            lst_of_num.extend(int(num) for num in lst if num != '')
        return lst_of_num == sorted(lst_of_num)

    def is_legal_option(self):
        return self.args[0] == '-b' and self.is_legal_list()

    def is_legal_file(self):
        return len(self.args[2]) > 0 and self.args[2][0] != '-'

    def is_legal_args(self):
        if len(self.args) not in [2, 3]:
            return False
        if len(self.args) == 2:
            return self.is_legal_option()
        else:
            return self.is_legal_option() and self.is_legal_file()

    def get_byte_indices(self):
        lst_of_indices = []
        for lst in self.split_list(self.args[1]):
            if len(lst) == 1:
                lst_of_indices.append(int(lst[0]) - 1)
            elif lst[0] == '':
                lst_of_indices.extend(range(int(lst[1])))
            elif lst[1] == '':
                lst_of_indices.extend([int(lst[0]) - 1, -1])
            else:
                lst_of_indices.extend(range((int(lst[0]) - 1), (int(lst[1]))))
        return lst_of_indices

    def cut_bytes(self):
        byte_indices = self.get_byte_indices()
        for line in self.contents:
            line_bytes = line.encode()
            line_length = len(line_bytes)
            self.lst_of_bytes.append([])
            for current, byte_index in enumerate(byte_indices):
                if byte_index >= line_length:
                    break
                self.cut_line(current, byte_index, byte_indices, line_bytes, line_length)

    def cut_line(self, current, byte_index, byte_indices, line_bytes, line_length):
        if byte_index == -1:
            previous_index = byte_indices[current - 1]
            rest_of_bytes = line_bytes[previous_index + 1:]
            self.lst_of_bytes[-1].extend(rest_of_bytes)

        elif byte_index < line_length:
            self.lst_of_bytes[-1].append(line_bytes[byte_index])
        else:
            return

    def eval(self) -> OutputInterface:
        if not self.is_legal_args():
            raise InvalidArgumentError(f"illegal arguments: {self.args}")
        self.contents = self.input_interface.readlines() if len(self.args) == 2 else File(self.args[2]).readlines()
        self.cut_bytes()
        decoded_contents = []
        for char_bytes in self.lst_of_bytes:
            decoded_content = bytes(char_bytes).decode()
            if decoded_content[0] != '\n' and decoded_content[-1] != '\n':
                decoded_content += '\n'
            decoded_contents.append(decoded_content)
        self.output_interface.set_content(decoded_contents)
        return self.output_interface

