# Fun packs
print(1,2,3,4)

myList = [1,2,4]

print(myList)
print(*myList) # 1,2,4

# def sayHello (n1,n2,n3,n4):
#     p = [n1,n2,n3,n4]
#     for n in p:
#         print(n)
        
# sayHello("S","L","6","N")

def sayHello (*people):
    for name in people:
        print(name)
        
sayHello("S","L","6","N",738458) # for any number of arg

def nameAndSkills(*name,job):
    pass