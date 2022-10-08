# import functools


# def repeat(num_times):

#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat


    


# @repeat(num_times=3)
# def greet(name):
#     print(f"Hello {name}")


# greet("Marian")



# def fibonaci(n):
#     a,b = 0, 1

#     while a < n:
#         print(a, end=" ")
#         a,b = b, a + b
#     print()


# fibonaci(1000)


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b

             
fib(1000)