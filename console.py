#!/usr/bin/python3
import cmd
import json
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    The command interpreter class for the HBNB project.
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """
        Method called when an empty line is entered, does nothing.
        """
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not args:
            print("** class name missing **")
        else:
            if args != "BaseModel":
                print("** class doesn't exist **")
            else:
                my_model = BaseModel()
                with open("file.json", 'w', encoding='utf-8') as output:
                    json.dump(my_model, output)
                    print(my_model.id)

    def do_show(self, args):
        if not args:
            print("** class name missing **")
        elif extends(args)[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            if extends(args)[0] and not extends(args)[1]:
                print("** instance id missing **")
            with open("file.json", 'r') as output:
                load = json.load(output)
                for i in range(len(load)):
                    if extends(args)[1] != load[i].id:
                        print("**no instance found**")
                    else:
                        print(load[i].__str__)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
