# # 1. flatten list
nestedList = [[1, 2], 3, [4], 5, [6, 7, [8, 9, [10]]]]

flatList = []
newList = []

# incomplete


def flattenList():
    # iterate over each item in the list
    for item in list:
        if type(item) == int:
            # push item into a new list
            newList.insert(-1, item)
            list.append(newList)
            print(list)

# flattenList()


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
# incomplete


def output(tupleInp):
    newTuple = ()
    # loop through each item in tuple
    for t in tupleInp:

        odrItems = (sorted(t))
        print(odrItems)
        # newItem = newTuple.insert(odrItems)
        # print(newItem)

# print(output(tupleInp))


# 5. Input: { 8, 16, 24, 1, 25, 3, 10, 65, 55 } --> max(65) min(1)

setInput = {8, 16, 24, 1, 25, 3, 10, 65, 55}


def maxMin(setInput):
    minNum = min(setInput)
    maxNum = max(setInput)
    return "Max Number: ", maxNum, "Min Number: ", minNum

# print(maxMin(setInput))


# 6. Input: “helloworld” ----> Output: 7


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
num = 1

def primeOrNot(num):
    if num % num == 0: 
        return True 
    else: 
        return False 
        
print(primeOrNot(num))




