# ------Method Lists-------
#       ------------

# append()
myFriends = ["Saad","Anas","Fawas"]
ages = [20,22,21]
myFriends.append("Abobkr")
myFriends.append([10])
myFriends.append(ages)
print(myFriends)
print(myFriends[-1]) # As one Element
print(myFriends[-1][1]) # 1 is inside the Last Element

# extend() : Its like +
# As one List
a = [1,2,3,4]
b = ["A","B","C"]
a.extend(b)
print(a)

ab = [1,2,3,"ALI","ALI",True,"ALI"]
ab.remove("ALI") # Just remove the first one
print(ab)

# sort()
z = [1,2,5,-1,-9,10,20,False] # Do not support by String With Int
x = ["C","A","B"] # its Okay
x.sort()
print(x)
z.sort() # sort(reversed = True )
print(z)

# reverse()
k = [1,2,5,-1,-9,10,20,False,"Bye",1]
k.reverse()
print(k)