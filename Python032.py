# Dict Method p2

a = {
    "Name" : "SL6"
}
print(a)
a.setdefault("Name","N")
print(a)
a.setdefault("Name2")
print(a)

# popitem() Last item You added
a = {
    "age" : 20
}
print(a.popitem()) #####
a[20] = 10
print(a)
print(a.popitem())


# Items > all keys and value

# fromkeys()

a = ("morning","afternoon","evening")
z = "DAY"
print(dict.fromkeys(a,z))
x = dict.fromkeys(z,a)
print(x)
