#!/usr/bin/python3

import cmd
'''class definition that contains the entry point of the command interpreter'''


class HBNBCommand(cmd.Cmd):
    '''contains the entry point of the command interpreter
    which lets us control the system through commands'''
    prompt = '(hbnb)'


if __name__ == '__main__':
    HBNBCommand().cmdloop()
