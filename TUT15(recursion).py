# def factorial(num):
#     if(num == 0 or num == 1):
#         return(1)
#     else:
#         num = num * factorial(num-1)
#         return(num)
        
# num = 3
# print(factorial(num))

        
def fibonacci(n):
    if(n==0):
        return(0)
    elif(n==1):
        return(1)
    else:
        n = (fibonacci(n-1) + fibonacci(n-2))
        return(n)
n = 2
print(fibonacci(n))        
        