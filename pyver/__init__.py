from importlib import import_module

__version__ = "1.2.0"

parse = import_module(".parse", __name__)
commands = import_module(".commands", __name__)
