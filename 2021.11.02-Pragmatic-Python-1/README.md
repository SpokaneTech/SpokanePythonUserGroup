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
## Pragmatic Python:
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
<!-- _class: lead -->
# “Pragmatic” ?

---
# Pragmatic

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
- Pair programming for ~20 minutes
- Lightning presentations for ~15-20 minutes

---
# Outline
- What is Python?
- Installing Python
- Running Python
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
- Dynamic
- Strong
- Indented
- Beginner-friendly
- Object-oriented

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
# Running Python
#### REPL
_**R**ead-**E**val-**P**rint-**L**oop_

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

---
# Craigslist CLI
- Search cars for sale
- Find lowest priced cars
- Save car images
- Search multiple Craigslist regions at once

---
# Craigslist CLI
**Search cars for sale**

```bash
$ python -m app \
    "https://spokane.craigslist.org/d/cars-trucks-by-owner/search/cto?query=montero"
mitsubishi montero XlS 2002
Montero/Pajero SR Safari roof 1998
2002 Mitsubishi Montero Sport 2002
```

---
# Craigslist CLI
**Find lowest priced cars**

```bash
$ python -m app --lowest \
    "https://spokane.craigslist.org/d/cars-trucks-by-owner/search/cto?query=montero"
2002 Mitsubishi Montero Sport is the lowest priced vehicle at $650
```

---
# Craigslist CLI
**Save car images**
```bash
$ python -m app --images --output ./out \
    "https://spokane.craigslist.org/d/cars-trucks-by-owner/search/cto?query=montero"
$ ls ./out
mitsubishi-montero-XlS-2002.jpg
Montero-Pajero-SR-Safari-roof-1998.jpg
2002-Mitsubishi-Montero-Sport-2002.jpg
```

---
# Craigslist CLI
**Search multiple Craigslist regions at once**
```bash
$ python -m app --query "montero" --locations "spokane" "seattle"
```
```text
mitsubishi montero XlS 2002
Montero/Pajero SR Safari roof 1998
2002 Mitsubishi Montero Sport 2002
2 rare Mitsubishi Monteros Gen 1
2003 Mitsu Montero Sport XLS
2002 Mitsubishi Montero Sport Mechanics Special
...
```

---
# Craigslist CLI Ideas
- Filter posts from within the last week
- Scrape data from item details page
- Calculate average price for vehicle
- Create UI using `tkinter`
- Read and parse `robots.txt`
- ...

---
# Pair Programming
Find a fellow Pythonista and tackle an improvement for the next 20 minutes.
</br>
[https://code.visualstudio.com/learn/collaboration/live-share](https://code.visualstudio.com/learn/collaboration/live-share)

---
# Lightning Presentations
Showcase the improvement you and your buddy made!

---
<style scoped>
ul { columns: 2; }
ul ul { columns: 1; }
</style>

# Learning Resources

- Blogs
  - [Official Docs](https://docs.python.org/3/)
  - **[Spokane Python](https://spokanepython.com)**
  - [https://realpython.com/](https://realpython.com/)
  - [https://www.fullstackpython.com/](https://www.fullstackpython.com/)
- Books
  - [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
  - [Python Cookbook](https://www.oreilly.com/library/view/python-cookbook-3rd/9781449357337/)
  - [Fluent Python](https://www.oreilly.com/library/view/fluent-python/9781491946237/)
- Conferences (watch previous years!)
  - [PyCon](https://us.pycon.org/2022/)
  - [PyCascades](https://2021.pycascades.com/)

---
<!-- _class: lead -->
Thank you for coming! Join us next time for
## Pragmatic Python:
# Journey to the **_Pythonic Peak_**
