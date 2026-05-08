def greet(func):
    def wrapper(*args, **kwargs):
        print("welcome")
        r = func(*args, **kwargs)
        print(r)
        print("Thanks")
    return wrapper


@greet
def add(a, b):
    x = a + b
    return x

add(4,7)