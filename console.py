#!/usr/bin/python3
'''class definition that contains the entry point of the command interpreter'''

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

from models import storage


class HBNBCommand(cmd.Cmd):
    '''contains the entry point of the command interpreter
    which lets us control the app through commands'''

    prompt = '(hbnb)'

    __classes_names = ['BaseModel', 'User', 'Place',
                       'State', 'City', 'Amenity', 'Review']

    def emptyline(self):
        '''overriding the emptyline method.
        to disable the repetition of the last command'''
        pass

# EOF AND quit --------------------------------

    def do_EOF(self, line):
        '''The end-of-file marker,
        If a command handler returns a true value,
        the program will exit cleanly'''

        return True

    def help_EOF(self):
        '''help for EOF command'''
        print('EOF\nexit cleanly returning true')

    def do_quit(self, line):
        '''quit the console'''
        return True

    def help_quit(self):
        '''help for quit command'''
        print('quit\nquit console returning true')

# create ----------------------------------------

    def do_create(self, line):
        '''Creates a new instance of given argument type,
        saves it (to the JSON file)
        and prints the id'''

        if not line or line == '':
            print('** class name missing **')
        elif line not in self.__classes_names:
            print("** class doesn't exist **")
        else:
            line = line.split()
            new_model = eval(line[0]+'()')
            new_model.save()
            print(new_model.id)

    def help_create(self):
        '''help for create command'''
        print("""create [Model_Type]\ncreates a new instance of given
                argument type, saves it (to the JSON file)
                and prints the id""")

    def complete_create(self, text, line, begidx, endidx):
        """command completion method based on the names of the Models"""
        if not text:
            completions = HBNBCommand.__classes_names[:]
        else:
            completions = [f
                           for f in HBNBCommand.__classes_names
                           if f.startswith(text)
                           ]
        return completions

# show -------------------------------------------

    def do_show(self, line):
        '''Prints the string representation of an instance
        based on the class name and id'''
        args = line.split()
        if not line or line == '':
            print('** class name missing **')
        elif args[0] not in self.__classes_names:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:

            model_type = args[0]
            model_id = args[1]
            model_key = f"{model_type}.{model_id}"
            if model_key not in storage.all():
                print("** no instance found **")
            else:
                all_models = storage.all()
                print(str(all_models[model_key]))

    def help_show(self):
        '''help for show command'''
        print("""show [model_type] [model_id]""")
        print('Prints the string representation of an instance based on \
the model_type and model_id')

    def complete_show(self, text, line, begidx, endidx):
        """command completion method based on the names of the Models"""
        if not text:
            completions = HBNBCommand.__classes_names[:]
        else:
            completions = [f
                           for f in HBNBCommand.__classes_names
                           if f.startswith(text)
                           ]
        return completions

# destroy ----------------------------------------

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        args = line.split()
        if not line or line == '':
            print('** class name missing **')
        elif args[0] not in self.__classes_names:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")

        else:

            model_type = args[0]
            model_id = args[1]
            model_key = f"{model_type}.{model_id}"
            if model_key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[model_key]
                storage.save()

    def help_destroy(self):
        '''help for destroy method'''
        print("show [model_type] [model_id]")
        print("Deletes an instance based on model_type and model_id")

    def complete_destroy(self, text, line, begidx, endidx):
        """command completion method based on the names of the Models"""
        if not text:
            completions = HBNBCommand.__classes_names[:]
        else:
            completions = [f
                           for f in HBNBCommand.__classes_names
                           if f.startswith(text)
                           ]
        return completions

# all -------------------------------------------

    def do_all(self, line):
        '''Prints all string representation of all instances
        based or not on the class name'''

        all_models = []
        if not line or line == '':
            for model in storage.all().values():
                all_models.append(str(model))
        else:
            args = line.split()
            model_type = args[0]
            if model_type not in self.__classes_names:
                print("** class doesn't exist **")
                return
            else:

                for model in storage.all().values():
                    if isinstance(model, eval(model_type)):
                        all_models.append(str(model))
        print(all_models)

    def help_all(self):
        '''help for all method'''
        print("all [model_type]")
        print("Prints all string representation of all instances based",
              "on the model_type if passed else Prints all string",
              "representation of all instances")

    def complete_all(self, text, line, begidx, endidx):
        """command completion method based on the names of the Models"""
        if not text:
            completions = HBNBCommand.__classes_names[:]
        else:
            completions = [f
                           for f in HBNBCommand.__classes_names
                           if f.startswith(text)
                           ]
        return completions

# update -----------------------------------------

    def do_update(self, line):
        '''Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)'''
        args = line.split()

        if not line or line == '':
            print('** class name missing **')
        elif args[0] not in self.__classes_names:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")

        else:
            model_type = args[0]
            model_id = args[1]
            model_key = f"{model_type}.{model_id}"
            attribute = args[2]
            value = eval(args[3])
            if model_key not in storage.all():
                print("** no instance found **")
                return
            all_models = storage.all()
            setattr(all_models[model_key], attribute, value)
            all_models[model_key].save()

    def help_update(self):
        '''help for all method'''

        # update <class name> <id> <attribute name> "<attribute value>"
        print("all [model_type]")
        print("Updates an instance based\
            on the class name and id by adding or updating attribute")

    def complete_update(self, text, line, begidx, endidx):
        """command completion method based on the names of the Models"""
        if not text:
            completions = HBNBCommand.__classes_names[:]
        else:
            completions = [f
                           for f in HBNBCommand.__classes_names
                           if f.startswith(text)
                           ]
        return completions

# -----------------------------------------
    def default(self, line):
        """default method to handle [model].all()"""
        if line.endswith(".all()"):
            nline = line[:-6]
            # Remove the ".all()" suffix and call do_all method
            self.do_all(nline)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
