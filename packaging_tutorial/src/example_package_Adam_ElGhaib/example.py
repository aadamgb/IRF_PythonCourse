def add_one(number):
    return number + 1


# Fibonacci numbers
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


def save_str2binary(text):
    bin = text.encode(encoding ='utf-8', errors='strict')
    with open('bin_output.bin', 'wb') as file:
        file.write(bin)


def read_binary2string(file_name):
    with open(file_name, 'r', encoding='latin1') as file:
        string = file.read()
    
    return string

