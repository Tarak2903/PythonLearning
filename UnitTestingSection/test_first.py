
def setup_module(module):
    print("Starting the module")

def teardown_module(module):
    print("Ending the module")

def setup_functin(function):

    print(f"\nStarting the function setup for {function.__name__}")

def teardown_function(function):
    print(f"\nEnding the function setup for {function.__name__}")


def test_one_check():
    assert 1==1

def test_two_check():
    assert 2==2
