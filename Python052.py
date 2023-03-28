# for

myR = range(1, 100) # > Like Random in java Not sure

for n in myR:
    print(n)
    
    


mySkills = {
    "H" : "91%" , "P" : "50%"
}
print(mySkills["H"]) 

for s in mySkills:
    print(f"{s} is {mySkills.get(s)}")