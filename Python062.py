# SCOPE


x = 1 # Glopal

def f():
    x = 2 # Local
    
def gg():
    global x #######
    x = 10
    print(f"{x}")
    

gg()
print(x)
    