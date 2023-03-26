# Slice Email

Name = input("Enter Your Name: ").strip().capitalize()
Email = input("Enter Your email: ").strip()
userName = Email[:Email.index("@")].capitalize()
domine =  Email[Email.index("@") + 1:]
print(f"Your name is {Name}\nYour User name is {userName}\nYour domine is {domine}")