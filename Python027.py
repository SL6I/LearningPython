# Set methods

# clear()
sett = {1,2,3}
sett.clear
print(sett)

# union()
a = {1,2,4}
b = {"A","MA"}
print(a |b)
print(a.union(b))

# add(Take one arg)


# Copy(shallow)

# remove(If the number not exsist ERROR)
# discard() withour error

# pop()
a  = {1,"hh",4}
print(a.pop()) # Random Element


# update() Like the union
a = {1,4,"a"}
b = {"a",4,"Ok"}
a.update(b)
a.update(["IDK ","HOW "])
print(a)
