###If - Else statements

# a =int(input("Enter the age: ")) 
# print("The age is:", a)
# if(a<18):
#     print("This person cannot vote")
# else:
#     print("This has rights to vote")



###Elif statement:     another example negative equals and positive.
# print("Enter the values of the number")
# a = int(input("Enter the value of 1st no."))
# b = int(input("Enter the value of 2nd no."))
# c = int(input("Enter the value of 3rd no."))

# if(a>b & a>c):
#     print("greatest is \'a':",a)
# elif(b>a & b>c):
#     print("greatest is \'b':",b)
# else:
#     print("greatest is \'c':",c)




###Nested if statement

# num = 20
# if(num < 0):
#     print("Number is negative")
# elif(num > 0):
#     if(num <= 10):
#         print("Number is between 1-10")
#     elif(num > 10 & num <= 20):
#         print("Number is between 1-20")
#         if(num == 20):
#             print("Number is equal to 20")
#     else:
#         print("Number is greater than 20")
# else:
#     print("Number is negative")
            

    
        ##example program if else

import time
current_hour =int(time.strftime("%H"))

timestamp =time.strftime("%H:%M:%S")
print(timestamp)

x = current_hour
if(0 <= x < 12):
    print("Good Morning")
elif 12 <= x < 17:
    print("Good Afternoon")
elif 17 <= x < 21:
    print("Good Evening")
else:
    print("Good Night")
    
    
    