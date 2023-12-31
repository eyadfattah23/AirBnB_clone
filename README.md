# AirBnB_clone

## Project description:

This project is a clone of AirBnB web application built from scratch and will call it HBNB

### **first** start by building the console, Base class and methods, and a cmd

-- > the console is the entry point of the command interpreter

which will be used to manage our AirBnB objects

> This is the first step towards building our first full web application: **_"the AirBnB clone"_**. This first step is very important because we will use what we build during this step with all other following steps: HTML/CSS templating, database storage, API, front-end integration…

#### Each task/code is linked and will help us to:

> put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of our future instances.

> create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.

> create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.

> create the first abstracted storage engine of the project: File storage.

> create all unittests to validate all our classes and storage engine.

## the command interpreter description:

### It's just like the shell but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

> Create a new object (ex: a new User or a new Place)

> Retrieve an object from a file, a database etc…

> Do operations on objects (count, compute stats, etc…)

> Update attributes of an object

> Destroy an object

### To create a command interpreter in Python using the `cmd` module, you can follow these steps:

> 1. Import the necessary module:

```python
import cmd
```

> 2.  Create a class that inherits from `cmd.Cmd`:

```python
class MyCmd(cmd.Cmd):
    pass
```

> 3.  Override the `do_<command>` methods to define the commands you want to support:

```python
class MyCmd(cmd.Cmd):
    def do_greet(self, line):
        print("Hello!")

    def do_quit(self, line):
        return True
```

> 4.  Optionally, provide a prompt for the command interpreter:

```python
class MyCmd(cmd.Cmd):
    prompt = ">>> "

    def do_greet(self, line):
        print("Hello!")

    def do_quit(self, line):
        return True
```

> 5.  Create an instance of your command interpreter class and call the `cmdloop()` method to start the command loop:

```python
if __name__ == "__main__":
    MyCmd().cmdloop()
```

Here's an example that puts all the steps together:

```python
import cmd

class MyCmd(cmd.Cmd):
    prompt = ">>> "

    def do_greet(self, line):
        print("Hello!")

    def do_quit(self, line):
        return True

if __name__ == "__main__":
    MyCmd().cmdloop()
```

When you run this script, it will start the command interpreter and display the prompt ">>>". You can enter commands like "greet" or "quit" to interact with the command interpreter.

---

### reload method explanation:

    '''
    1--> we got a dictionary like this from 'file.json':
            {"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {
                "my_number": 89,
                "__class__": "BaseModel",
                "updated_at": "2017-09-28T21:07:25.047381",
                "created_at": "2017-09-28T21:07:25.047372",
                "name": "My_First_Model",
                "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
    2--> we go over the dictionary
        with key ="BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d"
        and value = {
                "my_number": 89,
                "__class__": "BaseModel",
                "updated_at": "2017-09-28T21:07:25.047381",
                "created_at": "2017-09-28T21:07:25.047372",
                "name": "My_First_Model",
                "id": "ee49c413-023a-4b49-bd28-f2936c95460d
    			}
    3--> create instances using value as kwargs
        and add those instances
        using the right format to __objects
    '''

---

## front-end:

### resources:

> [Learn to Code HTML & CSS](https://intranet.alxswe.com/rltoken/T9KyiA6_Tm3Ny6oTn08S-A)

> [advanced selectors](https://learn.shayhowe.com/advanced-html-css/complex-selectors/)

> **Code Validation and helping links**: [HTML](http://validator.w3.org/) and [CSS](http://jigsaw.w3.org/css-validator/)

the most popular resets is [Eric Meyer’s reset](http://meyerweb.com/eric/tools/css/reset/), which has been adapted to include styles for the new HTML5 elements.

[Copy Paste Character.](http://copypastecharacter.com/)

### NOTES:

![1->](images/image.png)

> **2-> All HTML documents have a required structure that includes the following declaration and elements:** \<!DOCTYPE html>, \<html>, \<head>, and \<body>.

```HTML
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Hello World</title>
  </head>
  <body>
    <h1>Hello World</h1>
    <p>This is a web page.</p>
  </body>
</html>
```

> **3-> Self-Closing Elements:** > \<br>
> \<embed>
> \<hr>
> \<img>
> \<input>
> \<link>
> \<meta>
> \<param>
> \<source>
> \<wbr>

![4->](images/image-1.png)

> **5->** HTML comments start with `\<!-- and end with -->`. CSS comments start with \/\* and end with \*\/.

> **6->** the total width of an element can be calculated using the following formula:
>
> > margin-right + border-right + padding-right + width + padding-left + border-left + margin-left

> **7->**the total height of an element can be calculated using the following formula:
>
> > margin-top + border-top + padding-top + height + padding-bottom + border-bottom + margin-bottom

![8->](images/image2.png)

> 9-> "`margin: 30px 12px 4px;`" is valid

> 10-> "` <img src="logo.png" />`" is valid (remove or keep the /)
