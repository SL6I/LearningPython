#------Tuple------
#      -----

# Tuple with one Element
myT = ("SL6") # Do You think Its a Tuple?
myTT = "SL6"
print(myT)
print(myTT)
print()
print(type(myT))
print(type(myTT))


myT = ("SL6",) # Do You think Its a Tuple?
myTT = "SL6",
# The Comma changed Everything
print(myT)
print(myTT)
print()
print(type(myT))
print(type(myTT))


# Tuple Concat
a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
c = a+b
d  = a + ("boring",)+c # The Comma is important
print(d)

# (*)
myString = "Sultan"
myList = [1,0,2,3]
myTuple = "A","B"

print(myString * 3)
print(myList * 3)
print(myTuple * 3)

# Method count()
t = (1,2,3,2,3,23,23,3,2,2,3)
print(t.count(2))

# index()
t = (1,2,3,2,3,23,23,3,2,2,3)
print(t.index(2))

# Tuple destruct
a = ("6FSH","MNGD",2)
X,Y = a
print(X)
print(Y)