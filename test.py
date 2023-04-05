# # print('hello')
# # a = 2 + 6 + 1
# # print(a)
# # b = 3
# # print("type of b: ", type(b))
# # print('hello world!')
# # item = 'JohnCena'
# # print(item[6])
# # print(item[::-1])

# # print(item)
# # item1 = "{0} {1} ".format('john', 'cena')
# # print(item1)
# # # arrays
# # import array as arr;
# # a = arr.array('i', [1,2,3,4,5,6,7,8])
# # print(a[3])
# # b = arr.array('d', [])

# # list
# # L = [1,2,3,4]
# # L1 = []
# # L2 = list([1,2,3,4])
# # print(L2)

# # L[0] = 5
# # L.append(6)
# # L.insert(3, "Rishav")
# # print(L)
# # print(L1)
# # print(L2)

# # X = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
# # print(X[3])

# # print(X[-6])
# # print(X[2], " : ", X[-1], " : ", X[-5])

# # print(X[-4])
# # print(X[-1])
# # print(X[-6])
# # there is no length for integers

# # Z = [
# #     ['Geeks', 'For', 'Geeks'],
# #     ['Geeks'], "5", ['Hello',
# #                      ['World']]
# # ]

# # append method appends....at the end of the list

# # L = list()
# # L.append(1)
# # L.append(2)
# # L.append(4)
# # L.insert(3, 12)
# # L.insert(0, 'Geeks')
# # print(L)
# # L.extend([8, 'Geeks', 'Always'])
# # print(L)
# # L.append([8, 'Geeks', 'Always'])
# # print(L)


# # List = [1,2,3,4,5,5,6,7,8,9,10,11,12]

# # List = [1,2,3,4,5]
# # # List.remove(5)
# # # List.remove(6)
# # # print(List)
# # # List.remove(5)
# # # print(List)
# # List.pop(-3)
# # # List.append(5)
# # print(List)


# # List = [1, 2, 3, 4, 5]# a = List.pop()# print(a)# print("List after popping an element: ")# print(List)# List.append(a)# print(List)# Removing element at a specific location from the Set using the pop() method# a = List.pop(-1)# print("List after popping a specific element: ")# print(List)
# # L = [1,2,3,4,5,6,7,8,9]
# # L1 = (L[1:5])

# # print(L[-5:])
# # print(L[-5:-2])
# # print(L[::-1])
# # print(L[-5])
# # print(L[2])
# # L2 = L[:5]
# # # print(L2)
# # L3 = L[5:]
# # # print(L3)
# # L4 = L[:]
# # print(L4)
# # print(L[0:5])
# # print(L[0:6])

# # slice will start from the given index and go until the specified index -1
# # ([start_index:end_index])

# # T = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h']
# # print(T[:])

# # L4[0] ='Rishav'
# # print(L4)

# # TUPLEs are immutable

# # t1 = ('Geeks', 'For')
# # t2 = (5, 'Welcome', 7, 'Geeks')
# # t3 = t1 + t2
# # print(t1[1:])
# # print(t2[::-1])
# # print(t2[2:4])

# # tuple1 = (0,1,2,3,4)
# # tuple2 = ('python' , 'geek')
# # tuple3 = (tuple1,tuple2)
# # print(tuple3[1][0])
# # print(tuple3[0][2])
# # tuple1[0] = 's'

# # tuple1 = (0,1)
# # del tuple1
# # print(tuple1)


# # print(Z[3][-1])
# # print(Z[-3][-1])
# # print(len(Z[3][0]))
# # print(Z[1][0][4])
# # print(Z[0])
# # print(Z[1])
# # print(Z[0][1])
# # print(Z[0][1])
# # print(Z[3][1])
# # print(Z[3][1][0])
# # # print(Z[-1][-1][0])
# # print(Z[-1][-1])
# # print(Z[-1][-1][-1])
# # print(Z[-1][-2])
# # print(Z[-1][0])
# # print(Z[3][0])
# # L = [1,2,3,4]
# # print(len(L))
# # print(len(Z[0]))
# # print(len(Z))

# # dicitionary
# # stores data in key:value pairs

# from functools import reduce
# import os
# d1 = dict()
# d2 = {}
# L = list()
# L = []
# T = ()

# D = ({1: 'Geeks', 2: 'For', 3: 'Geeks'})
# d3 = dict([(1, 'Geeks'), (2, 'For')])
# d4 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# d5 = {'a': 'apple', 'b': 'ball'}
# d6 = {'a': ['Red Apple', 'Blue Apple'], 'b': ["Bat", "Ball"]}

