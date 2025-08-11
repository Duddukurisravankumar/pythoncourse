import json
import random
import string
from pathlib import Path
class Bank:
   
    database = Path("bankmanagement/data.json") 
    data = []
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else: print("file not exists")
    except Exception as err:
        print(f" an {err} error occured")
    
    @classmethod
    def update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
            
    @staticmethod
    def accountnumber():
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits,k=3)
        spech = random.choices("!@#$%^&*",k=1)
        acno = alpha + num +spech
        random.shuffle(acno)
        return "".join(acno)
    
    def createaccount(self):
        acc ={
            "name" : input("tell ur name : "),
            "age" : int(input("enter your age: ")),
            "phno" : input("enter your number"),
            "pin" :int( input("create pin : ")),
            "accnumber" : Bank.accountnumber(),
            "balance" : 0 
        }
        if acc['age']<=18 or len(str(acc['pin']))<4:
            print("sorry u can not crate account")
        else:
            print("account is created successfullyS")
            for i in acc:
                print(f"{i} : {acc[i]}")
            Bank.data.append(acc)
            Bank.update()
    def depositmoney(self):
        acnumber = input("please tell your account number ")
        pasw = int(input("please tell your pin aswell "))

        userdata = [i for i in Bank.data if i['accnumber'] == acnumber and i['pin'] == pasw]

        if userdata == False:
            print("soory no data found")
        
        else:
            amount = int(input("how much you want to depoit "))
            if amount  > 10000 or amount < 0:
                print("sorry the amount is too much you can deposit below 10000 and above 0")

            else:
                userdata[0]['balance'] += amount
                Bank.update()
                print("Amount deposited successfully ")
        
    def withdraw(self):
        acnumber = input("please enter your account number ")
        pasw = int(input("please enter your pin aswell "))

        userdata = [i for i in Bank.data if i['accnumber'] == acnumber and i['pin'] == pasw]

        if userdata == False:
            print("soory no data found")
        
        else:
            amount = int(input("how much you want to withdraw: "))
            if userdata[0]['balance']< amount or amount <= 0:
                print("sorry check your balance once")

            else:
                userdata[0]['balance'] -= amount
                Bank.update()
                print("transtraction  successful ")
    def details(self):
        acnumber = input("please enter your account number ")
        pasw = int(input("please enter your pin aswell "))

        userdata = [i for i in Bank.data if i['accnumber'] == acnumber and i['pin'] == pasw]

        if userdata == False:
            print("soory no data found")
        
        else:
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")
        
    def updatedetails(self):
        acnumber = input("please enter your account number ")
        pasw = int(input("please enter your pin aswell "))

        userdata = [i for i in Bank.data if i['accnumber'] == acnumber and i['pin'] == pasw]

        if userdata == False:
            print("soory no data found")
        
        else:
            print("select he details you vant to update:\n","1.name\n","2.passward\n","3.phone no\n")
            ch = int(input("enter your choice: "))
            if ch == 1:
                upname = input("enter your new name: ")
                userdata[0]['name'] = upname
                Bank.update()
                print("transastion successful")
            elif ch == 2:
                uppasw = int(input("set your new passward: "))
                userdata[0]['pin'] = uppasw
                Bank.update()
                print("transstation succesufful")
            elif ch ==3:
                ph = input("enter new ph number: ")
                userdata[0]["phno"] = ph
                Bank.update()
            else:
                print("select the correct option")
                return
                
                
    def deletaccount(self):
        acnumber = input("enter your acc ount number: ")
        pasw = int(input("enter your passward : "))
        userdata = [i for i in Bank.data if i['accnumber'] == acnumber and i['pin'] == pasw]
        if userdata is False:
            print("enter correct deatils")   
        else:
            print(" enter y to delet\n","enter n for not\n")
            check = input()
            if check == "y" or "Y":
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.update()
                print("transaction completed")
            else:
                print("thanks for using our bank")
            
user = Bank()
print("1.accountcreation\n","2.deposit\n","3.withdraw\n","4.details\n","5.updatedetails\n","6.deletaccount\n")
ch = int(input("enter your choice: "))
if ch==1:
    user.createaccount()
if ch==2:
    user.depositmoney()
if ch==3:
    user.withdraw()
if ch==4:
    user.details()
if ch==5:
    user.updatedetails()
if ch==6:
    user.deletaccount()
    