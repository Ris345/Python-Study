
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
