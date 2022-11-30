#!/usr/bin/python3
"""
program called console.py that
contains the entry point of the
command interpreter
"""


import cmd
import json
from models.base_model import BaseModel
from models.user import User
from os.path import exists


def isfloat(num):
    """Checks if a string is a float"""
    try:
        float(num)
        return True
    except ValueError:
        return False


def check_cls(cls):
    """Checks if the user entered a valid class"""
    if cls == 'BaseModel':
        return True
    elif cls == 'User':
        return True
    else:
        return False


def create_model(arg, **kwargs):
    """createa a new model based on the class entered"""
    args = arg.split()
    cls_name = ""
    if len(args) > 0:
        cls_name = args[0]
    if cls_name != 'User':
        if kwargs and kwargs['__class__'] == 'BaseModel':
            return BaseModel(**kwargs)
        elif cls_name == 'BaseModel':
            return BaseModel()

    if cls_name != 'BaseModel':
        if kwargs and kwargs['__class__'] == 'User':
            return User(**kwargs)
        elif cls_name == 'User':
            return User()


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

    def do_create(self, arg):
        """
        Creates a new instance of
        BaseModel,pass class as an argument,
        saves it (to the JSON file)
        and prints the id
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif check_cls(arg.split()[0]):
            model = create_model(arg)
            model.save()
            print(model.id)
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
        elif not check_cls(arg_list[0]):
            print("** class doesn't exist **")
        elif arg_len == 1:
            print("** instance id missing **")
        elif arg_len == 2 and check_cls(arg_list[0]):
            cls_name, cls_id = arg_list
            cls_name_id = "{}.{}".format(cls_name, cls_id)
            with open('file.json', 'r', encoding="utf-8") as f:
                objects = json.load(f)
            flag = 0
            for key in objects.keys():
                if key == cls_name_id:
                    dct = objects[key]
                    model = create_model(arg, **dct)
                    print(model)
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
        elif not check_cls(arg_list[0]):
            print("** class doesn't exist **")
        elif arg_len == 1:
            print("** instance id missing **")
        elif arg_len == 2 and check_cls(arg_list[0]):
            cls_name, cls_id = arg_list
            cls_name_id = "{}.{}".format(cls_name, cls_id)
            with open('file.json', 'r', encoding="utf-8") as f:
                objects = json.load(f)

            flag = 0
            for key in list(objects.keys()):
                if key == cls_name_id:
                    with open('file.json', 'w', encoding="utf-8") as f:
                        print(key)
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
        print(args[0])
        if arg_len > 0 and not check_cls(args[0]):
            print("** class doesn't exist **")
        elif exists("file.json"):
            objs_list = []
            with open('file.json', 'r',     encoding="utf-8") as f:
                objects = json.load(f)
            for key in objects.keys():
                model = create_model(arg, **objects[key])
                objs_list.append(model.__str__())
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
        elif not check_cls(args[0]):
            print("** class doesn't exist **")
        elif arglen == 1:
            print("** instance id missing **")
        elif arglen == 2:
            print("** attribute name missing **")
        elif arglen == 3:
            print("** value missing **")
        else:
            cls_name, cls_id, attribute, value = [args[i] for i in range(0, 4)]
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
                        model = create_model(arg, **dct)
                        setattr(type(model), attribute, value)
                        objects[key] = model.to_dict()
                        flag = 1
                json.dump(objects, f)
            if not flag:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
