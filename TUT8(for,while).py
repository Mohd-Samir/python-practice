###String example

# x = "samir"
# for i in x:
#     print(x)
    
    
##Lists example
# names = ["sameer","toufiq","amaan","ali"]
# for name in names:
#     print(name)
#     for i in name:
#         print(i)    
    


##range
# for i in range(0,6):
#     print(i)


    
    #####WHILE LOOP
    
    
# i = int(input("Enter a num: "))
# while(i < 10):
#     print(i)
#     i = i+1
# else:
#     print("end of the loop")


# i = 0
# while(i <= 15):
#     i = int(input("Enter a number: "))
#     print(i)
    
# print("end of the loop")


# count = 5
# while(count > 0):
#     print(count)
#     count = count-1
    
###Do while:                   it runs the code atleast once then checks the condn whether to stop/continue.
i=5
while True:
    print("Number :",i)
    i = i-1
    if(i<0):
        break