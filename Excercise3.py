name = input("enter your name: ")
print("Welcome to Kaun Banega Crorpati: ",name)


question=[{"question": "When did RCB win its first title?", "options": ["2020", "2021", "2023", "2025"], "answer": 4}
        #    ,{"question": "Who won the first IPL in 2008?", "options": ["RCB", "CSK", "RR", "MI"], "answer": 3}
]

for values in question:
    print(question("question")
    values["answer"]
    
choice = int(input("Choose one of four options(1-4): "))
if(choice == values["answer"]):
    print("your answer is correct")
    print("your amount is:10000rs")
else:
    print("sorry,your answer is wrong")
    print("your amount is:0rs")
