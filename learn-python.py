import string
from datetime import datetime
import re
from collections import Counter


def print_string_types(s):
    print(any(c.isalnum() for c in s))  # Alphanumeric
    print(any(c.isalpha() for c in s))  # Alphabet
    print(any(c.isdigit() for c in s))  # Digit
    print(any(c.islower() for c in s))  # Lowercase
    print(any(c.isupper() for c in s))  # Uppercase

# ? Split and delete the duplicate characters than print the resulted strings


def merge_the_tools(string, k):
    list_string = []
    for i in range(0, len(string) - k + 1, k):
        t = string[i:i+k]
        u = "".join(dict.fromkeys(t))
        print(u)


def print_logo():
    thickness = int(input())  # This must be an odd number
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) +
              (c * thickness).center(thickness * 6))

    # Middle Belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

    # Bottom Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) +
              (c * thickness).center(thickness * 6))

    # Bottom Cone
    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c +
              (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))


def my_print_logo():
    n = int(input())
    c = "S"
    print((c * 4).center(n))
    print((c).ljust(n))
    print((c * 4).center(n))
    print((c).rjust(n))
    print((c * 4).center(n))

# ! printing rangoli


def print_rangoli(size):
    alpha = string.ascii_lowercase
    lines = []

    # build the top half including the middle line
    for i in range(size):
        left = alpha[size-1:i:-1]   # decreasing part
        right = alpha[i:size]       # increasing part
        row = "-".join(left + right)
        lines.append(row.center(4*size - 3, "-"))

    # print top + reversed bottom
    print("\n".join(lines[-1::-1] + lines[1:]))


def validate_email(s):
    try:
        username, rest = s.split('@')
        website, extension = rest.split('.')
    except ValueError:
        return False

    if not re.fullmatch(r"[a-zA-Z0-9_-]+", username):
        return False
    elif not re.fullmatch(r"[a-zA-Z0-9]+", website):
        return False
    elif not re.fullmatch(r"[a-zA-Z]{1,3}", extension):
        return False
    else:
        return True


def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    delta = abs(int((dt1 - dt2).total_seconds()))
    return str(delta)


def counter_repeat():
    # x = int(input())
    items = list(map(int, input().split()))
    n = int(input())
    shoes = Counter(items)
    count = 0
    for i in range(n):
        shoe, amount = map(int, input().split())
        if shoe in shoes and shoes[shoe] > 0:
            shoes[shoe] -= 1
            count += amount
    print(count)
    
# todo: using the enumerate 

def enumerate_loop():
    a = ['a', 'b']
    print([(key, value) for key, value in enumerate(a)])

# todo: using try and catch in python

def divide_except():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        try:
            print(a // b)
        except Exception as e:
            print("Error Code:" , e)

# todo: how to check the validation of a regex ?
def is_valid_regex(pattern:str) -> bool:
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False
        
# todo: when you want to use sets in python
# ? you can use :
# ! intersection()
# ! difference()
# ! symmetric_difference() in either not both
# ...

# ? using the input to read the names of the students
if __name__ == '__main__':
    # n = int(input())
    # student_marks = {}
    # for _ in range(n):
    #     print("Student name space list of numbers:")
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # print("Enter the student name:")
    # query_name = input()
    # scores = student_marks[query_name]
    # # ! how to print a number in 2 places format after the decimal
    # result = sum(scores)/len(scores)
    # print(f"{result:.2f}")
    # # ! read the string
    # s = input()
    # print_string_types(s)
    # print_rangoli(10)
    # my_print_logo()
    # enumerate_loop()
    # divide_except()
    print(is_valid_regex("hello"))
