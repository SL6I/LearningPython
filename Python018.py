# String formatting new way


name = "Sultan"
age = 20
rank = 5
print("My name is {} and my age is {}".format(name,age))
print("My name is {:s} and my age is {:d} and my rank is {:f}".format(name,age,rank))

n = "Sultan"
l = "Python"
y = 0.6

print("I'm {} and I like {} and {}" .format(n,l,y))

# control float numbers
n = 10
print("num {:d}" .format(n)) # .0000000
print("num {:f}" .format(n))
print("num {:.2f}" .format(n))

# Truncate string
long = "Hello everyone and welcome here"
print("Message is {:.10s}" .format(long)) # 10 char


# Format money

myMoneyinDream = 54939292183
print("My money {:_}" .format(myMoneyinDream))
print("My money {:,}" .format(myMoneyinDream))
# not all char are available

# ReArrange Items
a,b,c = "One" , "Two" , "three"
print("my {} {} {}" .format(a,b,c))
print("my {1} {2} {0}" .format(a,b,c))

x,y,z = 10,20,30
print("my {} {} {}" .format(x,y,z))
print("my {1} {2} {0:.2f}" .format(x,y,z))


# Format in version 3.6+

myName = "Sultan"
myAge = 20
print(f"My name is : {myName} and my age is {myAge}")



