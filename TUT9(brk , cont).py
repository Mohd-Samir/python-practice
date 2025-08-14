##Here the break statement is used to stop or termninate the loop
##Where as Continue statement is used to stop the particualr iternation and continue executing the next..



###Break_Condition::                       ##if break is applied before print stmt it print from 0-4 and then breaks
# for i in range(0,12):                       ##if break is applied after print stmt it print from 0-5 and then breaks 
#     print("5 *",i,"=",5*i)
#     if(i==5):
#         break
# print("End of the loop and came out from it")    



# for i in range(1,101,2):
#     print(i, end = ",")
#     if(i==50):
#         break
#     else:
#         print("Improve")
# print("thankyou")        











    
    
####Continue_Condition:
for i in range(0,12):  #This will skip printing 5 * 5 because when i == 5, it hits continue and skips the print line.
    if(i==8):
        print("itration skipped")#if printed after the print condn This doesn't change anything, because the continue is after the print,so it has no effect.
        continue
    print("6 *",i,"=",6*i)
    