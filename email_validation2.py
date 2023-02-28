# practicing by myself #email_validation

email = input("Enter Your Email Address : ")
k = 0
j = 0
d = 0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():  # w-- W==w
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email, Please enter correct email")
                else:
                    print('Right Email')
                    
            else:
                print("Wrong Email, please use .com and .in only")
        else:
            print("Wrong Email, please use @ one time only")
    else:
        print('Wrong Email, Please use all lowercase charaters')
else:
    print("Wrong Email, please enter more than 6 character first")