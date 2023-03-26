# # 1. flatten list
nestedList = [[1, 2], 3, [4], 5, [6, 7, [8, 9, [10]]]]

flatList = []


def flattenList(nestedList):
    #  iterate through each item in the list
    for i in nestedList:
        # if item is in the  list then call the function by itself with the i from for loop
        if type(i) is list:
            # call the function with itself with i from the for loop
            flattenList(i)
        else:
            # add it to the list
            flatList.append(i)
    return (flatList)


print(flattenList(nestedList))


# flatItems = [i for i in nestedList if type(i) is list  flatList.extend(i)]
# print(flatItems)

# 2. return duplicates
# test case  ---> Input: [4,9,1,2,1,3,1,8,8,8,2,2,2] ---> Output: [1,2,3,4,8,9]
numInput = [4, 9, 1, 2, 1, 3, 1, 8, 8, 8, 2, 2, 2]


def sortNum(numInput):
    newList = []
    # iterate over each item in input
    for n in numInput:
        # if n not in newList add it to the List
        if n not in newList:
            # add it to the newList
            newList.append(n)
        # sort the list and return!
    return sorted(newList)


# print(sortNum(numInput))


# 3.
input = (5, 20, 3, 7, 6, 9)


def sum(input):
    # declare sum variable
    sum = 0
    # iterate through each num
    for i in input:
        # add each number
        sum += i
    return (sum)

# print(sum(input))


# 4
tupleInp = ([7, 5, 4], [8, 2, 4], [0, 7, 5])

# test case ---> input ([7, 5, 4], [8, 2, 4], [0, 7, 5]) --->  Output: ( [4, 5, 7], [2, 4, 8], [0, 5, 7] )


def output(tupleInp):
    newTuple = ()
    # loop through each item in tuple
    for t in tupleInp:
        odrItems = (sorted(t))
        print(list(odrItems))

# print(output(tupleInp))


# 5. Input: { 8, 16, 24, 1, 25, 3, 10, 65, 55 } --> max(65) min(1)

setInput = {8, 16, 24, 1, 25, 3, 10, 65, 55}


def maxMin(setInput):
    minNum = min(setInput)
    maxNum = max(setInput)
    return "Max Number: ", maxNum, "Min Number: ", minNum

# print(maxMin(setInput))


# 6. Input: “helloworld” ----> Output: 7
def countWords(words):
    word = {}
    # loop through the words
    for w in words:
        # if word not in the obj yet then add
        if w not in words:
            word[w] += 1
        else:
            word[w] = 1
    print(len(word))

# countWords("helloworld")


# 7.  Input: { ‘a’: 100, ‘b’:200, ‘c’:300 } --> Output: True
obj = {'a': 100, 'b': 200, 'c': 300}


def oddEven(obj):
    sum = 0
    #  convert dict into list
    newList = list(obj.values())
    # iterate through each item in the list
    for i in newList:
        sum += i
        if sum % 2 == 0:
            return True
        else:
            return False


# print(oddEven(obj))

# 8. Prime or not. Input: 5 ---> Output: True

def primeOrNot(n):
    if n > 1:
        # iterate over the num in range loop
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
            return True
        else:
            return False


# print(primeOrNot(7))

# 9. Input: 3,1,6 ---> Output: 6


def largeNum(number):
    bigNum = sorted(number)
#     print(bigNum[-1])

# largeNum([3, 1, 6])

# 10. The zip function returns a zip object, which is an iterator of tuples where the first item in each assed iterator
# is paired together andd the second item n each passed iterator are paired together.


# zip
list1 = [1, 2, 3, 4]
list2 = [4, 3, 2, 1]
z = zip(list1, list2)
z = list(z)
# print(z)

# unzip
unzip = list(zip(*z))
# print(unzip)
