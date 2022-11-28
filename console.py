#!/usr/bin/python3
"""
program called console.py that
contains the entry point of the
command interpreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        "Quit command to exit the program\n"
        return True

    def do_EOF(self, line):
        "Exit program"
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
