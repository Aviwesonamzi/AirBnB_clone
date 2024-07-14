#!/usr/bin/python3
"""Defines the HBNB console."""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Defines the HBNB command interpreter."""
    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel, 'User': User, 'State': State,
        'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review
    }

    def precmd(self, line):
        """Parses command input to handle dot notation."""
        match = re.match(r"(\w+)\.(\w+)\((.*)\)", line)
        if match:
            cls_name, command, args = match.groups()
            if command == "all":
                return f"do_all {cls_name}"
            elif command == "count":
                return f"do_count {cls_name}"
        return line

    def do_create(self, arg):
        """Creates a new instance of a class."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        print(instance)

    def do_destroy(self, arg):
        """Deletes an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances."""
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
            return
        instances = [
            str(obj) for obj in storage.all().values()
            if not arg or obj.__class__.__name__ == arg
        ]
        print(instances)

    def do_count(self, arg):
        """Retrieves the number of instances of a class."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        count = sum(1 for obj in storage.all().values() if obj.__class__.__name__ == arg)
        print(count)

    def do_update(self, arg):
        """Updates an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(instance, args[2], args[3])
        instance.save()

    def emptyline(self):
        """Overrides the default behavior to do nothing."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
