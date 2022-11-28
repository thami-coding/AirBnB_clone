#!/usr/bin/python3
"""
program called console.py that
contains the entry point of the
command interpreter
"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand
    contains the entry point of the
    command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Exit program"""
        print()
        return True

    def emptyline(self):
        """dont exceute previous command"""
        pass

    def do_create(self, arg):
        if arg == 'BaseModel':
            base_model = BaseModel()
            base_model.save()
            print(base_model.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
