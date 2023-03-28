
#  1.stuttering function
#  level super easy
# test cases stutter("incredible") ➞ "in... in... incredible?"
import math
from math import pi


def stutter(word):
    #  break down the string
    # get the vlaues from the first two indexes 0, 1
    #  concatenate .... with the first two indexes twice
    #  and finally add the word incredible + ? at the end
    #  return the answer as a string
    firstTwoletters = word[:2]
    return (firstTwoletters + '...' + firstTwoletters + '...' + word + '?')

# print(stutter("incredible"))
# print(stutter("enthusiastic"))
# print(stutter("outstanding"))


# 2 . discount function
# easy level
#  test case dis(1500, 50) ➞ 750
def dis(price, discount):
    #  we need to get the amount after the discount
    calc = discount / 100 * price
    return round(calc)


# print(dis(1500, 50))
# print(dis(89, 20))
# print(dis(100, 75))


# 3.
def addition(num):
    return num + 1

# print(addition(60))


# 4.

def radians_to_degrees(rad):
    degrees = rad * 180/pi
    #  print(round(degrees))

# radians_to_degrees(1)
# radians_to_degrees(20)
# radians_to_degrees(50)

# 5

def circle_or_square(rad, area):
    # find circumfrence of the circle
    # find the perimeter of the square
    # if circle > square return TRUE
    # else FALSE

    cirumference = 2 * pi * rad
    perimeter = math.sqrt(area) * 4
    if cirumference > perimeter:
        return True
    else:
        return False

# print(circle_or_square(16, 625))
# print(circle_or_square(5, 100))
# print(circle_or_square(8, 144))


# 6 Curzon Numbers
def is_curzon(num):
    # n ** num + 1 = someNum1
    # n * num + 1 = someNum2
    # if someNum % someNum2  == 0 return true
    #  else return false

    checkOne = 2 ** num + 1
    checkTwo = 2 * num + 1
    if checkOne % checkTwo == 0:
        return True
    else:
        return False

# print(is_curzon(5))
# print(is_curzon(10))
# print(is_curzon(14))


# 7 Luke, I Am Your ...
#  trying to use somehthing other than if/else statements

def relation_to_luke(name):
    family = {
        'Darth Vader': 'Father',
        'Leia': 'sister',
        'Han': 'brother in law',
        'R2D2': 'droid'
    }



# relation_to_luke('luke')



# def starts_with_A(s):
#     if s[0] == 'A':
#         return s
#     else:
#         return None

# fruit = ['Apple', 'Banana', 'Pear', 'Apricot', 'Orange']
# map_object = map(starts_with_A, fruit)
# # print(list(map_object))


# # map_item = map(lambda s: s[0] == 'A', fruit)
# # print(list(map_item))


# # def make_A_small(z):
# #     return z[0].lower()
    
items = ['Sabian' , 'HHX' , 'Ludwig' , 'Pearl']
# # map_items = map(make_A_small, items)
# # print(list(map_items))    


map_items = list(map(str.upper, items))
# print(map_items)
                       
# map_other = map(lambda z:  z[0].lower, items )
# print(list(map_other))



import re 
s = 'hello world'
match = re.search(r'hello.', s)
# print(match)

import re
txt = "The rain in Spain"
x = re.findall("ai",txt)
y = re.findall("Portugal",txt)
# print(x)
# print(y)


# x = re.search("\s",txt)
# y = re.search("Portugal",txt)
# print("The first white-space character is located in position:", x.start())
# print(y)


# x = re.split("\s",txt)
# y = re.split("\s",txt,1)

# print(x)
# print(y)


x = re.sub("\s","9", txt)
y = re.sub("\s","9", txt,1)

# print(x)
# print(y)



#  understanding lambda 

# def square():
#     return n ** 2

# square = lambda n: n ** 2 
# # print(square(2))




# maxi = lambda x, y: x if x > y else y
# print(maxi(4,6))


# def starts_with_word(x):
#     return x[0] == 'A'

# fruits = ['Apricot', 'Apple', 'Aqua' , 'Banana', 'Pear', 'Peach']
# map_obj = map(starts_with_word, fruits)
# # print(list(map_obj))

# map_objc = map(lambda x: x[0] == 'A', fruits)
# # print(list(map_obj))


def starts_with(s):
    return s[0] == 'O'
fruit = ['Apple', 'Banana', 'Pear', 'Apricot', 'Orange']
filt_obj = filter(starts_with, fruit)
# print(list(filt_obj))

filter_objs = filter(lambda x: x[0] == 'B', fruit)

# print(list(filter_objs))

from functools import reduce 

def add(x,y):
    return x + y

liste = [10,15,20,10]

# print(reduce(add, list))


print(reduce(lambda x,y: x + y, liste))















































