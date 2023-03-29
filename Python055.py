#

o = {
    "Java" : "hi%",
    "Python" : "40%"
}
# for skill in o :
    # print(o[skill])
    
    
# old way

for skilll ,v in o.items():
    print(skilll,v)
    
    
n = {
    "S" : {
      "aaaaa":"Sss"
    },
    "w" : {
        "hi" : 1
    },
    "t":{
        "q":999
    }
}

for x , xx in n.items():
    for c,d in xx.items():
        print(c)