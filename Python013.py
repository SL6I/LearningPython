# String methods
a = "     I Love Python     "
print(len(a))

# strip ,rstrip and lstrip
print(a.lstrip())

a = "####3#I Love Python #@########"
print(a.rstrip("#@"))

# title
b = "I love 2d Graphics etc..."
print(b.title()) # first litter capital

# zfill
c,d,e = "1" , "11", "111"
print(c.zfill(3))
print(d.zfill(3))
print(e.zfill(3))

# upper
name = "sultan"
print(name.upper())

# lower()
name = "SULTAn"
print(name.lower())