# # print(d6.get('a'))
# # print(d6.get('c', 'Not available'))
# # print(d5.get('a'))
# # print(d3)
# # print(d4)
# # print(D[1])
# # print(D[2])
# # print(D[3])
# # # print(D[1])
# # # print(D.get([5])) --> wrong syntax
# # print(D.get(5))
# # print(D.get(5, "not present"))

# d11 = {}
# d11[0] = 'Hello'
# d11[1] = 'How are you?'
# d11[3] = 'How is it going?'
# d11[4] = {'Nested': {'1': 'New', '2': 'World'}}

# # print(len(d11[4]["Nested"]['2']))

# # print(d11)
# # print(type(d11[3]))
# # print(d11[4]['Nested']['2'])
# # print(d11[4].get('Nested'))
# # print(d11[4].get('Nested').get('2'))

# dict1 = {1: 'Python', 2: 'Java', 3: 'Ruby', 4: 'Scala'}
# dict2 = dict1.copy()

# d7 = {'a': ["Red Apple", "Blue Apple"], 'b': ["Bat", "Ball"]}
# # print(d7)
# # d ={}
# # print(len(d))

# # dict1.clear()
# # print(dict1)
# # print(dict2)

# # print(dict2.items())
# # print(dict2.keys())
# # print(dict2.pop(4))
# # print(dict2.popitem())
# # dict2.update({3: 'Scala'})
# # print(dict2.values())

# # print(len(dict1))

# # test_value = 1000
# # if test_value > 1:
# #    print('this code is executed')

# # if test_value > 1000:
# #    print('this code is not executed!')

# # print('Program continues at this point')


# # if test_value == 100:
# #     print('It is a match ')

# # if test_value < 100:
# #     print('It is lower than 100')

# # if test_value > 100:
# #     print('It is higher than 100')


# # test_item = 50
# # if test_item < 1:
# #     print('Value is < 1')
# # else:
# #     print('Value is >= 1')


# # test_string = 'valid'
# # if test_string == 'NOT_VALID':
# #     print('String equals not_valid')
# # else:
# #     print('String equals somehting else!')


# # test_case = 'not_valid'

# # print(len(test_case))

# # pet_type = 'dog'

# # if pet_type =='dog':
# #     print('You have a dog')
# # elif pet_type == 'cat':
# #     print('You have a cat')
# # elif pet_type == 'fish':
# #     print('You have a fish')
# # else:
# #     print('you have something else')


# # for loop


# L = ["a", 'b', 'c', 'd', 'e']
# # print(len(L))
# # for i in L:
# #     print(i)
# #     print(i , end=" : ")
# #     print(L[i])

# # range(5)
# # # output --> 0,1,2,3,4

# # for i in range(len(L)):
# #     print(L[i]);

# # look into enumerate

# # for index, value in enumerate(L):
# #     # print(index, " : ",  value)
# #     print(index)
# #     print(value)
# #     # print(L)

# # n = 0
# # for i in range(1, 6):
# #    print(i)
# #    n +=  i * i
# # print(n)

# # use command + c to stop a while loop

# # count = 0
# # while(count < 3):
# #     count = count  + 1
# #     print('hello')

# # make a square of numbers in while loop

# # n = 0
# # i = 1
# # sum = 5
# # while ( i <= n):
# #     n += n ** i
# #     n = n + 1
# #     print(n)
# # n = 4
# # v = (n ** 2 + 1) / 2
# # v = (n ** 2 + 1) * (n ** 2 + 1) / n
# # # print(v)
# # sum=0
# # input = 4
# # sum = (input * (input + 1) * (2*input + 1))/ 6
# #  print(sum)

# # var = None

# # if var is None:
# #     print('value has a value None')
# # else:
# #     print('item has value')


# # a = 10
# # b = 20

# # if (a < b):
# #    pass
# # else:
# #    item = b < a
# #    print(item)

# # def function():
# #     pass

# # a = None
# # print(a)
# # a = 10 + 10
# # print(10)

# # def function_name(parameters):
# #     "docstring"
# #     return expression


# # def function_item(parameter: data_type):
# #     return expression

# # def function_control()

# # def fun():
# #     print('welcome to the jungle!')


# # fun()


