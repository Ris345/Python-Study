
# #  1.stuttering function
# #  level super easy
# # test cases stutter("incredible") ➞ "in... in... incredible?"
# from functools import reduce
# import re
# import math
# from math import pi


# def stutter(word):
#     #  break down the string
#     # get the vlaues from the first two indexes 0, 1
#     #  concatenate .... with the first two indexes twice
#     #  and finally add the word incredible + ? at the end
#     #  return the answer as a string
#     firstTwoletters = word[:2]
#     return (firstTwoletters + '...' + firstTwoletters + '...' + word + '?')

# # print(stutter("incredible"))
# # print(stutter("enthusiastic"))
# # print(stutter("outstanding"))


# # 2 . discount function
# # easy level
# #  test case dis(1500, 50) ➞ 750
# def dis(price, discount):
#     #  we need to get the amount after the discount
#     calc = discount / 100 * price
#     return round(calc)


# # print(dis(1500, 50))
# # print(dis(89, 20))
# # print(dis(100, 75))


# # 3.
# def addition(num):
#     return num + 1

# # print(addition(60))


# # 4.

# def radians_to_degrees(rad):
#     degrees = rad * 180/pi
#     #  print(round(degrees))

# # radians_to_degrees(1)
# # radians_to_degrees(20)
# # radians_to_degrees(50)

# # 5


# def circle_or_square(rad, area):
#     # find circumfrence of the circle
#     # find the perimeter of the square
#     # if circle > square return TRUE
#     # else FALSE

#     cirumference = 2 * pi * rad
#     perimeter = math.sqrt(area) * 4
#     if cirumference > perimeter:
#         return True
#     else:
#         return False

# # print(circle_or_square(16, 625))
# # print(circle_or_square(5, 100))
# # print(circle_or_square(8, 144))


# # 6 Curzon Numbers
# def is_curzon(num):
#     # n ** num + 1 = someNum1
#     # n * num + 1 = someNum2
#     # if someNum % someNum2  == 0 return true
#     #  else return false

#     checkOne = 2 ** num + 1
#     checkTwo = 2 * num + 1
#     if checkOne % checkTwo == 0:
#         return True
#     else:
#         return False

# # print(is_curzon(5))
# # print(is_curzon(10))
# # print(is_curzon(14))


# # 7 Luke, I Am Your ...
# #  trying to use somehthing other than if/else statements

# def relation_to_luke(name):
#     family = {
#         'Darth Vader': 'Father',
#         'Leia': 'sister',
#         'Han': 'brother in law',
#         'R2D2': 'droid'
#     }


# # relation_to_luke('luke')


# # def starts_with_A(s):
# #     if s[0] == 'A':
# #         return s
# #     else:
# #         return None

# # fruit = ['Apple', 'Banana', 'Pear', 'Apricot', 'Orange']
# # map_object = map(starts_with_A, fruit)
# # # print(list(map_object))


# # # map_item = map(lambda s: s[0] == 'A', fruit)
# # # print(list(map_item))


# # # def make_A_small(z):
# # #     return z[0].lower()
# items = ['Sabian', 'HHX', 'Ludwig', 'Pearl']
# # # map_items = map(make_A_small, items)
# # # print(list(map_items))


# map_items = list(map(str.upper, items))
# # print(map_items)

# # map_other = map(lambda z:  z[0].lower, items )
# # print(list(map_other))


# s = 'hello world'
# match = re.search(r'hello.', s)
# # print(match)

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# y = re.findall("Portugal", txt)
# # print(x)
# # print(y)


# # x = re.search("\s",txt)
# # y = re.search("Portugal",txt)
# # print("The first white-space character is located in position:", x.start())
# # print(y)


# # x = re.split("\s",txt)
# # y = re.split("\s",txt,1)

# # print(x)
# # print(y)


# x = re.sub("\s", "9", txt)
# y = re.sub("\s", "9", txt, 1)

# # print(x)
# # print(y)


# #  understanding lambda

# # def square():
# #     return n ** 2

# # square = lambda n: n ** 2
# # # print(square(2))


# # maxi = lambda x, y: x if x > y else y
# # print(maxi(4,6))


# # def starts_with_word(x):
# #     return x[0] == 'A'

