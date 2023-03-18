# String formatting

name = "Sultan"
age = 20
rank = 5

print("My name is "+name)
# print("My name is "+name+ "And my age is +"age) #Error
print("My name is %s and my age is %d"%(name, age))
print("My name is %s and my age is %d and my rank is %f"%(name, age,rank))

n = "Sultan"
l = "Python"
y = 0.6

print("I'm %s and I like %s and %d" %(n,l,y))

# control float numbers
n = 10
print("num %f" %n) # .0000000
print("num %.2f" %n)

# Truncate string
long = "Hello everyone and welcome here"
print("Message is %.10s" %long) # 10