# def add(num1: int, num2: int):
#     """num3"""
#     num3 = num1 + num2
#     return num3


# # add(1, 2)

# def subtract(num1, num2):
#     num3 = num2 - num1
#     return num3


# subtract(6, 7)


# n1 = 5
# n2 = 10
# item = add(n1, n2)
# # print(item)

# # def addfunc(a:int, b:int)->int:   
# # sum=a + b
# # return sumn1=int(input())
# # n2=int(input())
# # n3=addfunc(n1,n2)
# # print(n3)


# # count = 0
# # for i in range(1,5):
# #     count += i * i
# # print(count)

# # count = 4
# # i = 1
# # sum = 0
# # while i <= count:
# #     sum += i ** 2
# #     i = i + 1
# # print(sum)


# # def check(item):
# #     if (item == 'hello'):
# #         print('hello world')
# #     else:
# #         print('hello universe')


# # check('random')

# # arr = ['Python', 'is a', 'super', 'cool', 'progrmaming', 'language!']


# # def item():
# #     for i in (len(arr)):
# #         print(arr[i])
# # item()


# # word = "abc de ok"

# # clear
# # print(getVowel(words1, vowels))
# # print(getVowel(word2, vowels))

# # set is unordered set has no index --  sets are not a stack

# # myset = set(['a', 'b', 'c'])
# # print(myset)


# # myset.add('d')
# # print(myset)


# # myset[1] = 'hey'
# # print(myset)


# # myset1 = {"geeks", "for", 10, 52.7, True}
# # print(myset1)


# # def check(input):
# #     str = {'0', '1'}
# #     if str == set(input) or set(input) == {'1'} or set(input) == {'0'}:
# #         return True
# #     else:
# #         return False


# # print(check('hghghgh'))
# # print(check('01010101'))

# # def binary(s):    for char in s:        if char not in {'0', '1'}:            return False    return Trues=((input('Input Data: ')))d=set(s)print('Entered Data is : ',s)print('Is Binary: ',binary(d))


# # def strCount(words):
# #     # declare object
# #     a = {}
# #     # iterate over the words
# #     for word in words:
# #         #  if words is not already there then add it
# #         print(word)
# #         # word[words] = word.get(word, 0) + 1
# #     #  if word in a:
# #     # #   dont add
# #     #   print(word)
# #     #  else:
# #     #     print(a[word])
# #     #  else don't add


# # strCount('hello')


# # test_str = "Sauarabhhs"
# # result = {}
# # for keys in test_str:
# #     print("Before inserting result.get(keys, 0)", result)
# # #     result[keys] = result.get(keys, 0) + 1
# # #     print("After inserting result.get(keys, 0)", result)
# # #     print("Count of all characters is : ", result) 


# # # fruits = ['papaya', 'mango', 'kiwi']
# # # for fruit in fruits:
# # #     print(fruit)

# # # item = 'I am a javascript developer but I am also leanring python'
# # # for items in item:
# # #     print(items + '1')
# # # count = 7

# # # for x in range(1,60):
# # #     if (count % 2 == 0):
# # #         print('number is even!')
# # #     else:
# # #         print('number is not a even number!')


# # # arr = [1,2,3,4,5,6,7,8]
# # # # print(len(arr))


# # # for i in range(len(arr)):
# # #     if arr[i] > 4:
# # #         print('item is one two three four')


# # # def checkBinary(str):
# # #     binaryNum = set(['0', '1'])
# # #     for i in set(str):
# # #         if i not in binaryNum:
# # #            return False
# # #         else:
# # #            return True


# # # print(checkBinary('hghghghghghg'))

# # # words = "abc de ok"
# # # vowels = 'a,e,i,o,u,A,E,I,O,U'

# # # def checkVowels(words, vowels):
# # #     result = 0
# # #     for i in words:
# # #         if i in vowels:
# # #             result += 1
# # #     return result

# # # print(checkVowels(words, vowels))


# # # def checkBinary(str):
# # #     binary = {'0', '1'}
# # #     if binary == set(str) or set(str) == {'0'} or set(str) == {'1'}:
# # #         return True
# # #     else:
# # #         return False

# # # print(checkBinary('0'))


# # # n = input('enter')

# # # def checkStr(n):
# # #     if type(n) == str:
# # #         return True
# # #     else:
# # #         return False

# # # print(checkStr(n))


# # # vowels = 'a,e,i,o,u,A,E,I,O,U'
# # # input = 'ABeeIghiObhkUul'
# # # small = input.lower()

