# content of test_sample.py
from Block import *
block=Block()
def func(x):
    return x + 1
def rei(a):
    return a+1
def test_answer():
    assert func(3) == 5
def test_ans():
    assert rei(3) == 4
