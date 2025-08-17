# x = int(input("Enter the day number from(1-7): "))
# match (x):
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid DayNumber")
        
        
        
# balance = 100
# amount = int(input("Enter the amount: "))
# print("1.Check Balance")
# print("2.Deposit Money")
# print("3.Withdraw Money")
# print("4.Exit")

# x = int(input("Select on of the 4 options: "))
# match x:
#     case 1:
#         print("The balance amount is:",balance)
#     case 2:
#         if amount > 0:
#             balance += amount
#             print("The new amount after deposit is:",balance)
#     case 3:
#         if amount <= balance and amount > 0:
#             balance -= amount
#             print("The balance after withdrawal is:",balance)
#         else:
#             print("Insufficient Balance")
#     case 4:
#         print("Thank you for using Match-Case ATM!")

#     case _:
#         print("Invalid choice. Please enter a number between 1 and 4.")



x = int(input("enter the first number: "))
y = int(input("enter the second number: "))
print("1.'+'")
print("2.'-'")
print("3.'*'")
print("4.'/'")
z = int(input("select one of the four operations: "))
match(z):
    case 1:
        print("The result of x and y is: ",x+y)
    case 2:
        print("The result of x and y is: ",x-y)
    case 3:
         print("The result of x and y is: ",x*y)
    case 4:
         if(y!=0):
             print("The result of x and y is: ",x/y)
         else:
             print("Division by zero is not allowed")    
    case _:
        print("invalid choice")  
        