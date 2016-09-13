from hw0_soln import *

def test_reverse_string():
	assert reverse_string("") == ""
	assert reverse_string("hello") == "olleh"

def test_sign_flipper():
	assert sign_flipper([1, -2, 3]) == [-1,2,-3]

def test_fibonacci0():
	assert fibonacci(0) == 1

def test_fibonacci1():
	assert fibonacci(1) == 1

def test_fibonacci2():
	assert fibonacci(1) == 2

def test_fibonacci20():
	assert fibonacci(20) == 6765