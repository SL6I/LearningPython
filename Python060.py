# def s(*name):
#     for n in name:
#         print(n)
        
        
# s("Hi","bye")




dd = {
    "O" : 1,
    "s" :2
}
def dict(**nameSkills):
    print(type(nameSkills))
    for name,skill in nameSkills.items():
        print(f"{name} Has {skill}")
        
        
dict(**dd)
dict(a = "hi",b = "bye")