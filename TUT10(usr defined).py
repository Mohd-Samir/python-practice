# def geomean(a , b):
#     mean = (a * b)/(a + b)
#     print(mean)
    
# def isgreater(a , b):
#     if(a > b):
#         print("First no. is greater :",a)
#     else:
#         print("Second no. is greater :",b)
        
# a = 5
# b = 10
# geomean(a , b)
# isgreater(a , b)
        
# c = 99
# d = 1
# geomean(c , d)
# isgreater(c , d)       




# def check_even_odd(number):
#     if(number % 2==0):
#         print("The no. is even") 
#     else :
#         print("The no. is odd")    

# number = int(input("Enter a no."))
# check_even_odd(number)


# def isgreater(a , b , c):
#     if(a >= b and a >= c):
#         print("Greater is a",a)
#     elif(b >= a and b >= c):
#         print("Greater is b",b)
#     else:
#         print("Greater is c",c)
        
# a = int(input("Enter the first no. :"))
# b = int(input("Enter the 2nd no. :"))
# c = int(input("Enter the 3rd no. :"))
# isgreater(a , b , c)                







#####Functon Aurguments

# Defaut Argument
# Keyword Argument
# Variable length Argument
# Required Argument



##example
# def average(a,b):
#     average = (a+b)/2
#     print("The average of two no.'s is: ",average)
    
# a = 10 
# b = 15
# average(a,b)   

##Default Argument
# def add(a=10 , b=10):
#     print("The sum of a and b is",(a+b))
    
# add(a=5)    

def add(a , b=10):
    print("The sum of a and b is",(a+b))
    
add(a=25)  


##Keyword Argument: This technique can be used to change the order
##Require Argument : its states an argument must be definied 

def average(*numbers):
    total = 0
    for i in numbers:
        total = total + i
    print("Average is: ",total/len(numbers))
    
average(4,5,6,7)
