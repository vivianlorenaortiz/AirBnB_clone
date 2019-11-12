#!/usr/bin/python3
"""
Console for HBNB
"""
valid_class = ["BaseModel"]

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""
    prompt = "(hbnb)"

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """End of File command to quit the program"""
        return True

    def emptyline(self):
        """An empty line and ENTER should not execute anything"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel and prints the id"""
        var1 = args.split()
        if len(var1) == 0:
            print("** class name missing **")
        else:
            if var1[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                object = BaseModel()
                object.save()
                valid_class.append(object)
                print(object.id)
                print(valid_class)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        temp = args.split()
        if len(temp) == 0:
            print("** class name missing **")
        for items in valid_class:
            if temp[0] != items:
                print("** class doesn't exist **")
            if temp[1] != items:
                print("** intance id missing**")
            elif len(args) >= 2 and temp[0] == items:
                print(temp[0])

if __name__ == '__main__':
     HBNBCommand().cmdloop()