# # # def checkVowel(input):
# # #     for i in input:
# # #         if input in vowels:
# # #             print(len(vowels))
# # #         else:
# # #             print('not accepted')
# # # print(checkVowel(input))

# # #  if the vowel string is

# # # def checkItem():


# # # def check(string):
# # #     string = string.lower()
# # #     vowels = set("aeiou")
# # #     s = set({})
# # #     for char in string:
# # #         if char in vowels:
# # #             s.add(char)
# # #             if len(s) == len(vowels):
# # #                   print("Accepted")
# # #                   else:
# # #                   print("Not Accepted")
# # #                   if __name__ == "__main__":
# # #                      string = "SEEquoiaL"
# # #                      check(string)
# # #                      string = "AaeEsdfsdfgiOu"    check(string)    string = "Saurabh"    check(string)


# # # print (1000/0)

# # # a = [1,2,3]

# # # try:
# # #  print(a[1])
# # # except:
# # #    print('error')

# # # print(10/ 0)

# # # def divide(x,y):
# # #    try:
# # #       result1 = x / y
# # #       result2 = x // y
# # #       result3 = x % y
# # #       print(result1, result2, result3)
# # #    except ZeroDivisionError:
# # #       print('error')
# # # divide(21,3)
# # # divide(3,0)


# # # def fun(a):
# # #     if a < 4:
# # #         b = a/(a - 3)
# # #     print(b)
# # #     try:
# # #         fun(3)
# # #         fun(5)
# # #     except ZeroDivisionError:
# # #         print('zero division error')
# # #     except NameError:
# # #         print('name error occurred')


# # # fun(5)


# # # # read file
# # # file = open(item.txt, 'r')
# # # print(file)
# # # # edit the file
# # # file = file.write(item.txt, 'w')
# # # # closes a file
# # # file.close()


# # test_str = 'myNameisRishavaCharya'
# # obj = {}
# # for keys in test_str:
# #     obj[keys] = obj.get(keys, 0) + 1
# # print(obj)


# # # def checkWord(string):
# # #     str = string.lower()
# # #     vowels = set('aeiou')
# # #     s = set({})
# # #     for i in str:
# # #         if i in vowels:
# # #             s.add(i)
# # #         else:
# # #             pass
# # #     if (len(s)) == (len(vowels)):
# # #         print('Accepted')
# # #     else:
# # #         print('no accepted')


# # # checkWord('juju')


# # # present working directory
# # path = '/Users/admin/desktop/test'

# # # All files in Test folder before creating new file
# # dir_list = os.listdir(path)
# # print("List of directories and files before creation:")
# # print(dir_list)

# # # Creates a new file
# # with open('/Users/admin/desktop/test/test.txt', 'w') as fp:
# #     fp.write("New file created")


# # # All files in Test folder after creating new file
# # dir_list = os.listdir(path)
# # print("List of directories and files after creation:")
# # print(dir_list)


# # # present working directory
# # path = '/Users/admin/desktop/test'

# # # All files in Test folder before creating new file
# # dir_list = os.listdir(path)
# # print("List of directories and files before creation:")
# # print(dir_list)

# # # Creates a new file
# # with open('/Users/admin/desktop/test.txt', 'w') as fp:
# #     fp.write("New file created.")
# #     fp.write("This is the write command.")
# #     fp.write("It allows us to write in a particular file,this is a file.")
# #     fp.write("This will add this line,hello world!")

# # # All files in Test folder after creating new file
# # dir_list = os.listdir(path)
# # print("List of directories and files after creation:")
# # print(dir_list)


# # def checkWords():
# #     count = 0
# #     with open('/Users/admin/desktop/test.txt', 'r') as fp:
# #         file = fp.read()
# #         print(file)
# #     data = file.replace('.', ' ').replace(',', ' ').split()


# # #    print(data)
# # #    print(len(data))
# # #    for i in range(len(data)):
# # #       count += i
# # #       print(count)
# # checkWords()


# # def oddNum():
# #     num = []
# #     for i in range(1, 11):
# #         if i % 2 is not 0:
# #             num.append(i ** 2)
# #         #   print(num)
# # # print(oddNum())


# # # pythonic way of writing this code function
# # L = [i ** 2 for i in range(1, 11) if i % 2 == 1]
# # # print(L)


# # # Write a program to print a list with all numbers less than 100 who are divisible by both 2 and 5?


