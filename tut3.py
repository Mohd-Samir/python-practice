####LIST  it will always display in [square brackets].
##they are mutable means we can alter the values in LISTS
##STUDYING 3 THINGS LISTS TUPLES AND SWAPPING OF TWO ELEMENTS........



#grocery = ["tooth brush", "vim bar", "sugar", "grains", "rice"]
#print(grocery[0])

# numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
# numbers.sort()
# print(numbers)



#we cant directly reserve or sort the list in print statement so first we do that function then we will print.
# numbers.reverse()
# print(numbers[2])
# print(numbers)


#slicing in lists


# print(numbers[0:9])   ##prints no's from 2 to 7

#print(numbers[::1])     ##prints the same no's as there in the list remember before 1st colan the 
                        ##default value will be zero aftr 1st colon default value will the nth value 
                        ##and after the 2nd colon default value will be 1. 

#numbers.append(22)
#print(numbers)          ##append is used to add a number at the end.

# numbers.insert(4,0)      ##this is used to insert any no. in the middle 
# print(numbers)



###Tuple                 it will be written in (parantheses) they are immutable 

# tp = (1,2,3)
# print(tp)

tp = (1,)                #for single value add comma , then it will be considered as tuple.
print(tp)


##if we want to swap the values like a for b , and , b for a

a = 10
b = 5

## tradionally we Use
# temp = a
# a = b
# b = temp 
# print(a,b)   we can also wriye in simple way 

a , b = b , a
print(a,b)

