# Set Method p3


#   issuperset()
a = {1,2,4,3}
b = {1,2, 4}
print(a.issuperset(b))


# issubset()
c = {1,2,3}
d = {1,2,3}
print(d.issubset(c)) # d is


# isdisjoint()
e = {1,2,3}
f = {4,6}
print(f.isdisjoint(e)) # if there are no similar elements True