# # def checkNum():
# #     list = []
# #     for i in range(1, 100):
# #         if i % 2 == 0 and i % 5 == 0:
# #             list.append(i)
# #             print(list)
# # # print(checkNum())


# # L = [i for i in range(1, 100) if i % 2 == 0 and i % 5 == 0]

# # # print(L)


# # def createMatrix():
# #     matrix = []
# #     for i in range(0, 5):
# #         matrix.append([])
# #         for n in range(0, 5):
# #             matrix[i].append(n)
# #         print(matrix)


# # print(createMatrix())


# # # list =  []

# # matrix = [[i for i in range(0, 5)] for n in range(0, 5)]

# # # print(matrix)


# # # lambda

# # # def square(n):
# # #    item = n ** 2
# # #    return item

# # # print(square(5))

# # def square(n): return n ** 2


# # # print(square(5))


# # def max(x, y): return x if x > y else y


# # # print(max(4, 6))


# # T = 'hello world'
# # def Y(T): return print(T)


# # # print(Y)

# # # map function
# # def starts_with_A(s):
# #     return s[0] == 'A'


# # fruit = ['Apple', 'Banana', 'Pear', 'Apricot', 'Orange']
# # map_object = map(starts_with_A, fruit)
# # # print(list(map_object))


# # map_item = map(lambda s: s[0] == 'A', fruit)
# # print(list(map_item))


# # # filter function
# # def starts_with_F(j):
# #     return j[0] == 'F'


# # things = ['Fun', 'Fuzz', 'Action']

# # filter_obj = filter(starts_with_F, things)
# # # print(list(filter_obj))

# # filter_item = filter(lambda j: j[0] == 'F', things)
# # print(list(filter_item))

# # #  reduce function
# # def add(x, y):
# #     return x + y


# # list = [2, 4, 7, 3]
# # # print(reduce(add, list))
# # print(reduce(lambda x, y: x + y, list, 10))


# # myStrings = ("demigod", "rewire", "madam", "fortran", "python", "xamarin", "salas", "PHP")

# # def palineDrome(myStrings):
# #     list = []
# #     #  iterate through each string
# #     #  reverse each string
# #     #  if reverse string == regular string
# #     #  return  plaindrome
# #     #  else not a palindrome
# #     for s in myStrings:
# #         if s is s[::-1]:
# #             y = list(s)
# #             return y
# #         else:
# #             return 'not a palindrome'


# # filter_obj = filter(plaineDrome, myStrings)
# # print(list(filter_obj))


# # filter_strings = filter(lambda x: x == x[::-1], myStrings)

# # print(list(filter_strings))


# # def checkpalindrome(word):

# # return word == word[::-1]

# # words = ["demigod", "rewire", "madam", "fortran", "python", "xamarin", "salas", "PHP"]
# # palindromes = list(filter(checkpalindrome, words))
# # print(palindromes)


# # names = ['john', 'kodie','kimi', 'ron']

# # def upperCase(names):
# #     return names[0].upper()


# # map_object = map(upperCase, names)
# # print(list(map_object))

# # # print(upperCase(names))

# # persons = ['alfred', 'tabitha', 'william', 'arla']

# # uppered_persons = list(map(str.upper, persons))

# # print(uppered_persons)


# # •Write a Python program to print length of all the items of a list

# # •Input:
# # x = ['ab', 'cd', 'a']

# # # •Output:
# # # [2, 2, 1]


# # def itemLength(x):
# #     return  list(len(x))

# # map_obj = map(itemLength, x)
# # print(itemLength(map_obj))

# # print(itemLength(x))


# # x = ['ab', 'cd', 'a']
# # print(x)
# # len = list(map(len, x))
# # print(len)


# # numbers = []
# # for i in range(1,10001):


# # def checkNum():
# #     for n in range(1,10001):
# #         print(n)

# # print(checkNum())

# # list = [n for n in range(1,10001) if n % 8 == 0 ]
# # print(list)


# # elements = ['Ch','Dh','Eh','cb','Tb','Td','Chb','Tdb']

# # item = [e for e in elements if len(e) > 2 and e.endswith('b')]
# # print(item)

# # import re
# # s = 'hello world'
# # match = re.search(r' \ .', s)
# # print(match)

# # import re
# # txt = "The rain in Spain"
# # x = re.findall("ai",txt)
# # y = re.findall("Portugal",txt)
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


