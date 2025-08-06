import requests as r
import json
class bank_account:
    def __init__(self,holder,d):
        self.holder=holder
        self.balance=d['balance']
        self.id=d['id']
    def deposite(self,amount):
        if amount>0:
            self.balance+=amount
            depo_balance={
                "balance":self.balance
            }
            api=f"http://localhost:3000/users/{self.id}"
            am=json.dumps(depo_balance)
            r.patch(api,data=am)
            return f"balance after deposite: {self.balance}"
        else:
            return  "deposite amount should be positive"
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            draw_balance={
                "balance":self.balance
            }
            api=f"http://localhost:3000/users/{self.id}"
            am=json.dumps(draw_balance)
            r.patch(api,data=am)
            return f"balance after withdraw {self.balance}"
        else:
            return 'insufficent balance'
    def balance_display(self):
        return f"current balance {self.balance}"   
name=input('Enter account holder name:')
pin=int(input('Enter pin: '))
api="http://localhost:3000/users"
users=r.get(api)
users_list=users.json()
f=False
for user in users_list:
    if user['name']==name:
        f=True
        d=user
        h1=bank_account(name,d)
if f==False:
    c_id=0
    for user in users_list:
        c_id=int(user['id'])
    id=c_id+1
    id=str(id)
    user_data={
    "name":name,
    "id":id,
    "pin":pin,
    "balance":0.0
    }
    r.post(api,data=json.dumps(user_data))
    print('registered successfully')
else:
    if d['name']==name and int(d['pin'])==int(pin):  
        flag=True
        while flag:
            print('1.Depoiste')
            print('2.Withdraw')
            print('3.Balance')
            print('4.Exit')
            a=int(input('select one of the above options:'))
            if a==1:
                b=int(input('enter deposite amount :'))
                print(h1.deposite(b))
            elif a==2:
                b=int(input('enter withdraw amount :'))
                print(h1.withdraw(b))
            elif a==3:
                print(h1.balance_display())
            else:
                print('Thank you visit again')
                flag=False
    else:
        print('invalid  pin')
    