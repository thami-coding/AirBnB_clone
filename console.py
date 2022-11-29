#!/usr/bin/python3
"""
program called console.py that
contains the entry point of the
command interpreter
"""


import cmd
import json
from models.base_model import BaseModel
from os.path import exists


def isfloat(num):
    """Checks if a string is a float"""
    try:
        float(num)
        return True
    except ValueError:
        return False


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
        """press CTRL + D Exit program"""
        print()
        return True

    def emptyline(self):
        """
        Dont exceute previous command
        when enter is pressed with an empty line
        """
        pass

#
    def do_create(self, arg):
        """
        Creates a new instance of
        BaseModel,pass class as an argument,
        saves it (to the JSON file)
        and prints the id
        """
        if arg == 'BaseModel':
            base_model = BaseModel()
            base_model.save()
            print(base_model.id)
        elif len(arg) == 0:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation
        of an instance based on the class
        name and id
        """
        arg_list = arg.split()
        arg_len = len(arg_list)

        if arg_len == 0:
            print("** class name missing **")
        elif arg_len == 1 and arg != "BaseModel":
            print("** class doesn't exist **")
        elif arg_len == 1:
            print("** instance id missing **")
        elif arg_len == 2 and arg_list[0] == 'BaseModel':
            cls_name, cls_id = arg_list
            cls_name_id = "{}.{}".format(cls_name, cls_id)
            with open('file.json', 'r', encoding="utf-8") as f:
                objects = json.load(f)
            flag = 0
            for key in objects.keys():
                if key == cls_name_id:
                    dct = objects[key]
                    base_model = BaseModel(**dct)
                    print(base_model)
                    flag = 1
            if not flag:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on
        the class name and id
        (save the change into the JSON file)
        """
        arg_list = arg.split()
        arg_len = len(arg_list)

        if arg_len == 0:
            print("** class name missing **")
        elif arg_list[0] != "BaseModel":
            print("** class doesn't exist **")
        elif arg_len == 1:
            print("** instance id missing **")
        elif arg_len == 2 and arg_list[0] == 'BaseModel':
            cls_name, cls_id = arg_list
            cls_name_id = "{}.{}".format(cls_name, cls_id)
            with open('file.json', 'r', encoding="utf-8") as f:
                objects = json.load(f)

            with open('file.json', 'w', encoding="utf-8") as f:
                flag = 0
                for key in list(objects.keys()):
                    if key == cls_name_id:
                        del objects[key]
                        json.dump(objects, f)
                        flag = 1
            if not flag:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation
        of all instances based or not on
        the class name
        """
        args = arg.split()
        arg_len = len(args)
        if arg_len > 0 and args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif exists("file.json"):
            objs_list = []
            with open('file.json', 'r', encoding="utf-8") as f:
                objects = json.load(f)
            for key in objects.keys():
                base_model = BaseModel(**objects[key])
                objs_list.append(base_model.__str__())
            print(objs_list)

    def do_update(self, arg):
        """
        Updates an instance based
        on the class name and id by adding
        or updating attribute
        (save the change into the JSON file)
        """
        args = arg.split()
        arglen = len(args)

        if arglen == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif arglen == 1:
            print("** instance id missing **")
        elif arglen == 2:
            print("** attribute name missing **")
        elif arglen == 3:
            print("** value missing **")
        else:
            cls_name, cls_id, email, value = [args[i]for i in range(0, 4)]
            if value.isdigit():
                value = int(value)
            elif isfloat(value):
                value = float(value)

            cls_name_id = "{}.{}".format(cls_name, cls_id)
            with open('file.json', 'r', encoding="utf-8") as f:
                objects = json.load(f)
            with open('file.json', 'w', encoding="utf-8") as f:
                flag = 0
                for key in list(objects.keys()):
                    if key == cls_name_id:
                        dct = objects[key]
                        del objects[key]
                        base_model = BaseModel(**dct)
                        setattr(base_model, email, value)
                        objects[key] = base_model.to_dict()
                        flag = 1
                json.dump(objects, f)
            if not flag:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
