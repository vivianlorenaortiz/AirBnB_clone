#!/usr/bin/python3
"""
Console for HBNB
"""

import shlex
import cmd
import sys
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

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

        if len(args) == 0:
            print("** class name missing **")
            return
        token = args.split()

        try:
            nwInstance = eval(token[0])()
            nwInstance.save()
            print(nwInstance.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance"""
        temp = args.split()

        if len(temp) == 0:
            print("** class name missing **")
            return
        elif temp[0] not in self.myclasses:
            print("** class doesn't exist **")
            return
        elif len(temp) < 2:
            print('** instance id missing **')
            return
        else:
            all_objs = storage.all()
            for i in all_objs.keys():
                if i == "{}.{}".format(temp[0], temp[1]):
                    print(all_objs[i])
                    return
            print('** no instance found **')

    def do_destroy(self, line):
        '''
        Deletes an instance based on the class name and id.
        '''
        arg = line.split()

        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg[0] not in self.myclasses:
            print('** class doesn\'t exist **')
            return
        elif len(arg) < 2:
            print('** instance id missing **')
            return
        else:
            all_objs = storage.all()
            for i in all_objs:
                if i == "{}.{}".format(arg[0], arg[1]):
                    del all_objs[i]
                    storage.save()
                    return
            print('** no instance found **')

    def do_all(self, line):
        '''
        Prints all string representation of all instances based or not on the
        class name.
        '''
        args = line.split()
        all_objs = storage.all()

        if len(line) == 0:
            print(all_objs)

        elif line not in self.myclasses:
            print("** class doesn't exist **")
            return

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
        args = shlex.split(line)
        flag = 0

        if len(line) == 0:
            print("** class name missing **")
            return

        try:
            clsname = shlex.split(line)[0]
            eval("{}()".format(clsname))
        except IndexError:
            print("** class doesn't exist **")
            return

        try:
            instanceid = shlex.split(line)[1]
        except IndexError:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        try:
            clschange = all_objs["{}.{}".format(clsname, instanceid)]
        except IndexError:
            print("** no instance found **")
            return

        try:
            attributename = shlex.split(line)[2]
        except IndexError:
            print("** no instance found **")
            return

        try:
            updatevalue = shlex.split(line)[3]
        except IndexError:
            print("** value missing **")
            return

        else:
            try:
                setattr(clschange, attributename, int(updatevalue))
                storage.save()
            except:
                setattr(clschange, attributename, str(updatevalue))
                storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