# # x = re.sub("\s","9", txt)
# # y = re.sub("\s","9", txt,2)

# # print(x)
# # print(y)


# # def listfyColor(colorList):
# #     return colorList
# # colorList = ['Red', 'Blue', 'Black', 'Pink']


# # map_color = map(list,colorList)
# # print(list(map_color))

# class Dog:
#     attr1 = 'Mammal'
#     attr2 = 'Dog'

#     def fun(self):
#         print("I am a ", self.attr1)
#         print('I am a ', self.attr2)


# # Rodger = Dog()
# # Max = Dog()
# # print(Rodger.attr1)
# # print(Max.attr2)
# # Rodger.fun()


# # class Person:
# #     def __init__(self,name,last):
# #         self.fname = name
# #         self.lname = last
# #     def say_hi(self):
# #         print('hello! my name is',self.lname, self.fname)


# # p = Person('Rishav', 'Acharya')
# # x = Person('Kimmy', 'Green')
# # z = Person('Johnny', 'Boy')


# # p.say_hi()
# # x.say_hi()
# # z.say_hi()


# # class Car:
# #     wheels = 4
# #     def __init__(self, name):
# #         self.name = name


# # class Dog:
# #     animal = 'Dog'
# #     # contructor
# #     def __init__(self, breed, color):
# #         print(self)
# #         print('hello')
# #         self.breed = breed
# #         self.color = color


# # class Dog:
# #     animal = 'dog'

# #     def __init__(self, breed):
# #         self.breed = breed
# #     def setColor(self,color):
# #         self.color = color
# #     def getColor(self):
# #         return self.color


# # Pinky = Dog('Mastif:', 'Brown')
# # Kiku = Dog('Labrador:', 'Golden')

# # print( "Pinky", Pinky.animal)
# # print("Pinky", Pinky.color)

# # print( "Kiku", Kiku.animal)
# # print("Kiku", Kiku.color)


# # class Employee:

# #     def __init__ (self):
# #         print('employee create')
# #     def __del__()


# # import builtins
# # # help(builtins.abs)
# # print(builtins.abs(-155))

# # print(builtins.abs(155))

# # print(builtins.abs.__doc__)


# # import builtins
# # # help(builtins.abs)
# # print(builtins.abs.__doc__)
# # print(builtins.abs(-123))
# # help(builtins)


# # help(builtins)

# # help(print)

# # help(list)


# # class Balanced_brackets:
# # def is_valid_parenthese(self, str1):
# # stack= []
# # pchar = {"(": ")", "{": "}", "[": "]"}
# # for parenthese in str1:
# # if parenthese in pchar:
# # stack.append(parenthese)
# # print("Stack: ", stack)
# # elif len(stack) == 0 or (pchar[stack.pop()]) != parenthese:
# # return "Unbalanced"
# # return len(stack) == 0


# # print(Balanced_brackets().is_valid_parenthese("({[]})"))
# # print(Balanced_brackets().is_valid_parenthese("()"))
# # print(Balanced_brackets().is_valid_parenthese("()("))
# # print(Balanced_brackets().is_valid_parenthese(")("))


# # class Rectangle:
# #      def __init__ (self, length, breadth):
# #          self.length = length
# #          self.breadth = breadth
# # def area(self):
# #         total = self.length * self.breadth
# #         print(total)

# class Rectangle:
#     #   intialize constructor
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#     # calculate area

#     def area(self):
#         total = self.length * self.breadth
#         return total


# item = Rectangle(4, 8)

# # print(item.area())


# class Student:
#     pass


# class Marks:
#     pass


# student1 = Student()
# marks1 = Marks()


# # print(isinstance(student1, Student))
# # print(isinstance(student1, Marks))
# # print(isinstance(marks1, Marks))
# # print(isinstance(marks1, Student))
# # print(issubclass(Student, object))
# # print(issubclass(Marks, object))

# # import math

# # class Circle:

# #      def __init__(self,radius):
# #           self.radius = radius
# #      def totalArea(self):
# #           return  round(math.pi * self.radius ** 2)
# #      def periMeter(self):
# #           return round(2 * math.pi * self.radius)

# # circle1 = Circle(8)

# # print(circle1.totalArea())
# # print(circle1.periMeter())

# # test cases ---> valid parenthisesis ---->


