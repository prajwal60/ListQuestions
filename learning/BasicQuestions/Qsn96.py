# Write a Python program to print the current call stack.
import traceback
def a1():
    return abc()
def abc():
    traceback.print_stack()
a1()