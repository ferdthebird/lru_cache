# lru_cache
python implementation of an lru style cache
This code implements a least recently used cache and a shell to excersize it.  The cache is a key/value store and treats both keys and values as strings.  The separator used by the command parser is the space character so multi-word strings and keys are not allowed.  

Installation: 

No installation or compilation is required. Simply create a directory, save the codetest.tgz file there and then untar the files. To execute, just run the repl.py file.  The code is standard Python 2.7 and only depends on standard modules.  It is possible that the env program lives somewhere else on your computer.  If it is unable to be located you can directly execute the program with python repl.py.

The program is largely self-documenting.  Type ? or help to see supported commands when the program is running.

This was the initial problem specification:

Design and implement an LRU (Least Recently Used) cache. This is a cache with fixed size in terms of the number of items it holds (supplied at instantiation).  For this exercise, we won’t worry about the number of bytes. Your program can treat the keys and values as strings.  You don’t need to support keys or values that contain spaces.  The cache must allow client code to get items from the cache and set items to the cache. Once the cache is full, when the client wants to store a new item in the cache, an old item must be overwritten or
removed to make room. The item we will remove is the Least Recently Used (LRU) item.  Note that your cache does not need persistence across sessions.

Please read input from stdin and print output to stdout and support the following format (you don't need to print any kind of prompt character).
All inputs and outputs exist on their own line:

The first input line should set the max number of items for the cache using the keyword SIZE.  The program should respond with ‘SIZE OK’. This must only occur as the first operation.

Set items with a line giving the key and value, separated by a space, 
your program should respond with 'SET OK'.

Get items with a line giving the key requested, your program should respond with the previously stored value, for example “GOT foo”. If the the key is not in the cache, it should reply with “NOTFOUND”.

‘EXIT’ should cause your program to exit.

If the input is invalid, your program should respond with ‘ERROR’

Sample Input
SIZE 3
GET foo
SET foo 1
GET foo
SET foo 1.1
GET foo
SET spam 2
GET spam
SET ham third
SET parrot four
GET foo
GET spam
GET ham
GET ham parrot
GET parrot
EXIT

Expected Output
SIZE OK
NOTFOUND
SET OK
GOT 1
SET OK
GOT 1.1
SET OK
GOT 2
SET OK
SET OK
NOTFOUND
GOT 2
GOT third
ERROR
GOT four

