from src.apps.Application import Application
from src.utils import OutputInterface


class UnsafeDecorator(object):
    def __init__(self, application: Application):
        self.app = application

    def eval(self) -> OutputInterface:
        try:
            return self.app.eval()
        except Exception as e:
            print(f"Exception: {e}")
