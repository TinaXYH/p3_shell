from src.CmdTreeConverter import CmdTreeConverter
from src.Evaluator import Evaluator
from src.converters.CommandConverter import CommandConverter


class TestingFramework:
    def __init__(self, command: str):
        oi = CmdTreeConverter.convert(command).accept(CommandConverter()).accept(Evaluator())
        print(oi.capture_content())
