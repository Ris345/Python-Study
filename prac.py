
#  1.stuttering function
#  level super easy
# test cases stutter("incredible") ➞ "in... in... incredible?"
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
