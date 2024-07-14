#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for HBNB.

    Attributes:
        prompt (str): The custom command prompt.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Args:
            arg (str): The argument passed to the command (not used).

        Returns:
            bool: True to exit the command loop.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.

        Args:
            arg (str): The argument passed to the command (not used).

        Returns:
            bool: True to exit the command loop.
        """
        print()  # Print a newline for a clean exit
        return True

    def emptyline(self):
        """
        Do nothing on empty line input.

        Returns:
            None
        """
        pass

    def default(self, line):
        """
        Handle unknown commands.

        Args:
            line (str): The input line.

        Returns:
            None
        """
        if line.strip() == "":
            return
        print("*** Unknown syntax: {}".format(line))

if __name__ == '__main__':
    """
    Entry point of the command interpreter.
    """
    HBNBCommand().cmdloop()
