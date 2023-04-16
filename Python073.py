# filter is like map but it a little different let's see small exp



# filter with lampda
names = ["ALI","AMEER","ANA", "SAAD"]
result = filter(lambda n : n[0] == "A", names)
for i in result:
    print(i)