a = 5
print(type(a))

a = 5.0
print(type(a))

a = "5"
print(type(a))

print(type(print))

def func(a):
    return(a * 5)

print(type(func))


print(func(5))
print(func("Hello "))
print(func("Na") + " Batman!")

## BASIC DATA TYPES
# Dictionaries
my_dict = {"key": 1.0, "x": "this is a string"}
print(my_dict["key"])
print(my_dict["x"])
my_dict["x"] = 2.0
print(my_dict["x"])




a = "Hello"

a.upper()
print(a)

b = a.upper()
print(a, b)


a = [3, 2, 1]
b = a
print(id(a), id(b))
b.sort()
print(a)


def func(x=[]):
    x.append("world!")
    print(x)

a = ["Hello "]
func(a)
func(a)

func()
func()


def func(x=None):
    if x is None:
        x = []
        x.append("h")
        print(x)


func()
func()
func()


def func(*args, **kwargs):
    print(args)
    print(kwargs)

a = (1, 2, 3)
func(*a)

b = {"hello": None}
func(**b)


## Decorators can be used to track the execution time of a function
d = {"a": 3.14, "b": 42, "cc": 1}

print("hello")
for c in d:
    print(c)

for item in d.items():
    print(f"{item[0]} = {item[1]}")

for key, value in d.items():
    print(f"{key}={value}")



def my_iter(num):
    c = num
    for ind in range(num - 1, 0, -1):
        c *= ind
        yield c
 
for x in my_iter(10):
    print(x)
 
print(type(my_iter(100)))

g = my_iter(10)
x = next(g)
print(f"{x=}")
x = next(g)