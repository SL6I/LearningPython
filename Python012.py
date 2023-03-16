# --------------------
# --- String Index ---
# --------------------
MyString = "I am SL6"
print(MyString[0]) # > I
print(MyString[5]) # >> S

# Using minus Number will Start from The Right :
print(MyString[-1]) # > 6
print(MyString[-3]) # > S

# Slicing
# [Start : End]
# [Start : End : steps]
print(MyString[3:7]) # 7 index is not include 
print(MyString[2:])
print(MyString[:4])

print(MyString[:]) # > Full String

print(MyString[::2]) # only even number include 0 index
print(MyString[::3]) # 0 3 6 9 and so that