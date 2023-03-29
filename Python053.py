# Nested loop

m =['sl6','ali','saad']
s = ['python','java']

for n in m :
    for ss in s:
        print(f"{n} has a {ss} skill")
        
        
a = {
    "Sl6" : {
        "Python" : "40%",
        "java" : "44%"
    },
    "ALi" : {
        "7sab" : "50%"
    }
}
# print(a["Sl6"]["Python"])

for name in a:
    # print(name+ "has")
    
    for c in a[name]:
        print(f"{name} Has {c} and {a[name][c]}")