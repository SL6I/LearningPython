# while training

myF = ['a','b','c','d','e']
a = 0

while a <= len(myF)-1:
    print(f"#{str(a+1).zfill(2)} {myF[a]}")
    a += 1 
else:
    print("IDk")