# # fruits = ['Apricot', 'Apple', 'Aqua' , 'Banana', 'Pear', 'Peach']
# # map_obj = map(starts_with_word, fruits)
# # # print(list(map_obj))

# # map_objc = map(lambda x: x[0] == 'A', fruits)
# # # print(list(map_obj))


# def starts_with(s):
#     return s[0] == 'O'


# fruit = ['Apple', 'Banana', 'Pear', 'Apricot', 'Orange']
# filt_obj = filter(starts_with, fruit)
# # print(list(filt_obj))

# filter_objs = filter(lambda x: x[0] == 'B', fruit)

# # print(list(filter_objs))


# def add(x, y):
#     return x + y


# liste = [10, 15, 20, 10]

# # print(reduce(add, list))


# # print(reduce(lambda x,y: x + y, liste))


# #  7 convert(5) ➞ 300

# def convert(minutes):
#     return minutes * 60

# # print(convert(5))
# # print(convert(3))
# # print(convert(2))


# # 8.

# def tri_area(base, height):
#     return round(base * height / 2)
# # print(tri_area(3, 2))
# # print(tri_area(7, 4))
# # print(tri_area(10, 10))


# # 9.

# def cubes(a):
#     return a ** 3
# # print(cubes(3))
# # print(cubes(4))
# # print(cubes(5))


# # 10

# def football_points(wins, draws, losses):
#     return wins * 3 + draws * 1 + losses * 0

# print(football_points(3, 4, 2))
# print(football_points(5, 0, 2))
# print(football_points(0, 0, 1))


# test case ---->lottery([["YYW", 70], ["WXK", 65], ["RPDI", 88]], 2)
# ➞ "Loser!"

#  step 1 the nested lists should have a character match in the sublist ---> if "WXK" --> should match 65 --> win, if all the wins is greater than the win number then it is a win other wise it's a loss

#  step 2

# def lottery(ticket, win):
#     newList = []
#     miniWin = 0
#     # run a for loop iterate through each item
#     for t in ticket:
#         character = (t[0])
#         ticketNum = (t[1])
#         print(t[1])
#         for c in character:
#             print(c)
#         # mini win
#         if character == ticketNum:
#             miniWin += 1
#         else:
#             miniWin = 0
#         # bigger win
#         if miniWin > win:
#             return 'Winner!'
#         else:
#             return 'Looser!'

# print(lottery([["YYW", 70], ["WXK", 65], ["RPDI", 88]], 2))
# print(lottery([["KG", 80], ["NTBBVZ", 79], ["CI", 73],
#       ["AGXMEE", 74], ["IU", 68], ["VOSP", 84]], 1))
# print(lottery([["ZSAMZB", 81], ["XWWCXP", 72],
#       ["SYBRQOHP", 88], ["HJSVV", 75]], 1))


# # class Rectangle:
# #     def __init__(self,l,b):
# #         self.l = l
# #         self.b = b
# #     def get_area(self):
# #         area = self.l * self.b
# #         return area

# # c = Rectangle(4,6)
# # # print(c.get_area())

# class Student:
#     pass


# class Marks:
#     pass


# student1 = Student()
# marks = Marks()

# print(isinstance(student1, Student))
# print(isinstance(student1, Student))
# print(isinstance(marks, Marks))

# print(isinstance(Student, object))
# print(isinstance(Marks, object))

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def totalArea(self):
#         pi =  3.14
#         return pi * self.radius ** 2

#     def perimeter(self):
#         return 2 * self.radius

# print(Circle(6).totalArea())
# print(Circle(6).perimeter())


# class isValid:
#     def __init__(self, input):
#         self.input = input


# def checkBrackets():
#     bracks = {
#         '{': '}',
#         '[': ']',
#         '(': ')',
#     }


# print(checkBrackets())


# def calc_age(age):
# 	return age * 365


# print(calc_age(20))


# conver to int ----> str
# def int_to_str(num):
#     print(type(num))
#     return str(num)

# print(int_to_str(4))


# def str_to_int(str):
#     print(type(str))
#     return int(str)

# print(str_to_int('4'))

# weird way the if/else works here..
# def fizz_buzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return 'fizz_buzz'
#     elif num % 3 == 0:
#         return 'fizz'
#     elif num % 5 == 0:
#         return 'buzz'
#     return str(num)


# print(fizz_buzz(2))


