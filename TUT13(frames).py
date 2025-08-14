##F-STRING

# str = "my name is {} and i am pursuing {} from {}"   # it have problem such if we exchange the place of variable 
name = "Mohammed Sameer"                              # the value and meaning will completely changed so we have
degree = "CSE"                                        # other kind of f-string for the solution.
college = "T.John institue of technology"
# print(str.format(name,degree,college))


print(f"My name is {name} and i am pursuing {degree} from {college}")


price = 49.5000
txt = f"The price is only {price:.2f} dollars"
print(txt)


print(f"{2*30}")