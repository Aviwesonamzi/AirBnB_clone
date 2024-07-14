#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()  # Print a newline for a clean exit
        return True

    def emptyline(self):
        """Do nothing on empty line input"""
        pass

    def default(self, line):
        """Handle unknown commands"""
        if line.strip() == "":
            return
        print("*** Unknown syntax: {}".format(line))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
