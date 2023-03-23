# ------Method Lists P2-------
#       ---------------

# clear()
a = [1, 2, 3, 4]
a.clear()
print(a)

# copy
b = [1, 2, 3, 4]
c = b.copy()
print(b)
print(c)
b.append("hi")
print(b) # Changed
print(c) # didn't change

# count()
d = [1,2,3,4,5,6,24,1,2,3,2,]
print(d.count(1))
print(d.count(2))

# index()
c = ["SL6","Ali","Saad","Anas","Ali"]
print(c.index("Anas")) # First one

# insert(index,element) # Before
i = [1,2,3,4,5,6,7,8,9]
i.insert(0,4) 
i.insert(-1,"WTFNot last index")
print(i)

# pop()
s = [1,2,3,"a"]
print(s.pop(1))

