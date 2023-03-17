# String methods #2

#split | rsplit
a = "I love Python and PHP"
print(a.split())

a = "I love Python and PHP"
print(a.split(" ",2)) # 2 is maximma

# rsplit from right

# center
a = "Sultan"
print(a.center(9)+"test") # Spaces
print(a.center(9,"#")+"test")
print(a.center(16,"$")+"test")

# Count
a = "I love Python"
print(a.count("o"))
print(a.count("o",0,6)) # Case sensitive

# swapcase
a = "I love PyTHon"
print(a.swapcase())

# startswith()
a = "I love Python"
print(a.startswith("I")) # True | False
print(a.startswith("P",7,))

# endswith()
a = "I love Python"
print(a.endswith("n")) # True | False
print(a.endswith("P",0,8))