# # def isValid(input):
# #      collection = {
# #           '(':')'
# #           ,'{':'}'
# #           ,'[':']'
# #      }
# #      stack = []
# #      for p in input:
# #           if input in collection:
# #             stack.append(p)
# #             print(stack)
# #           elif len(stack) == 0 or collection[stack.pop()] != collection:
# #                 return False
# #           return len(stack) == 0


# # print(isValid('(){}[]'))


# # class Brackets:
# #     def isValid(self, str):
# #         print(str)
# #         stack = []
# #         collection = {
# #             '(': ')', '{': '}', '[': ']'
# #         }
# #         for p in str:
# #             if p in collection:
# #                 # if any opening bracket append it to the key
# #                 stack.append(p)
# #                 print(stack)
# #             elif len(stack) == 0 or collection[stack.pop()] != p:
# #                 return False
# #         return len(stack) == 0


# # # print(Brackets().isValid('{}()[]'))
# # # print(Brackets().isValid('([{}])'))
# # # print(Brackets().isValid('())'))
# # # print(Brackets().isValid('{[)()('))
# # # print(Brackets().isValid('{{{{{{'))
# # # print(Brackets().isValid('}}}}}}}'))
# # # print(Brackets().isValid('{([])}'))

# # # class BaseClass:


# # # class DerivedClass(BaseClass):

# # # class Person:
# # #     def __init__(self,name,id):
# # #         self.name = name
# # #         self.id = id
# # #     def display(self):
# # #         print(self.name, self.id)


# # class Emp(Person):
# #     def __init__(self, name, id, post, salary):
# #         self.salary = salary
# #         self.post = post
# #         Person.__init__(self,name,id)
# #     def print(self):
# #         print("Emp class called")


# # emp_details = Emp('Cookie', 890, 500000, 'Full-Stack developer')
# # print(emp_details.display())

# # # returns a error
# # class A:
# #     def __init__(self, n='Rahul'):
# #         self.n = n


# # class B:
# #     def __init__(self, roll):
# #         self.roll = roll


# # o = B(23)
# # print(o.name)

# # class Employee():
# #     def __init__(self, id, name, Add):
# #         self.id = id
# #         self.name = name
# #         self.Add = Add


# # class Freelance(Employee):
# #     def __init__(self, id, name, Emails):
# #         super().__init__(id, Name, Add)
# #         self.Emails = Emails


# # # ep1 = Freelance()


# # •Write a python function to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.

# # •Assume that atleast one pair exists.

# # •L = [3,4,6,1,8], target = 10

# # •Output – [1,2]

# L = [3,4,6,1,11]
# target = 12

# # def findSum(L, target):
# #     #  loop through the list
# #     #  find the sum of each pair
# #     # if sum === target return the index of the L
# #     for num in range(len(L) - 1):
# #         for x in range(num + 1, len(L)):
# #             if L[num] + L[x] == target:
# #                 return [num, x]


# # print(findSum(L,target))


# # def twoSum(L,target):
# #     d = {}
# #     for i, value in enumerate(L):
# #         if d.get(value, None) == None:
# #             d[target - value] = i
# #         else:
# #             return [d.get(value), i]


# # print(twoSum(L, target))


# class Animals:
#     def __init__(self):
#         self.legs = 4
#         self.domestic = True
#         self.tail = True
#         self.mammals = True

#     def isMammal(self):
#         if self.mammals:
#                 print('it is a mammal!')
#     def isDomestic(self):
#         if self.domestic:
#                 print('it is domestic!')

# class Dogs(Animals):
#     def __init__(self):
#         super().__init__()


# class Horses(Animals):
#     def __init__(self):
#         super().__init__()


#     def hasTailandLegs(self):
#         if self.tail and self.legs == 4:
#             print('has tails and legs')


# # tom = Dogs()
# # tom.isMammal()

# # print(Horses.__mro__)
# # print(Dogs.__mro__)












# # item = [1,4,7,8]
# # print(list(enumerate(item)))


#  re practicing the twoSum problem with class


# class based way!
# class Number:
#     def __init__(self,L,target):
#          self.target = target
#          self.L = L

#     def twoSum(self):
#         for n in range(len(L)):
#             for x in range(n + 1, len(L)):
#                if L[n] + L[x] == target:
#                    return [n, x]


# L = [3, 4, 6, 1, 7]
# target = 7


# class Number:
#     def __init__(self,L, target):
#         self.L = L
#         self.target = target

