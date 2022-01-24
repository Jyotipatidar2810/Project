ch=input("Enter the first name:-")
ch=input("Enter the last name:-") 
user_name=input("enter user name:-")
if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
    print("Next")
    date=int(input("enter the date"))
    month=input("enter the month")
    year=int(input("enter the year"))
    if date==1-9 or month=="a-z" or year==2022:
        print("correct")
        gender=input("Enter your gender")
        if gender=="female" or gender=="male":
            language=input("Enter the language")
            if language=="English":
                number=int(input("Enter ten digit mobile number"))
                if (number >=0 or number <=9):
                    print(+91,number)
                    if len(str(number)) ==10:
                        OTP=int(input("enter the OTP"))
                        if len(str(OTP))==6:
                            print("Confirm")
                            passward=input("Enter the passward")
                            if passward>="a-z" or passward<="A-Z":
                                special_char=input("enter the special character")
                                if special_char=="@"or"$"or"#":
                                    numeric=int(input("Enter the number"))
                                    if numeric>=1:
                                        print(passward+special_char+str(numeric))
                                        login=input("Do you want to log in")
                                        if login=="yes":
                                            print("Your facebook account is successfully created,Thankyou")
                                        else:
                                            print("Unsuccessful")
                                    else:
                                        print("Invalid")
                                else:
                                    print("It is not special character")
                            else:
                                print("It is not latter")          
                        else:
                            print("Resand OTP")      
                    else:
                        print("Enter correct mobile number")
                else:
                    print("Invalid")
            else:
                print("Incorrect language")
        else:
            print("Incorrect gender")            
    else:
        print("error")           
else:   
    print("Wrong character")