# from: https://www.youtube.com/watch?v=N4mEzFDjqtA&t=17s
import random 
import sys
import os

print("Hellow World")
# comment
'''
comment
'''
name = "Bruno"
print(name)

# Non trivial operators: % (module), ** (exponation), // (converts to int (returns only the int value))
print("test")
print('test')
print('"test"')
print("'test'")

multi_line_quote = '''first line
second line '''
print(multi_line_quote)
another = 'another line'
print(multi_line_quote + another)
concat_str = "test" + " another"
print(concat_str)
using_comma_get_tuple = "test", " another", "yey"
type(using_comma_get_tuple)
print(using_comma_get_tuple[0])

print('\n' * 5)
print("I don't like ", end=" aa ") #won't break line
print("again")

print(name, another)
print(name + another)

a = 3
if a == 2 :
    print("a=", 2)
elif a == 1 :
    print("a=", 1)
else:
    print("a not 1 nor 2")

for x in range(0, 10):
    print(x)

# print in the same line
for x in range(0, 10):
    print(x, ', ', end="")
