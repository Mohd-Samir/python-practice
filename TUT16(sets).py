# SETS they are defined in curly{} braces 
# sets are unordered collection of data items. regular sets are mutable not changable but the frozen sets are immutable,
# and do not contain duplicate items


#1.
# s = set()          ##if we use only {} to create an empty set it becomes dictionary so,
# print(type(s))   ###we use set function with parenthesis to define an empty set.

#2.
# s = {1,2,3,4,5.2,6,8,4,10}
# # print(s)

# #3.
# # for accessing
# for values in s:
#     print(values)
    
    
    
###4. Sets Methods

#1. UNION
# cities1 = {"madrid","columbia","berlin","tokyo","denver"}   
# cities2 = {"chicago","delhi","columbia","denver","tokyo"}
# # print(cities1.union(cities2))
# cities1.update(cities2)  #it prints the value of cities1 along with the values of cities2 as update value
# print(cities1,cities2)                     #prints updated value of cities1 and the values of cities2
     
    


#2. INTERSECTION
cities1 = {"madrid","columbia","berlin","tokyo","denver"}   
cities2 = {"chicago","delhi","columbia","denver","tokyo"}
# x=cities1.intersection(cities2)
# print(x)
# cities1.intersection_update(cities2) 
# print(cities1)

#3. SYMMETRIC
# if A and B are two sets then its symmetric will be:
#     (A - B) U (B - A) orally: (elements in A but not in B) U (elements in B but not in A)

# number_1 = {1,2,3,4,5,8,9,0}                     #A-B = {5,0}  B-A = {6,10}
# number_2 = {2,4,6,8,9,10,1,3}                    #output:{0, 5, 6, 10}
# # print(number_1.symmetric_difference(number_2))              #.symmetric_difference()	✅ Yes	❌ No
# number_1.symmetric_difference_update(number_2)           ##.symmetric_difference_update()	❌ No (returns None)	✅ Yes
# print(number_1)                                    #output :{0,5,6,10} assigned to number_1



#4. isdisjoint returns boolean value as true if there is no intersection 
# cities1 = {"madrid","columbia","berlin","tokyo","denver"}   
# cities2 = {"chicago","delhi","columbia","denver","tokyo"}
# print(cities1.isdisjoint(cities2))                #output:False


cities1 = {"madrid","columbia","berlin","tokyo","denver"}   
cities2 = {"chicago","delhi"}
print(cities1.isdisjoint(cities2))     #output:True