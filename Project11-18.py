name = "Sultan"
age = "20"
country = "SA"
print('"Hello \' '+name+ '\' \n, How are u doing \\""" your age is "'+age+'\n\"\" + and yor country is:'+country)
name = 'Elzero'
print(name[1])
print(name[2])
print(name[len(name)-1])
# ------------------
print(name[1:4])
print(name[::2])
name = "#@#@Elzero#@#@"
print(name.strip("#@"))

num = "9"
num2 = "15"
num3= "130"
num4 = "950"
num5 = "1500"
print(num.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))

name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20,"#"))

name_one = "OSamA"
print(name_one.swapcase())

msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))

name = "Elzero"
print(name.index("z"))

msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","Love",1))

print(msg.replace("<3","Love"))

name = "Osama"
age = 38
country = "Egypt"
print(f"My Name Is {name}, And My Age Is {age}, And My {country} Is Egypt")