# class Calulator:
#     def __init__(self,num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#     def add(self):
#         return self.num1 + self.num2
#     def subtract(self):
#         return self.num1 - self.num2
#     def multply(self):
#         return self.num1 * self.num2
#     def divide(self):
#         return self.num1 / self.num2


# cl = Calulator(10, 5)

# print(cl.add())
# print(cl.subtract())
# print(cl.multply())
# print(cl.divide())

# right shift problem
# def shift_to_right(x, y):
# 	return  x / 2 ** y


# print(shift_to_right(-512, 10))

# info = {
#   "cost_price": 2.77,
#   "sell_price": 7.95,
#   "inventory": 8500
# }


# # profit problem
# def profit(info):
#     cost =  info.get('cost_price')
#     sell = info.get('sell_price')
#     inventory = info.get('inventory')
#     total_sales = round(sell) * inventory
#     total_cost = round(cost) * inventory
#     profit = total_sales - total_cost
#     return profit

# print(profit(info))

# cricket problem
# def total_overs(balls):
# 	return balls / 6


# print(total_overs(164))


# destinationOne = ['e', 'n', 'e', 'e', 'n']
# destinationTwo = ['w', 'n', 'w', 'n', 'w', 'w', 'n']

# # robot problem
# # def robot_path(commands):

# # list of multiples
# def list_of_multiples (num, length):
# 	for i in range(num):
#         return i


# print(list_of_multiples(7,5))


# def list_of_multiples(num, length):
#     list = []
#     for i in range(1, num + 1):
#         list.append(num * i)
#         if len(list) == length:
#             return list


# print(list_of_multiples(7, 5))


# class Animal:
#     def __init__(self,color):
#         print(self)
#     def color(self, color):
#         print(self.color)


# an = Animal()
# print(an.color())


# def sum(num):
#     total = 0
#     for i in range(1,num + 1):
#         total += i ** 2
#     return total

# print(sum(4))

# n = 4
# i = 1
# total = 0
# while i <= n:
#     total  = total + i * i
#     i = i + 1

#     print(total)

# print(n * (n + 1) * (2 * (n + 1)) // 6)


# L = [1,2,1,6,9,4,0,1,6,2,8,1000,1]
# count = {}

# def frequentNum(L):
#     for i in range(len(L)):
#         if L[i] not in count:
#             count[L[i]] = 1
#         else:
#             count[L[i]] += 1
#     return max(count, key =count.get)

# print(frequentNum(L))


# def check(num):
#     return num


# print(check([1,2,3,4]))
# print(check([3,4,5,6,4]))

# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# output = 5

# def removeDuplicates(nums):
#     for i in range(len(nums)):
#         firstVal = nums[i]
#         for j in range(i + 1, len(nums)):
#             secondVal = nums[j]
#             if firstVal != secondVal:
#                 return i

# print(removeDuplicates(nums))

# nums = [1,1,2]

# def removeDuplicates(nums):
#     i = 0
#     for j in range(len(nums)):
#         if nums[i] != nums[j]:
#             nums[i + 1] = nums[j]
#             i += 1
#     print(nums)
#     return i + 1

# print(removeDuplicates(nums))


# def reverseString(str):
#     # reverse for loop
#     for i in range(len(str), 0,  - 1):
#         print(str[i])


# print(reverseString('Hello'))


# def reverseString(str):
#     i = 0
#     for j in range(len(str)):
#         i -= 1
#     print(i)

# print(reverseString('hello'))


# def reverseString(str):
#     # str[left], str[right] = str[right], str[left]
#     left = 0
#     right = len(str) - 1
#     while left < right:
#         temp = str[left]
#         str[left] = str[right]
#         str[right] = temp
#         left +=   1
#         right -=  1
#         left, right = left + 1, right - 1
#     return str

# str  = ["h","e","l","l","o"]
# print(reverseString(str))


# arr = [0,1,0,3,12]

# def moveZeros(arr):
#     for a in range(len(arr)):
#         if arr[a] == 0:
#             arr.append(0)
#             arr.remove(0)
#     return arr


# print(moveZeros(arr))


# nums = [0,1,0,3,12]

# class Solution:
#     def moveZeros(self, nums):
#         slow = 0
#         for fast in range(len(nums)):

#             if nums[fast] != 0 and nums[slow] == 0:

