##DOCTYPE is a type of string which should used just after definition of a function,module,class or method 
#they are associated with the object as their doc attribute. later we use this attribute to retrieve this doc string

def compute_add(a,b):
    '''This function gave the addition of two numbers (a) and (b)'''
    sum = a + b
    print("addition of two numbers is: ",sum)
    
a = 5
b = 10
compute_add(a,b)
print(compute_add.__doc__)