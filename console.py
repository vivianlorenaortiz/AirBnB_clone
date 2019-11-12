#!/usr/bin/python3
"""
Console for HBNB
"""
valid_class = ["BaseModel"]

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""
    prompt = "(hbnb)"
    myclasses = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

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

    def do_destroy(self, line):
        '''
        Deletes an instance based on the class name and id.
        '''
        arg = line.split()
        if len(line) == 0:
            print('** class name missing **')
            return False
        elif arg[0] not in self.myclasses:
            print('** class doesn\'t exist **')
            return False
        elif len(arg) < 2:
            print('** instance id missing **')
            return False
        else:
            all_objs = storage.all()
            for i in all_objs:
                if i == "{}.{}".format(arg[0], arg[1]):
                    del all_objs[i]
                    storage.save()
                    return False
            print('** no instance found **')


if __name__ == '__main__':
     HBNBCommand().cmdloop()
