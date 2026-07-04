# Python - Decorators

def the_decorators(function):
    def inner_function():
        print("Work befor the main function execut")
        function()
        print("Work after the main function execut")
    return inner_function

@the_decorators
def my_funtion():
    print("Hello ,  World!")

my_funtion()