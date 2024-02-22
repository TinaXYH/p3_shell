from src.CmdTreeConverter import CmdTreeConverter
from src.apps.ApplicationFactory import ApplicationFactory
from src.commands.SequenceCommand import SequenceCommand
from src.commands.call.CallCommand import CallCommand
from src.commands.call.argument.Argument import Argument
from src.commands.call.argument.Atom import Atom
from src.commands.call.argument.quoted.BackQuoted import BackQuoted
from src.commands.call.argument.quoted.DoubleQuoted import DoubleQuoted
from src.commands.call.argument.quoted.Quoted import Quoted
from src.commands.call.argument.quoted.SingleQuoted import SingleQuoted
from src.commands.call.argument.redirection import *
from src.commands.call.argument.redirection.OutputRedirection import OutputRedirection
from src.commands.pipe.RecursivePipeCommand import RecursivePipeCommand
from src.commands.pipe.SimplePipeCommand import SimplePipeCommand
from src.converters.CommandConverter import CommandConverter
from src.exceptions import InvalidArgumentError
from src.utils import InputInterface, OutputInterface


class Evaluator:
    @staticmethod
    def visit_single_quoted(obj: SingleQuoted) -> str:
        return obj.content

    def visit_back_quoted(self, obj: BackQuoted) -> str:
        raw_tree = CmdTreeConverter.convert(obj.content)
        command = raw_tree.accept(CommandConverter())
        oi = command.accept(self)
        return oi.capture_content()

    def visit_double_quoted(self, obj: DoubleQuoted) -> str:
        return "".join(c.accept(self) if isinstance(c, BackQuoted) else c for c in obj.content)

    def visit_atom(self, obj: Atom) -> str:
        return obj.content.accept(self) if isinstance(obj.content, Quoted) else obj.content

    def visit_input_redirection(self, obj: InputRedirection) -> InputInterface:
        return InputInterface(mode='file', filepath=obj.filepath.accept(self))

    def visit_output_overwrite(self, obj: OutputRedirectionOverwrite) -> OutputInterface:
        return OutputInterface(mode='file_overwrite', filepath=obj.filepath.accept(self))

    def visit_output_append(self, obj: OutputRedirectionAppend) -> OutputInterface:
        return OutputInterface(mode='file_append', filepath=obj.filepath.accept(self))

    def visit_argument(self, obj: Argument) -> (list[str], InputInterface, OutputInterface):
        input_interface = None
        output_interface = None
        args: list[str] = []

        def has_io(mode: int) -> bool:
            """
            check interfaces
            :param mode:
                Type: int.

                Values:
                    0: check input interface.

                    1: check output interface.

                    2: check both.
            :return:
                True: has the checked interface(s)
                False: empty
            """
            match mode:
                case 0:
                    return input_interface is not None
                case 1:
                    return output_interface is not None
                case 2:
                    return input_interface is not None or output_interface is not None

        def guard(mode: int):
            """
            raise exceptions if meets semantic error
            :param mode:
                Type: int
                Values:
                    0: guard Atom
                    1: guard input interface
                    2: guard output interface
            """
            match mode:
                case 0:
                    if has_io(2):
                        raise InvalidArgumentError("Argument must before the redirections")
                case 1:
                    if has_io(0):
                        raise InvalidArgumentError("Too many input redirections")
                    if has_io(1):
                        raise InvalidArgumentError("Input redirection must before output redirection")
                case 2:
                    if has_io(1):
                        raise InvalidArgumentError("Too many output redirections")

        for c in obj.contents:
            if isinstance(c, Atom):
                guard(0)
                args.append(c.accept(self))
            elif isinstance(c, InputRedirection):
                guard(1)
                input_interface = c.accept(self)
            elif isinstance(c, OutputRedirection):
                guard(2)
                output_interface = c.accept(self)
        if not has_io(0):
            input_interface = InputInterface()
        if not has_io(1):
            output_interface = OutputInterface()
        return args, input_interface, output_interface

    def visit_call(self, obj: CallCommand, oi: OutputInterface = None) -> OutputInterface:
        appname = obj.appname
        args, input_interface, output_interface = obj.arg.accept(self)
        if oi:
            input_interface.from_output(oi)
        app_object = ApplicationFactory.get_application(appname, args, input_interface, output_interface)
        return app_object.eval()

    def visit_sequence_command(self, obj: SequenceCommand) -> OutputInterface:
        oi_left = obj.left.accept(self)
        oi_right = obj.right.accept(self)
        return OutputInterface.concatenate(oi_left, oi_right)

    def visit_simple_pipe(self, obj: SimplePipeCommand) -> OutputInterface:
        oi_left = obj.left.accept(self)
        return self.visit_call(obj.right, oi_left)

    def visit_recursive_pipe(self, obj: RecursivePipeCommand):
        oi_left = obj.left.accept(self)
        return self.visit_call(obj.right, oi_left)