#                 nums[slow], nums[fast] = nums[fast], nums[slow]
#             if nums[slow] != 0:

#                 slow += 1
#         return nums

# sl = Solution()
# print(sl.moveZeros(nums))

# single num
# nums = [1]
# dict = {}

# class Solution:
#     def singleNumber(self, nums):
#         for i in range(len(nums)):
#             if nums[i] in dict:
#                 dict[nums[i]] += 1
#             else:
#                 dict[nums[i]] = 1

#         return min(dict, key =dict.get)

# sl = Solution()
# print(sl.singleNumber(nums))

# def oddNums():
#     num =[]
#     for i in range(1,100):
#         if i % 2 != 0:
#             num.append(i)
#     return num
# print(oddNums())

# nums = [1,1,2]
# # output = 2

# def removeDuplicates(nums):
#   i = 0
#   for j in range(len(nums)):
#         if nums[i] != nums[j]:
#             nums[i + 1] = nums[j]
#             i += 1
#   print(nums)
#   return i + 1

# print(removeDuplicates(nums))


# nums = [1,1,2]

# def removeDuplicates(nums):
#     i = 0
#     for j in range(len(nums)):
#         if nums[i] != nums[j]:
#             nums[i + 1] = nums[j]
#             i += 1
#     print(nums)
#     return i + 1

# print(removeDuplicates(nums))


#  Contains Duplicate
# nums = [1, 2, 3, 4]


# def containsDuplicate(nums):
#     # iterate through each item
#     # keep a track of each item
#     dict = {}
#     for j in range(len(nums) - 1):
#         if nums[j] == nums[j + 1]:
#             dict[nums[j]] += 1
#         else:
#             dict[nums[j]] = 1
#     return dict
#     # if dict.values() > 2:
#     #     return True
#     # else:
#     #     return False

# # print(containsDuplicate(nums))


s = " race a car"


class Solution:
    def isPalindrome(self, s):
        #  clean the space between strings
        # lowercase all letters
        #  reverse the str
        # if the intial string is equal to the reversed string return True
        cleanedUpstr = ''.join(filter(str.isalnum, s)).lower()
        sortStr = cleanedUpstr[::-1]
        newStr = "".join(sortStr)
        if cleanedUpstr == newStr:
            return True
        else:
            return False

# sl = Solution()
# print(sl.isPalindrome(s))

# two pointer method


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum(i):
                i += 1
            while i < j and not s[j].isalnum(j):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


s = "rat"
t = "car"


class Solution:
    def isAnagram(self, s, t):
        # length of each string is same if not stop the function overall
        if len(s) != len(t):
            return
        # sort both strings if they are the same then it is anagram
        sortS = sorted(s)
        newStrS = "".join(sortS)
        sortT = sorted(t)
        newStrT = "".join(sortT)
        if newStrS == newStrT:
            return True
        else:
            return False


# sk = Solution()
# print(sk.isAnagram(s, t))

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]


class Solution:
    def intersect(self, nums1, nums2):
        list = []
    #  loop through each array if items in num1 == num2 append it in a new list
        for n in range(len(nums1)):
            for x in range(len(nums2)):
                if nums1[n] == nums2[x]:
                    list.append(nums2[x])
        return list


# sl = Solution()
# print(sl.intersect(nums1, nums2))


# range(10)

# for i in range(10):
#     print(i, end=',')
# print()

# for x in range(1,20):
#     print(x, end=',')
# print()

# for j in range(1,20,3):
#     print(j, end=' ')
# print()

# def custom_range(a):
#     i = 1
#     while i <= a:
#          print(i, end=':')
#          i -= 1
# print()

# custom_range(10)

# # for c in custom_range(10):
# #     print(c, end=' ')

# def custom_range(x,y=0,z=1):
#     if y == 0:
#         x = y
#         y = x

#     while x < y:
#         yield x
#         print(x)
#         x += z

#     while x > y:
#         yield x
#         x += z


# # custom_range(1,20,2)


def custom_range(x, y=0, z=1):

    if y == 0:
        x = y
        y = x

    if x < y:
        while x < y:
            yield x
            x = x+z
    else:
        while x > y:
            yield x
            x = x + z


# for i in range(10):
# print(i, end=',')
# print()

