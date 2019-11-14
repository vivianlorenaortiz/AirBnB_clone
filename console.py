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

    prompt = "(hbnb) "
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
        data = shlex.split(line)
        my_list = []
        if len(line) < 1:  # If only typed all
            # Print all the items of storage
            for key, value in storage.all().items():
                c_name, c_id = key.split(".")
                my_list.append("{}".format(value))
            print(my_list)
        else:
            if not data[0] in HBNBCommand.myclasses:
                print("** class doesn't exist **")
            else:
                # print all the keys with data[0]
                for key, value in storage.all().items():
                    c_name, c_id = key.split(".")
                    if c_name == data[0]:
                        my_list.append("{}".format(value))
                print(my_list)
    def do_update(self, line):
        '''
        Updates an instance based on the class name and id by adding or
        updating.
        '''
def do_update(self, line):
        '''
        Updates an instance based on the class name and id by adding or
        updating.
        '''
        data = shlex.split(line)
        if len(data) < 1:
            print("** class name missing **")
        elif not data[0] in HBNBCommand.myclasses:
            print("** class doesn't exist **")
        elif len(data) < 2:
            print("** instance id missing **")
        else:
            key = data[0] + "." + data[1]
            if key not in storage.all():
                print("** no instance found **")
            elif len(data) < 3:
                print("** attribute name missing **")
            elif len(data) < 4:
                print("** value missing **")
            else:
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    obj = storage.all().get(key)
                    setattr(obj, data[2], data[3])
                    storage.save()
                    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
