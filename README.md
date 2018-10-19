# n-queens
Solution for the n-queens problem: https://en.wikipedia.org/wiki/Eight_queens_puzzle

[![Build Status](https://travis-ci.org/Linkstrange/n-queens.svg?branch=master)](https://travis-ci.org/Linkstrange/n-queens)

## Setup
No needed setup if you want to use the public database specified in the config.ini file

If you want to setup your own database, run solutions.sql script included under postgres folder to setup the tables needed. You will need to specify the details of your database in the config.ini file

## Running

Installing dependencies
```python
pip install -r requirements.txt
```

Running the solver for n=8
```python
python main.py 8
```

## Sample output
The output will be a text representation for all found solutions, also the elapsed time it took to found those solutions.
```
...
_|_|_|Q|_|_|_|_|
_|Q|_|_|_|_|_|_|
_|_|_|_|_|_|Q|_|
_|_|Q|_|_|_|_|_|
_|_|_|_|_|Q|_|_|
_|_|_|_|_|_|_|Q|
_|_|_|_|Q|_|_|_|
Q|_|_|_|_|_|_|_|
----------------
_|_|_|_|Q|_|_|_|
_|Q|_|_|_|_|_|_|
_|_|_|Q|_|_|_|_|
_|_|_|_|_|_|Q|_|
_|_|Q|_|_|_|_|_|
_|_|_|_|_|_|_|Q|
_|_|_|_|_|Q|_|_|
Q|_|_|_|_|_|_|_|
----------------
_|_|Q|_|_|_|_|_|
_|_|_|_|Q|_|_|_|
_|Q|_|_|_|_|_|_|
_|_|_|_|_|_|_|Q|
_|_|_|_|_|Q|_|_|
_|_|_|Q|_|_|_|_|
_|_|_|_|_|_|Q|_|
Q|_|_|_|_|_|_|_|
----------------
_|_|Q|_|_|_|_|_|
_|_|_|_|_|Q|_|_|
_|_|_|Q|_|_|_|_|
_|Q|_|_|_|_|_|_|
_|_|_|_|_|_|_|Q|
_|_|_|_|Q|_|_|_|
_|_|_|_|_|_|Q|_|
Q|_|_|_|_|_|_|_|
Elapsed time 0.10774741803178553 seconds
```
