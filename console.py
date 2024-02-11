#!/usr/bin/python3
"""Command interpreter for HBNB project"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            if args[0] not in globals():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + '.' + args[1]
            obj_dict = storage.all()
            obj = obj_dict.get(key)
            if not obj:
                print("** no instance found **")
            else:
                print(obj)
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            if args[0] not in globals():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + '.' + args[1]
            obj_dict = storage.all()
            obj = obj_dict.get(key)
            if not obj:
                print("** no instance found **")
            else:
                del obj_dict[key]
                storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        obj_dict = storage.all()
        if not arg:
            print([str(obj) for obj in obj_dict.values()])
            return
        try:
            if args[0] not in globals():
                print("** class doesn't exist **")
                return
            print([str(obj) for key, obj in obj_dict.items()
                   if key.split('.')[0] == args[0]])
        except IndexError:
            print("** class name missing **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            if args[0] not in globals():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + '.' + args[1]
            obj_dict = storage.all()
            obj = obj_dict.get(key)
            if not obj:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(obj, args[2], eval(args[3]))
            obj.save()
        except IndexError:
            print("** instance id missing **")

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