# for i in custom_range(10):
# print(i, end=',')
# print()

# for x in range(1, 20):
# print(x, end=',')
# print()

# for x in custom_range(1, 20):
# print(x, end=',')
# print()

# for j in range(1, 20, 3):
# print(j, end=' ')
# print()

# for j in custom_range(1, 20, 3):
# print(j, end=' ')
# print()

# for j in range(20, 1, -3):
# print(j, end=' ')
# print()

# for j in custom_range(20, 1, -3):
# print(j, end=' ')
# print()
# print('end')
#  


# intuitive solution but wrong solu
# x = -123

# class Solution:
#     def reverse(self, x):
#             # convert the x into string
#             # revesre the string
#             # return the string
#             toStr = str(x)
#             reverse = toStr[::-1]
#             print(reverse)


# sl = Solution()
# print(sl.reverse(x))

# x = 123

# class Solution:
#     def reverse(self, x):
#         # convert it into a list
#         # iterate through item backwards
#         # return the result
#         while x < 0:
#             num = x % 10
#         print(num)


# s = Solution()
# print(s.reverse(x))


# def digit_reverse(x):
#     if x>=(2**31-1) or x<=-2**31:
#         return 0

#     else:
#         s=str(x)

#     if x>=0:
#         rev = s[::-1]
#     else:
#         temp=s[1:]
#         temp2=temp[::-1]
#         rev="-"+temp2

#     if int(rev)>=2**32-1 or int(rev)<=-2**32:
#         return 0
#     else:
#         return int(rev)

# print(digit_reverse(1230))
# print(digit_reverse(12345))
# print(digit_reverse(-12345))
# print(digit_reverse(1234556465125564215641))
# print(digit_reverse(-123452514654))
# print(digit_reverse(5000))


# s = "loveleetcode"
# keepTrack = 0
# i = 0
# dict = {}
# class Solution:
#     def firstUniqChar(self, s):
#         for i in range(len(s) - 1):
#             for j in range(1,len(s)):
#                 if s[i] == s[j]:
#                     dict[s[i]] += 1
#                 else:
#                     dict[s[i]] = 1
#         return dict


# sl = Solution()
# print(sl.firstUniqChar(s))

# s = "loveleetcode"
# list = []
# class Solution:
#     def firstUniqChar(self, s):
#         for i in range(len(s) - 1):
#             if s[i] != s[i + 1]:
#                 list.append(i)
#             else:
#                  - 1
#         return list[0]


# sl = Solution()
# print(sl.firstUniqChar(s))

# s = "leetcode"
# test= s.split(' , ')
# print(test)
# # def containsDuplicate(s):
# #     # iterate through each item
# #     # keep a track of each item
# #     dict = {}
# #     for j in range(len(s) - 1):
# #         if nums[j] == nums[j + 1]:
# #             dict[nums[j]] += 1
# #         else:
# #             dict[nums[j]] = 1
# #     return dict


# # print(containsDuplicate(s))


# s = "aabb"
# class Solution(object):
#     def firstUniqChar(self, s):
#         dict = {}
#         i = 0
#         for i in s:
#             if i in dict:
#                 dict[i] += 1
#             else:
#                 dict[i] = 1
#         test = list(dict.values())
#         print(test)
#         for x in range(len(test)):
#             if test[x] < 2:
#                 return x
#         return - 1

# sl = Solution()
# print(sl.firstUniqChar(s))

# s = "loveleetcode"


# class Solution(object):
#     def firstUniqChar(self, s):
#         dict = {}
#         for i in s:
#             if i in dict:
#                 dict[i] += 1
#             else:
#                 dict[i] = 1
#         print(dict)
#         for x in range(len(s)):
#             if dict[s[x]] < 2:
#                 return x
#         return - 1

# sl = Solution()
# print(sl.firstUniqChar(s))


# import collections
# from collections import Counter
# def firstUniqChar(s):
#     count=collections.Counter(s)

#         #3 ways of iteration:
#         # for i in s > value of s :> leetcode
#         # for i in range(len(s)) > index> s[i] > 01234567

#     for index,value in enumerate(s): #enum creates key-value pair
#         if count[value]==1:
#             return index
#     return -1


# print(firstUniqChar("leetcode")) #0
# print(firstUniqChar("loveleetcode")) #2
# print(firstUniqChar("aabbccc")) #-1
# print(firstUniqChar("abcabc"))


