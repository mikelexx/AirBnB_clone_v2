#!/usr/bin/python3
"""Defines the HBNB console."""
import cmd
from shlex import split
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sys


class HBNBCommand(cmd.Cmd):

    """ Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
        }

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")
        exit()
    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, terminal_input):
        """Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
        Create a new class instance with given keys/values and print its id.
        """
        try:
            if not terminal_input:
                raise SyntaxError()
            input_list = terminal_input.split(" ")
            kwargs = {}
            for i in range(1, len(input_list)):
                key, value = tuple(input_list[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                print(input_list[0])
                new_instance = eval(input_list[0])()
            else:
                new_instance = eval(input_list[0])(**kwargs)
                storage.new(new_instance)
            print(new_instance.id)
            new_instance.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, terminal_input):
        """ Method to show an individual object """
        try:
            if not terminal_input:
                raise SyntaxError()
            input_list = terminal_input.split(" ")
            if input_list[0] not in self.__classes:
                raise NameError()
            if len(input_list) < 2:
                raise IndexError()
            new_instanceects = storage.all()
            key = input_list[0] + '.' + input_list[1]
            if key in new_instanceects:
                print(new_instanceects[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, terminal_input):
        """ Destroys a specified object """
        try:
            if not terminal_input:
                raise SyntaxError()
            print(terminal_input)
            input_list = terminal_input.split(" ")
            if input_list[0] not in self.__classes:
                raise NameError()
            if len(input_list) < 2:
                raise IndexError()
            new_instanceects = storage.all()
            key = input_list[0] + '.' + input_list[1]
            if key in new_instanceects:
                del new_instanceects[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, terminal_input):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated new_instanceects."""
        if not terminal_input:
            o = storage.all()
            if len(o) > 0:
                print("[", end="")
                for k in o:
                    print(o[k], end="")
                print("]")
            #print([o[k].__str__() for k in o])
            return
        try:
            args = terminal_input.split(" ")
            if args[0] not in self.__classes:
                print(args[0],"not in ",  self.__classes)
                raise NameError()
            plint_list = []
            o = storage.all(eval(args[0]))
                
            if len(o) > 0:
                print("[", end="")
                for k in o:
                    print(o[k], end="")
                print("]")
           # print([o[k] for k in o])

        except NameError:
            print("** class doesn't exist **")
    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_update(self, terminal_input):
        """Updates an instanceby adding or updating attribute
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no new_instanceect taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
            AttributeError: when there is no attribute given
            ValueError: when there is no value given
        """
        try:
            if not terminal_input:
                raise SyntaxError()
            input_list = split(terminal_input, " ")
            if input_list[0] not in self.__classes:
                raise NameError()
            if len(input_list) < 2:
                raise IndexError()
            new_instanceects = storage.all()
            key = input_list[0] + '.' + input_list[1]
            if key not in new_instanceects:
                raise KeyError()
            if len(input_list) < 3:
                raise AttributeError()
            if len(input_list) < 4:
                raise ValueError()
            v = new_instanceects[key]
            try:
                v.__dict__[input_list[2]] = eval(input_list[3])
            except Exception:
                v.__dict__[input_list[2]] = input_list[3]
                v.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")
    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")

    def strip_clean(self, args):
        """parses the arguments and return a string of command
        Args:
            args: input list of args
        Return: formatted string of args
        """
        new_list = []
        new_list.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            new_list.append(((new_str.split(", "))[0]).strip('"'))
            new_list.append(my_dict)
            return new_list
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        new_list.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in new_list)

    def default(self, terminal_input):
        """retrieve all instances of a class and
        retrieve the total count of the instances
        """
        input_list = terminal_input.split('.')
        if len(input_list) >= 2:
            if input_list[1] == "all()":
                self.do_all(input_list[0])
            elif input_list[1] == "count()":
                self.count(input_list[0])
            elif input_list[1][:4] == "show":
                self.do_show(self.strip_clean(input_list))
            elif input_list[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(input_list))
            elif input_list[1][:6] == "update":
                args = self.strip_clean(input_list)
                if isinstance(args, list):
                    new_instance = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, terminal_input)
    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        for k, v in storage._FileStorage__objects.items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """ """
        print("Usage: count <class_name>")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
