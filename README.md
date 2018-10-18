# n-queens
Solution for the n-queens problem

[![Build Status](https://travis-ci.org/Linkstrange/n-queens.svg?branch=master)](https://travis-ci.org/Linkstrange/n-queens)

## Setup
Run solutions.sql script included under postgres folder to setup the database. The solver will try to connect to a database called nQueens with the user postgres and no password on localhost:5432, so it is recommended to create a database with those characteristics first.

The setup will be easier on future releases, by allowing the use of configuration files. 

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