# x = "leetcode"
# test = dict(x)

# print(test)

# wrong solution
# digits = [9,9]
# class Solution(object):
#     def plusOne(self, digits):
#        for i in range(len(digits)):
#           if len(digits) == 1:
#               test = digits[i] + 1
#               breakDown = [int(i) for i in str(test)]
#               return breakDown
#           else:
#                lastDigit= digits.pop()
#                changedNum = lastDigit + 1
#                digits.append(changedNum)
#                return digits

# sl = Solution ()
# print(sl.plusOne(digits));

# def reverseString(str):
#     # str[left], str[right] = str[right], str[left]
#     left = 0
#     right = len(str) - 1
#     while left < right:
#         temp = str[left]
#         str[left] = str[right]
#         str[right] = temp
#         left +=   1
#         right -=  1
#         left = left + 1
#         right = right - 1
#     return str

# str  = ["h","e","l","l","o"]
# print(reverseString(str))


s = ["h", "e", "l", "l", "o"]
# i = 0 , j = 4 while i is 0
# 0,1,2,3,4
#


class Solution(object):
    def reverseString(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            test = s[i]
            s[i] = s[j]
            s[j] = test
            i += 1
            j -= 1
            i = i + 1
            j = j - 1
        return s


# sl = Solution()
# print(sl.reverseString(s))

nums = [1, 2, 3, 4]


class Solution(object):
    def containsDuplicate(self, nums):
        dict = {}
        # iterate through  nums
        for i in nums:
            #  if value in obj + 1
            if i in dict:
                dict[i] += 1
            #  else 1
            else:
                dict[i] = 1
        #  if length of the obj is more than 1
        if max(dict.values()) > 1:
            return True
        else:
            return False

# sl = Solution()
# print(sl.containsDuplicate(nums))

# s = "anagram"
# t = "nagaram"
# class Solution(object):
#     def isAnagram(self, s, t):
#         if len(s) != len(t):
#             return
#         strs = sorted(t)
#         testStr = "".join(strs)
#         strs2 = sorted(s)
#         testStr2 = "".join(strs2)
#         if testStr == testStr2:
#             return True
#         else:
#             return False


# # sl = Solution()
# # print(sl.isAnagram(s,t))

# import collections

# s = "rat"
# t = "car"
# class Solution(object):
#     def isAnagram(self, s, t):
#         dict = {}
#         for i in s:
#             if i in dict:
#                 dict[i] += 1
#             else:
#                 dict[i] = 1
#         for x in t:
#             if x in dict:
#                 dict[x] += 1
#             else:
#                 dict[x] = 1
#         if dict[s[i]] > 0:
#             return True
#         else:
#             return False

# sk =Solution()
# print(sk.isAnagram(s,t))


# class Solution:

#  def isAnagram(self, s: str, t: str) -> bool:
#  dic = {}
# for i in s:
#  if i not in dic:

#  dic[i] = 1
#   else:

#  dic[i] += 1


# for j in t:

# if j not in dic:
# return False
# else:
#  dic[j] -= 1
# if dic[j] == 0:

# dic.pop(j)

# if len(dic) == 0:

# return True

# else:

# return False


# digits = [9,9]
# # [123] ---> [1,2,4]
# class Solution(object):
#     def plusOne(self, digits):
#         list = []
#         #  right a reverse for loop
#         #  add the i[0] value + 1
#         # then push it to the new array
#         # for d in range(len(digits)):
#         if  len(digits) > 1:
#             lastNum = digits.pop()
#             addOne = lastNum + 1
#             digits.append(addOne)
#         else:
#             addsingleNum = digits[0] + 1
#             nums = [int(i) for i in str(addsingleNum)]
#             return digits
#         return [1] + digits


# sk = Solution()
# print(sk.plusOne(digits))

        # inplace operations
# digits = [9]

# class Solution(object):
#     def plusOne(self, digits):
#         n = len(digits)
#         for i in range(n):
#             index = n - 1 - i
#             if digits[index] == 0:
#                 digits[index] = 0
#             else:
#                 digits[index] = digits[index] + 1
#                 return digits

#         return [1] + digits

# sk = Solution()
# print(sk.plusOne(digits))


# matrix = [[1,1,1],[1,0,1],[1,1,1]]
# # output =  [[1,0,1],[0,0,0],[1,0,1]]
# class Solution(object):
#     def setZeroes(self, matrix):
#         #  changeMatrix[0] idx 1
#         #  changematrix[1] idx 0,1,2
#         # changematrix[2] idx 0,1,2
#         if len(matrix) > 3 or len(matrix) < 3:
#             return
#         else:
#                    firstMatrix = matrix[0]
#                    secondMatrix = matrix[1]
#                    thirdMatrix = matrix[2]
#                    for m in range(len(matrix)):
#                     check1 = firstMatrix[m]
#                     check2 = secondMatrix[m]
#                     check3 = thirdMatrix[m]
#                 #     if that list has a value of 0 then make everything in the list 0
#                 # and also make the index of that particualr lists 0 for example if m[2] = 0 then make that index position 0
#                     if check1 == 0 or check2 == 0 or check3 == 0:
#                         thatMatrix = matrix[m]
#                         thatidx = m
#                         print(thatidx)
#                         for m in range(len(thatMatrix)):
#                             thatMatrix[m] -= thatMatrix[m]
#                             # list[0] [0,0,0]
#                             # list[1] [1,0,1]


# sl = Solution()
# print(sl.setZeroes(matrix))


# matrix = [[1,1,1],[1,0,1],[1,1,1]]
# class Solution(object):
#     def setZeroes(self, matrix):
#     rows = set()
#     column = set()
#     n = len(matrix)
#     c = len(matrix[0])
#     for i in range(n):
#         for j in range(n):
#             if matrix[i][j] == 0:
#                 rows.add(i)
#                 column.add(j)


#         print(rows)
#         print(column)


#         for i in range(n):
#             for j in range(c):
#                  if i in row or j in column:
#                     matrix[i][j] = 0

# print(matrix)


# sk = Solution()
# print(sk.setZeroes(matrix))


# str = "%%%%%Saurabh%%%%Singh%%%%"
# def trimPercentSign(str):
#     newStr = ''
#     # loop through the string
#     # remove push the string only to a new string
#     #  then add the % sign in respective places
#     #  if letter is capital then before that add a percent sign in between the strings
#     n = len(str)
#     for s in range(n):
#         if str[s] != '%':
#             newStr += str[s]
#     l = len(newStr)
#     for a in range(l):
#         if newStr.isalpha():
#             newStr += '%'
#     return newStr
# # print(trimPercentSign(str))
# input_str = "%%%%%Saurabh%%%%Singh%%%%"


# def remove_percentage_sign(input_str):
#     output = ""
#     prev_char_is_letter = False
#     for char in input_str:
#         if char != '%':
#             output += char
#             prev_char_is_letter = True
#         else:
#             if prev_char_is_letter:
#                 output += '%'
#                 prev_char_is_letter = False
#     if output[-1] == '%':
#         output = output[:-1]

#     return output


# print(remove_percentage_sign(input_str))

prices = [7, 1, 5, 3, 6, 4]


# class Solution(object):
#     def maxProfit(self, prices):
#         buy = 0
#         sell = 0
#     #    profit = sell - buy
#         cost = range(len(prices))
#         for p in cost:
#             buy = (prices[p])
#             sell = prices[p - 1]
#             print(buy, end=" | ")
#             print()
#         #    print(sell, end=" | ")


# sk = Solution()
# print(sk.maxProfit(prices))


L = [1, 2, 1, 6, 9, 4, 0, 1, 6, 2, 0, 1000, 1, 2, 2, 2, 2, 2]
# L1 = [1,1,1,1]


def repeatedNum(L):
    dict = {}
    for n in L:
        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1
    print(dict)

    m = 0
    for index, value in dict.items():
        print(dict.items())
        if value > m:
            m = value
            output = index
    return output

# print(repeatedNum(L))


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# class Solution(object):
#     def trap(self, height):
#         for h in range(len(height)):
#             right = height[h]
#             left = len(height) - 1
#             right = left
#             left = right


# sk = Solution()
# print(sk.trap(height))


# class Solution:

#     def trap(self, height: List[int]) -> int:

#         left = 0

#         right = len(height) - 1

#         max_left = max_right = water = 0


#         while left < right:

#             if height[left] <= height[right]:

#                 if height[left] >= max_left:

#                     max_left = height[left]

#                 else:

#                     water += max_left - height[left]

#                 left += 1

#             else:

#                 if height[right] >= max_right:

#                     max_right = height[right]

#                 else:

#                     water += max_right - height[right]

#                 right -= 1


#         return water


# arr = ["t", "h", "e" , "s", "k", "y", "i", "s", "b", "l", "u","e"]

# def reverseStr(arr):
#         reverse = arr[::-1]
#         return reverse

# print(reverseStr(arr))


# def fixStr():
#      left = 0
#      right = len(arr) - 1
#      while >= 0:


# nums = [1,2,3,4,5,6,7]
# k = 3

# # Output: [5,6,7,1,2,3,4]

# newList = []
# class Solution(object):
#     def rotate(self, nums, k):
#             r = range(len(nums))
#             for n in r:
#                 if n == k:
#                     newList.append( nums[k + 1])
#                     print(newList)


# sk = Solution()
# print(sk.rotate(nums,k))


# nums = [3,0,1]

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:


# def shift_to_right(x, y):
#         return round(x / 2 ** y)

# print(shift_to_right(4666,6))


list = [-1, 3, 5, 6, 99, 12, 2]
# def find_highest(list):
#     min = list[0]
#     for i in range(len(list)):
#         if list[i] > min:
#             min = list[i]
#     return min


# print(find_highest(list))

# trying to use recursion to solve this problem
# def find_highest(list):
#    min = list[0]
#    i = 0
#    if list[i] > min:
#        min = list[i]
#    else:
#        find_highest(i, list)
#        pass
#    return min


# print(find_highest(list))

# arr = [-1, 3, 5, 6, 99, 12, 2]
# def highestNum(arr):
#     i = 0
#     right = len(arr) - 1
#     tracker = range(len(arr))
#     for i in tracker:
#         if arr[i] > arr[right]:
#             print('tracker left', arr[i])
#             print('tracker right', arr[right])


# print(highestNum(arr))


# def tri_area(base, height):
#     return round((base * height) / 2)


# print(tri_area(7, 4))


# lst = [1, 2, 3, 4, 5, 6]


# def sum_odd_and_even(lst):
#     even = 0
#     sum = 0
#     odd = 0
#     for i in range(len(lst) - 1):
#         if lst[i] % 2 == 0:
#             even += lst[i]
#         else:
#             odd += lst[i]
#     print('odd', odd)
#     print('even', even)


# print(sum_odd_and_even(lst))

# solving simple problems to be familiar with syntax
# def football_points(wins, draws, losses):
#     return wins * 3 + draws * 1 + losses * 0


# print(football_points(5, 0, 2))


# def format_date(date):
#     # remove the extra slashes and everything from the date so we can restructure it
#     # use filter function to remove the unwanted slashes
#     date_list = date.split("/")
#     reverse_list = date_list[::-1]
#     print(reverse_list)
#     newStr = ''
#     for d in reverse_list:
#         newStr += d

#     return newStr; 


# print(format_date("11/12/2019"))

# calculate profit 
# info =  {
#   "cost_price": 2.77,
#   "sell_price": 7.95,
#   "inventory": 8500
# }
# def profit(info):
#     total_sales = info["cost_price"] * info["inventory"] - info["sell_price"] * info["inventory"]
#     return round(abs(total_sales))

# print(profit(info))


# invert key value 

# dct = { "z": "q", "w": "f" }
# def invert(dct):
#     return dict(map(reversed, dct.items()))
            
# print(invert(dct))

orginalLst = [5, 5, 10, 10, 15, 15, 20, 20]
orginalTime = 120

def interview(lst, tot):
	# time limit is 120 mins 
    # easy questions 5 mins 
    # easy question 10 mins 
    # med questions 15 mins 
    # hard questions 20 mins 
    global orginalLst 
    global orginalTime
    timeOrg = 0
    time = 0
    orginalTime =sum(orginalLst)
    
    for timeOrg in orginalLst:
        for time in lst:
            if time <= timeOrg and orginalTime <= tot:
                return "Qualified"
            else:
                return "Disqualfied"

print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))
print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64))
print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120))
print(interview([5, 5, 10, 10, 15, 15, 20], 120))
print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))











