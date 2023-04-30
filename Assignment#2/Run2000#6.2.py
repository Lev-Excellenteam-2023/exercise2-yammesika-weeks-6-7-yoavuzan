import time
import timeit


def timer(function, *param, **parameters):
    """
       take function and dictionary or iterable. and

               :return: print the time this function work.
               :rtype: void
       """
    exec_time = timeit.timeit(lambda: function(*param, **parameters), number=1)
    print('Execution time:', exec_time, 'milliseconds')


def main():
    """ test the function timer"""
    timer(print, "Hello")
    timer(zip, [1, 2, 3], [4, 5, 6])
    timer("Hi {name}".format, name="Bug")


if __name__ == '__main__':
    main()