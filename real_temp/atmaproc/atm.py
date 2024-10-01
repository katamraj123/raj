name= "raj"
password = "123"
users = input("enter the user_name:")
passwords = input("enter the pass_word:")
opt = '''
    1.credit
    2.debit
    3.ministatment
    4.exit
'''
Amount=10000
if name == users and password == passwords:
    print(opt)
    while True:
        option = int(input("enter the option:"))
        if option ==1:
            credit_amount=int(input("enter the credit_amount:"))
            print(Amount+credit_amount)
        elif option ==2:
            debit_amount=int(input("enter the debit_amount:"))
            print(Amount-debit_amount)
        elif option ==3:
            print(Amount)
        elif option ==4:
            exit
        else:
            print("check the option and try again")
        
else:
    print("invalid credentials")