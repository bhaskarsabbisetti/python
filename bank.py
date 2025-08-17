import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Bhaskar_6281',
    database='Bank_data'
)
cur=db.cursor()
print('1.LOGIN')
print('2.REGISTER')
a=int(input('Enter one of the above options:-'))
if a==1:
    n=input('enter your name:-')
    name=n.lower()
    password=input('enter your password:-')
    cur.execute('select password from customer where name=%s',(name,))
    res=cur.fetchone()
    if res:
        pas=res[0]
        if password==pas:
            flag=True
            while flag:
                print('login successfull 👍')
                print('1.Deposite')
                print('2.Withdraw')
                print('3.Balance')
                print('4.Exit')
                b=int(input('Enter one option:-'))
                if b==1:
                    amt=int(input('Enter deposite money:-'))
                    cur.execute('select balance from customer where name=%s',(name,))
                    cur_amt=cur.fetchone()
                    dep=cur_amt[0]+amt
                    cur.execute('update customer set balance=%s where name=%s',(dep,name))
                    db.commit()
                    print('money deposite successfully👍')
                elif b==2:
                    amt=int(input('Enter withdraw money:-'))
                    cur.execute('select balance from customer where name=%s',(name,))
                    cur_amt=cur.fetchone()
                    if cur_amt[0]>=amt:
                        wit=cur_amt[0]-amt
                        cur.execute('update customer set balance=%s where name=%s',(wit,name))
                        db.commit()
                        print(f'{amt}rs withdarw successfull')
                        print(f'Balance after withdraw {wit}')
                    else:
                        print('Insuffcient balance')
                elif b==3:
                    cur.execute('select balance from customer where name=%s',(name,))
                    amt=cur.fetchone()
                    print(f'Current Balance:-{amt[0]}')
                else:
                    print('Thank you visit again')
                    flag=False           
        else:
            print('Incorrect password try again')

elif a==2:
    name=input('Enter your name:-')
    name=name.lower()
    cur.execute('select *from customer where name=(%s)',(name,))
    res=cur.fetchone()
    if res:
            print('User already exist👍')
    else:
        flag=True
        while flag:
            password=input("Enter a new password:-")
            cnf=input('Confirm password:-')
            if password==cnf:
                data='insert into customer(name,password) values(%s,%s)'
                values=(name,password)
                cur.execute(data,values)
                print('Registered successfully👍')
                flag=False
            else:
                print('Password mis match')
else:
    print('Invalid choice')
db.commit()
cur.close()
db.close()

# table='create table customer (acc_id INT AUTO_INCREMENT PRIMARY KEY,name varchar(20), password varchar(20),balance decimal(10,2) default 0.00)'
# cur.execute(table)