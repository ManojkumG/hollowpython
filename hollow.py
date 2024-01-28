a = 5 
for i in range(a):
    if i == 0:
        print("+ "*a)
    if i == (a-1):
        left_space = " "* i
        print(left_space+"*")
    else:
        left_space = "  "* i
        hollow = " "* (a - i) 
        print(left_space + "* " + hollow + " *")