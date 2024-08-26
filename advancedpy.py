#converting a python dictionary to json
import json
person = {
    "name": "Vee",
    "Age": 26,
    "status": "single",
    "has kids": False,
    "is rich": True
}
pjson = json.dumps(person, indent=2, sort_keys=True)
print(pjson)
''' returns a json object{
  "Age": 26,
  "has kids": false,
  "is rich": true,
  "name": "Vee",
  "status": "single"
}
'''
#to dump it into a file name person.json
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

#converting/decoding from json to python dictionary
person = json.loads(pjson)
print(person)
#decode from a file
with open('person.json', 'r') as file:
    person =json.load(file)
    print(person)


#Encoding from  a class
import json


class User:

    def __int__(self, name, age):
        self.name = name
        self.age = age

user = ('vee', 26)
def encode_class(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True }
    else:
        raise TypeError


userjson = json.dumps(user, default=encode_class )
print(userjson)
print(type(userjson)) #returns <class 'str'>


#To decode back to python
userr = json.loads(userjson)
print(userr)
print(type(userr)) #returns <class 'list'>

#RANDOM NUMBERS
#Random module
#random.random returns a random float between 0 and 1
import random
a = random.random()
print(a)

#specifying range
b = random.uniform(1, 10)
print(b)

#random integers
c = random.randint(1, 10) #includes the upper range. randrange() excludes it
print(c)

#working with lists
my_list = list("ABCDEFGH")
print(my_list) #returns ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

f = random.choice(my_list)
print(f) #random element from the list

g = random.sample(my_list, 3)
print(g) #three unique elementts without repetition

h = random.choices(my_list, k=3) #can pick elements multiple times
print(h) #['C', 'C', 'D']

random.shuffle(my_list) #shuffles randomly
print(my_list #['B', 'E', 'H', 'F', 'C', 'D', 'A', 'G']
      
import random
#reproducing data with random seed()

random.seed(1)
print(random.random())
print(random.randint(1, 10)) #retuns 0.13436424411240122 and 2

random.seed(1)
print(random.random())
print(random.randint(1, 10)) #returns 0.13436424411240122 and 2

random.seed(2)
print(random.random())
print(random.randint(1, 10)) #returns 0.9560342718892494 and 1

random.seed(2)
print(random.random())
print(random.randint(1, 10)) # returns 0.9560342718892494 and 1

#secrets module
import secrets
a = secrets.randbelow(10)
print(a) #integer from 0-10 excluding 10

#integer of specified bits
b = secrets.randbits(4)
print(b) #0-15

#working with lists
mylist = ("ABCDEFG")
a = secrets.choice(mylist)
print(a) #random unique element

a = np.random.rand(3)
print(a) #returns an array [0.97382899 0.45129313 0.80798121]

b = np.random.rand(3,3)
print(b) #returns a 3 by 3 array

c = np.random.randint(0, 10, 3)
print(c) #returns a 3 elements array from 0-9

d = np.random.randint(0, 10, (3,4))
print(d) #returns a 3d array with 4 elements

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
np.random.shuffle(arr)
print(arr) """returns.only shuffles one first axis
[[1 2 3]
 [7 8 9]
 [4 5 6]]"""



#Basic function decorator
def my_decorator(func):
    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper


@my_decorator
def print_name():
    print('Vee')

#print_name = my_decorator(print_name)

print_name()


#A class decorator that tracks how many times a function is executed
class Countcalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is excecuted {self.num_calls} times' )
        return self.func(*args, **kwargs)

@Countcalls
def say_hello():
    print('Hello there')

say_hello()
say_hello()

#A class decorator that tracks how many times a function is executed
class Countcalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is excecuted {self.num_calls} times' )
        return self.func(*args, **kwargs)

@Countcalls
def say_hello():
    print('Hello there')

say_hello()
say_hello()

#Generators
def my_generator():
    yield 1
    yield 2
    yield 3


g = my_generator()
# To print all the values
for i in g:
   # print(i) #retuns 1,2,3

    # To print values one by one
    value = next(g)
    print(value) #prints 1

    value = next(g) #prints 2
    print(value)

    value = next(g) #prints 3
    print(value)
    
def my_generator():
    yield 2
    yield 1
    yield 3


g = my_generator()

print(sum(g)) #sums the value,6
print(sorted(g)) #sorts in order, 123

#Excecution of generator
def countdown(num):
    print('start')
    while num > 0:
        yield num
        num -= 1


cd = countdown(4)

value = next(cd)
print(value)

print(next(cd))
print(next(cd))
print(next(cd))

#fibonacci sequence using generator
def fibonacci(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b, a + b
        a += 1

fib = fibonacci(30)
for i in fib:
    print(i)


#Generato expressions
mygenerator = (i for i in range(10) if i % 2 == 0)
for i in mygenerator:
    print(i)


#multiprocessing
from multiprocessing import process
import os
import time

def squares():
    for i in range(100):
        i * i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()

#create the process
for i in range(num_processes):
    p = process (target=squares)
    processes.append(p)

#start
for p in processes:
    p.start()

for p in processes:
    p.join()

print('end main')





import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    used_letters = set()  # letters that the user has guessed
    alphabet = set(string.ascii_uppercase)

    # getting user input
    user_letter = input('Enter a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You have already used that letter. Try again')
    else:
        print('invalid character')


    print()


























