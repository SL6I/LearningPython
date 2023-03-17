# String methods # 3

# index(sub,start,end)
a = "I love Python"
print(a.index("l"))
# print(a.index("l",0,1)) #Error
print(a.find("l",0,1)) # if its not exists -1

# rjust(width,fill char) ljust()
a = "Sultan"
print(a.rjust(20,"#"))

# splitlines()
e = """First line
second
third"""
print(e.splitlines())

# expandtabs()
a = "I\tLove\tPython"
print(a.expandtabs(10))

one = "I Love Python And 3G"
print(one.istitle()) # check

three = ""
print(three.isspace()) #False

five = "I love Python"
print(five.islower()) # if one is upper > False

seven = "Osama ma"
eight = "SL6"
print(seven.isidentifier())
print(eight.isidentifier())

x = "AAAAAAAAAA30AAAAAAA"
print(x.isalpha())
y = "AAAAAAAAA123"
print(y.isalnum())
