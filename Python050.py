# Loop training 3

t = 4
passs = "Sl6"
user = input("Enter the pass")
while user != passs and t >= 0 :
    user =  input(f"Enter the pass {'Last' if t == 0 else t} ")
    t -= 1
    
    # if t == 0:
        # break 
    
    
else:
    print("correct pass") # if while False will come here