#     def twoSum(self):
#             dict = {}
#             for item,  value  in enumerate(L):
#                  if dict.get(value, None) == None:
#                     dict[target - value] = item
#                  else:
#                       return [dict.get(value), item]


# checkTarget = Number(L, target)
# print(checkTarget.twoSum())


# dict = {
#     'age': 30,
#     'occupation': 'Software engineer',
#     'salary': 80000,
#     'desiredincome': 200000,
#     'relationship': 'widowed'
# }

# print(dict.get('age', None))




# nums = (55,44,33,22)

# print(max(min(nums[:2])))


# def power(x,y):
#     if y == 0:
#         return 1
#     else:
#         return x * power(x,  y - 1)
    
    



# print(power(2,3))



# class Call():
#     # Attributes
#     shape = ' '
#     numOfboxes = 0
#     color = ''
#     dimenisons = ''
#     num_of_rows = 0
#     num_of_columns = 0

#     # Methods
#     def grow():
#         pass
#     def reproduce():
#         pass 
#     def die():
#         pass

# class Animal_Cell(Cell):
#     pass

# class Jail_Cell():
#     pass


# # Animal_Cell = Call()

# # Animal_Cell.shape = 'Rectangle'

# # Plant_Cell = Animal_Cell 


# print(Animal_Cell.shape)

# # print(Plant_Cell.shape)  

# # Fundamentals of OOP 
# # 1. Inheritance 
# # 2.Encapsultaion 
# # 3. Abstraction 
# # 4. Polymorphism 



# class Base1(object):
#     def __init__(self):
#         self.str1 = 'Geek1'

# class Base2(object):
#     def __init__(self):
#         self.str2 = 'Geek1'
    
# class Derived(Base1,Base2):
#     def __init__(self):
#         Base1.__init__
#         Base2.__init__
#         print('derived')


#     def printStr(self):
#         print(self.str1, self.str2)

# ob = Derived()

# ob.printStr()


# class Mammal():
#     def __init__(self,name):
#         print(name)

# class canFly(Mammal):
#     def __init__(self, canFly_name)



# class Vehicle():
#     def __init__(self):
#         self.vehicle = 'Truck'
         
# class Car(Vehicle):
#     def __init__(self):
#         self.car = 'Yes'

# class CityRide(Car):
#     def __init__(self):
#         self.cityride = 'Yes'

# class Offroad(Car):
#     def __init__(self):

# class Suv(CityRide, Offroad):
#     def __init__(self):
#         super().__init__()

# ob = Vehicle()
# print(ob)


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name 
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100


class Car(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 20 / 100
        return amount

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount



School_bus = Bus("SchoolVolvo", 12, 50)
Car_obj = Car('Ferrari', 15, 30)
# print(School_bus.fare())

# print(Car_obj.fare())

class Vehicle:
    def __init__(self,name, color,price):
        self.name = name 
        self.color = color
        self.price = price 

    def show(self):
        print('details', self.name, self.color, self.price)
    def maxSpeed(self):
        print('vehicle has a max a speed of 150')
    def change_gear(self):
        print('change gear to 6 gear')
    
class Car(Vehicle):
    def max_speed(self):
        print('car speed is 240')
    def change_gear(self):
        print('car change gear to 7')   
    def is_electric(self):
        print('car is electric')




class Shopping: 
    def __init__(self,basket, buyer):
        self.basket = list(basket)
        self.buyer = buyer
    def __len__(self):
        print('Redifine Length')
        count = len(self.basket)
        return count * 2
    

shopping = Shopping(['Shoes', 'dress'], 'Jessa' )
print(len(shopping))


# for i in range(5):
#     print(i, end =',')

# print()
# for i in range(5,10):
#     print(i, end = ',')

# print()

# for i in range (2, 12, 2):
#     print(i, end = ',')
# print()



# a = 5
# b = 3
# c = a + b
# print(c)


# a ='5'
# b ='3'
# x = a + b
# print(x)



# class Area:
#     def __init__(self,length,breadth,totalarea):
#         self.length = length 
#         self.breadth = breadth
#         self.totalarea = totalarea
#     def squareArea(self,totalarea):
#        return totalarea ** 2

#     def recArea(self,length,breadth):
        
#         return self.length * self.breadth


# # a = Area(4)


# # print(Area.squareArea())

# class Shape:
#     def area(self, a, b = 0):
#         if b > 0:
#             print(a * b)
#         else: 
#             print(a ** 2)

# square = Shape()

# square.area(2)













































