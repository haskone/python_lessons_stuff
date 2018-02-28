import pytest

# do 3 different test for each argument
@pytest.mark.parametrize("some_arg", [1, 2, 3])
def test_the_same(some_arg):    
    assert some_arg > 0

# kind of stub, it's used in the in test_1_that_needs_resource_a
@pytest.fixture()
def resource_a():
    print('\nresources_a() "setup"')

def test_1_that_needs_resource_a(resource_a):
    print('test_1_that_needs_resource_a()')

# initializations and post clean methods
def resource_a_setup():
    print('resources_a_setup()')

def resource_a_teardown():
    print('resources_a_teardown()')

def setup_module(module):
    print('\nsetup_module()')
    resource_a_setup()

def teardown_module(module):
    print('\nteardown_module()')
    resource_a_teardown()


#############################################
################## one func and 2 test for it
def func(x, y):
    return int(x / y) + 1

def test_answer():
    result = func(10, 2)
    assert result == 6, "weird value"
    assert isinstance(result, int)

def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        func(10, 0)