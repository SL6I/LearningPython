# Type conversation

# str()
a = 10
print(type(a))
print(type(str(a)))

# tuple()
s = "SL6"
l = [1,2,3]
se = {1,2,3}
dic = {1 : "Hi",2 : "Bye"}

print(tuple(s))
print(tuple(l))
print(tuple(se))
print(tuple(dic)) # Take only the key
# print(tuple(500)) Error we cant convert int to tuple

# list()
# is the same


# set() 
# The same but the Order always change



# dict()
# s = "SL6"
l = [[1,"One"],["Two", 2]]
# se = {1,2,3}
t = (("a",1),("n",2)) # Key and val

# print(dict(s)) Error there is no key or val
print(dict(l))
# print(tuple(se)) ################Error because it's change##########
print(dict(t))