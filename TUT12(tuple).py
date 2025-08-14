# Tuples are immutable

# tup = (1, 2, 3, 4, "sam", "prince")
# print(tup)



# print(tup[0]) 
# print(tup[5])



# if 1 in tup:
#     print(True)
# else:
#     print(False)


# Indexing                         while calculating negative index always consider the total lenth of the variable first
# print(len(tup))
# print(tup[::2])






# ###Operations in Tuple
# tup1 = ("china","india","afghan","pak","sa")
# ###as we know tuple is immutable we can't modify it directly so we need to convert it into a list and then 

# temp = list(tup1)
# temp.append("USA")
# # temp.pop(0)
# temp[1] = "finland"
# print(len(temp))
# tup1 = tuple(temp) #This step ensures that after all changes, tup1 is a tuple again instead of a list.
# print(temp)


# number_1 = (1,2,3,4,5)
# number_2 = (6,7,8,9,10) 
# print(number_1 + number_2)
# print(type(number_1))

numbers = (10,20,20,40,40,50,90,65,100,20,49,55,49)
# res = numbers.count(20)
res = numbers.index(20,4,10)

print("Index of 20 in numbers is:",res)
