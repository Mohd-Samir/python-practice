lst = ["science","maths", "social","hindi","english","kannada"]
# print(lst)
# print(type(lst))
# if "science" in lst:
#     print("yes")
# else:
#     print("no")    

# print(lst[0])

# lst[1] = "computers"
# print(lst)

## List comprehension

# number1 = [i*i for i in range(10)]
# print(number1)

# numbers = [i*i for i in range(10) if i%2==0 ]
# print(numbers)

# numbers = [1,2,3,4,5]
# new_list = [num**2 for num in numbers if num%2==0]
# print(new_list)

# words = ["apple", "banana", "cherry", "date"]
# new_list = [len(word) for word in words]
# print(new_list)

# numbers = [10, 15, 20, 25, 30, 35]
# new_list = [num/5 for num in numbers if num >20]
# print(new_list)

numbers = [3, 8, 12, 15, 20, 27, 30, 33, 40]
new_list = [num**2 for num in numbers if num%2==0 and num>10]
print(new_list)