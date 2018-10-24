from importlib import import_module

version = "1.0.0"

parse = import_module(".parse", __name__)
commands = import_module(".commands", __name__)
