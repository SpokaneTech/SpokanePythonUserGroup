---
title: "Pragmatic Python: Welcome to the Jungle"
marp: true
html: true
theme: gaia

---
<style>
p, pre {
    margin-top: 8px !important;
}
</style>
<style scoped>
h1 {
    font-size: 2.4rem;
}
h2 {
    font-size: 2rem;
}
</style>

<!-- _class: lead -->
## Pragmatic Python
# Welcome to the Jungle
_November 2, 2021_
Joe Riddle

---
<!-- _class: lead -->
# Hi, I'm Joe Riddle 👋

---
# Previous meetup recordings now available
https://spokanepython.com

[IntelliTect YouTube](https://www.youtube.com/channel/UCZSEfrUQnLLohBWDKRRSohw)

---
# “Pragmatic” ?

> of or relating to a practical point of view or practical considerations.

\- dictionary.com

> relating to matters of fact or practical affairs often to the exclusion of intellectual or artistic matters : practical as opposed to idealistic.

\- merriam-webster.com

---
# Pragmatic
> dealing with things sensibly and realistically in a way that is based on practical rather than theoretical considerations.

\- Oxford Languages

---
# Goal
Teach user group members practical skills to create, manage, and host their own Python project.

---
# Series Outline
- 5-6 meetups
- Later topics may include:
  - Managing Python dependencies
  - Publishing Python packages
  - Running Python projects in "prod"
  - Testing and linting
  - Intro to machine learning
  - Django

---
# Today's Format
- Talk / live code for ~60 minutes
- Pair program for ~30 minutes
- Lightning presentations for ~15-20 minutes

---
# Outline
- What is Python?
- Installing Python
- Editing Python
- Anatomy of a **module**
- Anatomy of a **package**
- Using the standard library
- Using common packages

---
# Live Coding Example
Craigslist CLI tool
- Search cars for sale
- Find lowest priced cars
- Save car images
- Search multiple Craigslist regions at once

---
# What is Python?

- Interpreted
- Object-oriented
- Dynamic
- Strong
- Indented
- Beginner-friendly

---
# Python 2 or 3?

#### Answer: 3

Python 2 has been [sunset](https://www.python.org/doc/sunset-python-2/).

In 2021, this is a non-issue.

---
# Installing Python
#### Windows
[https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/) _or_
```powershell
>choco install python
```

#### Linux
```bash
$ sudo apt-get update
$ sudo apt-get install python
```

---
# Installing Python (cont'd)
#### Mac OS X

[https://opensource.com/article/19/5/python-3-default-mac](https://opensource.com/article/19/5/python-3-default-mac)

tl;dr: use `pyenv` or Homebrew. **Don't use the built-in Python.**

---
# Editing Python
#### IDLE
_**I**ntegrated **D**evelopment and **L**earning **E**nvironment_
Python-specific

#### IDE
_**I**ntegrated **D**evelopment **E**nvironment_
[VS Code](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/)

---
# What is a **Module**?

> A module is a file containing Python definitions and statements. 

https://docs.python.org/3/tutorial/modules.html


---
# Anatomy of a **Module**

`script.py`
```python
import sys                  # <-- importing a package

def main():                 # <-- function declaration
    car = sys.argv[1]
    print(f"Your favorite car is a {car}!")  # <-- an "f-string"

if __name__ == "__main__":  # <-- only execute if run as the entry point
    main()                  # <-- calling a function
```

```bash
$ python script.py "Mitsubishi Montero Sport"    # <-- running a python module
Your favorite car is a Mitsubishi Montero Sport!
```

---
# What is a **Package**?

> Packages are a way of structuring Python’s module namespace by using “dotted module names”.

https://docs.python.org/3/tutorial/modules.html#packages
</br>

---
# Anatomy of a **Package**
```text
app/
  ├── __init__.py
  ├── __main__.py
  └── app.py
```
`__init__.py`
```python
# marks directory as a python package
```

`__main__.py`
```python
# executed when the package itself is invoked using -m 
from .app import run

if __name__ == "__main__":
    run()
```

---
# Anatomy of a **Package** (cont'd)
`app.py`
```python
import sys

def main():
    car = sys.argv[1]
    print(f"Your least favorite car is a {car}!")
```

```bash
$ python -m app "Chrysler PT Cruiser"
Your least favorite car is a Chrysler PT Cruiser!
```