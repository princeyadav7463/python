# day 27
#  Docstrings in python

def square(n):
    # Takes in a number n, returns the square of n
    print(n**2)
square(5)
print(square.__doc__)  # __doc__ is used to print the docstring of the function and it is a special variable in python. It is used to store the documentation of the function. It is a string that is written in the first line of the function. It is used to explain what the function does. It is a good practice to write docstrings for all the functions. It is a good practice to write docstrings for all the functions. 

'''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''