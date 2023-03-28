# While training 2

myF = []
max = 5
a = 1
while max > 0:
    web = input("Website name: ")
    
    myF.append(f"https//{web.strip().lower()}")
    
    max -= 1
    print(f"{a} {myF}")
    a += 1
else:
    print("Done")
    
    
if len(myF) > 0: # order
    myF.sort()
    print(myF) 
    index = 0
    while index < len(myF):
        print(myF[index])
        index += 1