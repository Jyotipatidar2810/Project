print("please enter your card")
print("WELCOME TO SBI ATM")
pin=(input("enter you card pin:-"))
balance=5000
pin=len(str(pin))==4
if len(str(pin))==4:
    if pin==1000 or 9999:
        print("""
        1==balance 
        2==withdraw amount 
        3==deposit amount 
        4==exit
        """
        )
    try:
        option=int(input("please enter your choice"))  
    except:
        print("please enter valid option")  
    
    if option==1:
        print("your current balance is",balance)
    if option==2:
        withdrawal_amount=int(input("please enter your withdrawal amount"))
        balance=balance-withdrawal_amount
        print(withdrawal_amount,"is deposited to your account")
        print("your current balance is",balance)
    if option ==3:
        deposit_amount=int(input("please enter your deposit amount"))
        balance=balance+deposit_amount
        print(deposit_amount,"is credited to your account")
        print("your updated balance is",balance)
    if option==4:
        print("exit")

else:
    print("wrong pin please try again")


