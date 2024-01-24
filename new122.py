import hashlib
import requests
import os
import mysql.connector
import datetime

user = "Aniket"

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abcd1234",
    database="ecommerce"
)
mycursor = mydb.cursor()

description = " make a simple calculator using switch..case in Java. This calculator would be able to add, subtract, multiply and divide two numbers."

''' "CREATE TABLE TRANSACTION (Transaction_id int NOT NULL AUTO_INCREMENT,Product_id varchar(255) NOT NULL,USERNAME varchar(255), DATETIME VARCHAR(255), PRIMARY KEY(Transaction_id));"
sql2="INSERT INTO TRANSACTION(Product_id,USERNAME,DATETIME) VALUES (%s,%s,%s)"
val=("ABC","Aniket",x.strftime("%c"))
A SIMPLE CALCULATOR WHICH CAN PERFORM BASIC ARITHMETIC OPERATIONS LIKE ADDITION, SUBTRACTION, MULTIPLICATION OR DIVISION DEPENDING UPON THE USER INPUT.
mycursor.execute(sql2,val)
mydb.commit()
" make a simple calculator using switch..case in Java. This calculator would be able to add, subtract, multiply and divide two numbers."
"CREATE TABLE PRODUCT(Product_id int NOT NULL AUTO_INCREMENT,Buying_price varchar(255), Password VARCHAR(255),Product_name VARCHAR(255),Product_description VARCHAR(500),Images VARCHAR(255) PRIMARY KEY(Product_id))";
"CREATE TABLE LOGIN (USERNAME VARCHAR(255), PASSWORD VARCHAR(255),FULLNAME VARCHAR(255),EMAIL VARCHAR(255));"
"INSERT INTO LOGIN (USERNAME,PASSWORD,FULLNAME,EMAIL) VALUES (%s,%s,%s,%s)"

CREATE TABLE TRANSACTION_BLOCKCHAIN (Block_no int(4) AUTO_INCREMENT, prev_hash VARCHAR(255),Data VARCHAR(255),current_hash VARCHAR(255) ,PRIMARY KEY(block_no))

"INSERT INTO Product_details(Buying_price,Password,Product_name,Product_description) VALUES (%s,%s,%s,%s)"
val=("2 Acecoin","ABCD1234","Python Calculator",description)
insert into product(Buying_price,Password,Product_name,Product_description,Images)values(%s,%s,%s,%s,%s)"
val=("2 Acecoins","ABCD1234","Python Calculator",description,"/static/calculator.jpeg")
insert into product(Buying_price,Password,Product_name,Product_description,Images)values(%s,%s,%s,%s,%s)
sql = "SELECT MAX(Transaction_id)  FROM TRANSACTION"
mycursor.execute(sql)
details = mycursor.fetchall()
val2=(details[0][0],)
sql2="SELECT * FROM TRANSACTION WHERE Transaction_id=%s "
mycursor.execute(sql2,val2)
myresult=mycursor.fetchall()'''
'''a = 1
b = datetime.datetime.now()
c = 1
d = "ANIKET SHARMA"

prev_hash="0000"


transaction = {"Product_id": a, "Date": b, "Transaction_id": c, "Username": d, "last_block_hash": prev_hash}

transaction = str(transaction)
result = hashlib.sha256(transaction.encode()).hexdigest()


sql="SELECT * FROM TRANSACTION_BLOCKCHAIN"
mycursor.execute(sql)
myresult=mycursor.fetchall()
print(myresult)
amount=3
#sql="SELECT *  FROM TRANSACTION_BLOCKCHAIN WHERE BLock_no= (SELECT MAX(Block_no) FROM TRANSACTION_BLOCKCHAIN)"
#sql = "SELECT prev_hash FROM TRANSACTION_BLOCKCHAIN WHERE Block_no=(SELECT MAX(Block_no) FROM TRANSACTION_BLOCKCHAIN)"
sql = "Delete from transaction where product_id=%s"
val=("4",)
mycursor.execute(sql,val)
mydb.commit()
myresult=mycursor.fetchall()
print(myresult)

'''
'''
email="anikets2408@gmail.com"
psw="123"
def get_status(amount):
    request1="https://gautam666.pythonanywhere.com/transaction/start?amount="+amount+"&email="+email
    res = requests.get(request1)
    ref_no=res.text
    print(ref_no)
    print(request1)
    return ref_no


def get_status2(ref_no):
    request2="https://gautam666.pythonanywhere.com/transaction/execute?email="+email+"&passwd="+psw+"&ref_no="+ref_no
    res2=requests.get(request2)
    print(request2)
    print(res2.text)

def get_status3(ref_no):
    request3="https://gautam666.pythonanywhere.com/transaction/confirm?ref_no="+ref_no
    res3=requests.get(request3)
    print(res3.text)
    response=res3.text
    return res3.text




amount="23"
a=get_status(amount)
get_status2(a)
b=get_status3(a)

status = '{"email":"' + email + '","amount":"' + amount + '","Status":"sucess"}'

if b == status:
    print("ok")
'''

sql="CREATE TABLE LOGIN (USERNAME VARCHAR(255), PASSWORD VARCHAR(255),FULLNAME VARCHAR(255),EMAIL VARCHAR(255));"





mycursor.execute(sql)
mycursor.commit()
print("ok")
myresult=mycursor.fetchall()
print(myresult)
for x in myresult:
    print(x)

#CREATE TABLE TRANSACTION_BLOCKCHAIN (Block_no int(4) AUTO_INCREMENT, prev_hash VARCHAR(255),Data VARCHAR(255),current_hash VARCHAR(255) ,PRIMARY KEY(block_no))
#INSERT INTO TRANSACTION_BLOCKCHAIN (prev_hash,Data,current_hash)VALUES('0000','GENSISBLOCK','0001')