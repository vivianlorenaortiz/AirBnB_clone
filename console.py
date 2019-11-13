#!/usr/bin/python3
"""
Console for HBNB
"""

import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity


valid_class = ["BaseModel"]


class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""
    prompt = "(hbnb)"

    myclasses = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                 "Review"]

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
        elif temp[0] not in self.myclasses:
            print("** class doesn't exist **")

        elif len(temp) < 2:
            print('** instance id missing **')
        else:
            all_objs = storage.all()
            for i in all_objs.keys():
                if i == "{}.{}".format(temp[0], temp[1]):
                    print(all_objs[i])
                    return False
                print('** no instance found **')

    def do_destroy(self, line):
        '''
        Deletes an instance based on the class name and id.
        '''
        arg = line.split()
        if lpren(line) == 0:
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

    def do_all(self, line):
        '''
        Prints all string representation of all instances based or not on the
        class name.
        '''
        args = line.split()
        all_objs = storage.all()

        if line not in self.myclasses:
            print("** class doesn't exist **")
        else:
            for i in all_objs:
                if i.startswith(args[0]):
                    strg = str(all_objs[i])
                    print(strg)

    def do_update(self, line):
        '''
        Updates an instance based on the class name and id by adding or
        updating.
        '''
        updatevalue = 0.0
        args = line.split()
        flag = 0

        if len(line) == 0:
            print("** class name missing **")

        try:
            clsname = line.split()[0]
            eval("{}()".format(clsname))
        except IndexError:
            print("** class doesn't exist **")

        try:
            instanceid = line.split()[1]
        except IndexError:
            print("** instance id missing **")

        all_objs = storage.all()
        try:
            clschange = all_objs["{}.{}".format(clsname, instanceid)]
        except IndexError:
            print("** no instance found **")

        try:
            attributename = line.split()[2]
        except IndexError:
            print("** no instance found **")

        try:
            updatevalue = line.split()[3]
        except IndexError:
            print("** value missing **")
        else:
            try:
                setattr(clschange, attributename, int(updatevalue))
                storage.save()
            except:
                setattr(clschange, attributename, str(updatevalue))
                storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
