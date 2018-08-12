from timeit import Timer

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

"""
Let’s look at four different ways we might generate a list of n numbers starting with 0.
    - First we’ll try a for loop and create the list by concatenation
    - Then we’ll use append rather than concatenation
    - Then we’ll try creating the list using list comprehension and finally, and perhaps the most obvious way, using the range function wrapped by a call to the list constructor.

To capture the time it takes for each of our functions to execute we will use Python’s timeit module.
    To use timeit you create a Timer object whose parameters are two Python statements. 
        - The first parameter is a Python statement that you want to time
        - the second parameter is a statement that will run once to set up the test.

    The timeit module will then time how long it takes to execute the statement some number of times. By default timeit will try to run the statement one million times. When its done it returns the time as a floating point value representing the total number of seconds. However, since it executes the statement a million times you can read the result as the number of microseconds to execute the test one time. You can also pass timeit a named parameter called number that allows you to specify how many times the test statement is executed.

    The statement from __main__ import test1 imports the function test1 from the __main__ namespace into the namespace that timeit sets up for the timing experiment.
"""

t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")

"""
output : 
$ python3 2.6.1\ Listing\ 3.py
concat  1.5894567949999328 milliseconds
append  0.09528493700054241 milliseconds
comprehension  0.03817194399925938 milliseconds
list range  0.01669329799915431 milliseconds

- From the experiment above it is clear that the append operation at 0.30 milliseconds is much faster than concatenation at 6.54 milliseconds.
"""