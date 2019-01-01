import pathlib


curdir = pathlib.Path('./coms')
ret = []


for command in curdir.iterdir():
    if command.name[0] != "_" and command.name[0] != ".":
        ret.append(command.name[:-3])

__all__ = ret
