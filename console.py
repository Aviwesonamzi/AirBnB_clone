#!/usr/bin/python3
# console.py

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
# Add other necessary imports...

class HBNBCommand(cmd.Cmd):
    # Existing code...

    def do_create(self, args):
        """Create a new instance of BaseModel, save it (to the JSON file), and print the id."""
        if not args:
            print("** class name missing **")
            return
        try:
            cls = globals()[args]
        except KeyError:
            print("** class doesn't exist **")
            return
        new_instance = cls()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        try:
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name."""
        if not args:
            for obj in storage.all().values():
                print(obj)
        else:
            if args not in globals():
                print("** class doesn't exist **")
                return
            for key, obj in storage.all().items():
                if key.startswith(args):
                    print(obj)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        try:
            obj = storage.all()[key]
        except KeyError:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3].strip('"')
        setattr(obj, attr_name, attr_value)
        obj.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
