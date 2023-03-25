# Dict

# Key : Value
# Key should be immutable that means You cannot add [] as a key
# Key should be unique
user = {
    "Name" : "SL6",
    "age" : 20,
    # [1,2,3] : "Error"
    True : [1,2,3   ],
    "Name" : "SLL6" # it will take the last update for the key
}

#  Not order
print(user["Name"])
print(user.get("Name"))

print(user.keys())
print(user.values())

exp = {
    "One" :{
        "lang" : "Python",
        "pro" : "39%"
    }
    
}
print(exp.get("One").get("lang"))
print(exp["One"]["lang"])

f = {
    "hi" : "Bye",
    "ff" : "jjj"
}
ff = {
    "mdre" : f
}
print(ff)