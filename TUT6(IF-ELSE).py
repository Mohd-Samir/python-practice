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

# if(a>=b & a>=c):
#     print("greatest is \'a':",a)
# elif(b>=a & b>=c):
#     print("greatest is \'b':",b)
# else:
#     print("greatest is \'c':",c)




###Nested if statement

# num = -0.5
# if(num < 0):
#     print("The number is negative")
# elif(num > 0):
#     print("The number is positive")
#     if(num > 0 and num <= 10):
#         print("The number is between 1-10")
#     elif(num > 10 and num <= 20):
#         print("number is between 11-20")
#     elif(num > 20):
#         print("The number is greater than 20")
#     else:
#         print("The number is negative")


            
# person = int(input("What is your age: "))
# print("My age is: ",person)  
# license_status = input("what is the status of the license (YES/NO): ")
# x = "have license"
# y = "doesn't have license"  
# if(person >= 18):
#     print("age of the person is greater than 18")
#     if(person >= 18 and license_status == "YES"):
#         print("you can drive")
#     elif(person >= 18 and license_status == "NO"):
#         print("you need to buy license and then you can drive")
# else:
#     print("you can't drive")
    
    

    
        ##example program if else

import time
current_hour =int(time.strftime("%H"))
timezone = time.strftime("%H:%M:%S")
print(timezone)
x = current_hour
if(0 <= x < 12):
    print("Good Morning")
elif 12 <= x < 17:
    print("Good Afternoon")
elif 17 <= x < 21:
    print("Good Evening")
else:
    print("Good Night")
    
    
    