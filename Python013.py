# String methods
a = "     I Love Python     "
print(len(a)) # the length of a

# strip ,rstrip and lstrip
print(a.lstrip()) # like trim in java

a = "####3#I Love Python #@########"
print(a.rstrip("#@"))

# title
b = "I love 2d Graphics etc..."
print(b.title()) # first litter capital

# zfill
c,d,e = "1" , "11", "111"
print(c.zfill(3)) # 001
print(d.zfill(3)) # 011
print(e.zfill(3)) # 111

# upper
name = "sultan"
print(name.upper())

# lower()
name = "SULTAn"
print(name.lower())