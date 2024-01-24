import datetime
import hashlib
import smtplib
import requests
from flask import send_file
from flask import Flask, render_template, request, make_response
import mysql.connector
from werkzeug.utils import redirect

newcommers = Flask(__name__)


@newcommers.route("/")
def newuser():
    return render_template("loginpage.html")


@newcommers.route('/form_newuser_button', methods=['POST', 'GET'])
def newuser_button():
    return render_template("newaccount.html")


@newcommers.route('/form_new_user', methods=['POST', 'GET'])
def generatenewaccount():
    mydb = mysql.connector.connect(
        host="Anikets240802.mysql.pythonanywhere-services.com",
        user="Anikets240802",
        password="abcd1234@",
        database="Anikets240802$Ecommerce"
    )
    mycursor = mydb.cursor()
    user = request.form['uname']
    username = request.form['uname']
    password = request.form['newpsw1']
    confirmpassword = request.form['newpsw2']
    uname = request.form['uname']
    fname = request.form['fname']
    mail = request.form['mailid']
    uname = uname.lower()
    username = username.lower()
    sql = "SELECT * FROM LOGIN WHERE USERNAME= " + "'" + uname + "'"
    mycursor.execute(sql)
    myresult = mycursor.fetchone()

    if username != myresult:
        if password == confirmpassword:
            sql = "INSERT INTO LOGIN (USERNAME,PASSWORD,FULLNAME,EMAIL) VALUES (%s,%s,%s,%s)"
            val = (username, password, fname, mail)
            mycursor.execute(sql, val)
            mydb.commit()

            return render_template("loginpage.html", info="Login again")
        else:
            return render_template("loginpage.html")

    else:
        return render_template("newaccount.html", info="Choice a different Username")


@newcommers.route('/set', methods=['POST', 'GET'])
def cokkie():
    user = request.args.get('uname')
    resp = make_response()
    resp.set_cookie('uname', user)
    return resp


@newcommers.route('/set1', methods=['POST', 'GET'])
def cokkie1():
    a = request.cookies.get('uname')
    return a


@newcommers.route('/form_login', methods=['POST', 'GET'])
def login():
    mydb = mysql.connector.connect(
        host="Anikets240802.mysql.pythonanywhere-services.com",
        user="Anikets240802",
        password="abcd1234@",
        database="Anikets240802$Ecommerce"
    )
    mycursor = mydb.cursor()

    try:
        sql = "SELECT * FROM LOGIN WHERE USERNAME= %s "

        user = request.form['uname']
        password = request.form['psw']
        name1 = (request.form['uname'].lower(),)
        mycursor.execute(sql, name1)
        myresult = mycursor.fetchone()

    except:
        return render_template("loginpage.html", info='try again')

    if password == myresult[1]:
        resp = make_response(render_template("homepage.html", User=user))
        resp.set_cookie('uname', user)
        return resp
    else:
        return render_template("loginpage.html", info='Try again, Incorrect Password or Username ')


@newcommers.route('/to_homepage', methods=['POST', 'GET'])
def return_to_homepage():
    user = request.cookies.get('uname')
    user = str(user)
    return render_template("homepage.html", User=user)


@newcommers.route('/form_logout', methods=['POST', 'GET'])
def log_out():
    return render_template("loginpage.html", info="Would you like to login again?")


@newcommers.route('/form_transactionhistory', methods=['POST', 'GET'])
def transactionpage():
    mydb = mysql.connector.connect(
        host="Anikets240802.mysql.pythonanywhere-services.com",
        user="Anikets240802",
        password="abcd1234@",
        database="Anikets240802$Ecommerce"
    )

    mycursor = mydb.cursor()
    mycursor1 = mydb.cursor()
    try:
        a = request.cookies.get('uname')
        a = str(a)
        val = (a,)
        sql = "SELECT * FROM TRANSACTION WHERE USERNAME= %s"
        sql2 = "SELECT * FROM LOGIN WHERE USERNAME= %s"
        mycursor1.execute(sql, val)
        myresult = mycursor1.fetchall()
        mycursor.execute(sql2, val)
        details = mycursor.fetchone()

        return render_template("dashboard.html", Transactionhistory=myresult, fullname="Name:" + " " + details[2],
                               email="Email:" + " " + details[3], username="Username:" + " " + details[0], User=a)

    except:
        return render_template("dashboard.html", No_transactions="No Transactions yet")


@newcommers.route('/get_status/<id>', methods=['POST', 'GET'])
def send_refno(id):
    mydb = mysql.connector.connect(
        host="Anikets240802.mysql.pythonanywhere-services.com",
        user="Anikets240802",
        password="abcd1234@",
        database="Anikets240802$Ecommerce"
    )
    try:
        user = request.cookies.get('uname')
        user = str(user)

        mycursor = mydb.cursor()
        email = request.form['aceuname']
        email = str(email)
        passwordace = request.form['psw']
        passwordace = str(passwordace)
        print("hello1")
        sql = "SELECT BUYING_PRICE FROM PRODUCT WHERE Product_id=%s"
        val = (id,)
        mycursor.execute(sql, val)
        print("hello2")
        myresult = mycursor.fetchall()
        amount = myresult[0][0]
        print("hello3")
        amount = str(amount)

        a = get_status(amount, email)
        get_status2(a, email, passwordace)
        b = get_status3(a)


        status = '{"email":"'+email+'","amount":"'+amount+'","Status":"sucess"}'
        print(b)
        if b == status:
            BuyNow(id)
            return render_template("thanku.html", id=id, User=user)
        else:
            return render_template('failed.html')
    except:
        return render_template('failed.html')



def get_status(amount, email):
    request1 = "https://gautam666.pythonanywhere.com/transaction/start?amount=" + amount + "&email=" + email
    res = requests.get(request1)
    ref_no = res.text
    print(ref_no)
    print(request1)
    return ref_no


def get_status2(ref_no, email, psw):
    request2 = "https://gautam666.pythonanywhere.com/transaction/execute?email=" + email + "&passwd=" + psw + "&ref_no=" + ref_no
    res2 = requests.get(request2)
    print(request2)
    print(res2.text)


def get_status3(ref_no):
    request3 = "https://gautam666.pythonanywhere.com/transaction/confirm?ref_no=" + ref_no
    res3 = requests.get(request3)
    print(res3.text)
    response = res3.text
    return res3.text


@newcommers.route('/server_login/<id>', methods=['POST', 'GET'])
def trans_login(id):
    return render_template("acecoins.html", id=id)


def BuyNow(id):
    mydb = mysql.connector.connect(
        host="Anikets240802.mysql.pythonanywhere-services.com",
        user="Anikets240802",
        password="abcd1234@",
        database="Anikets240802$Ecommerce"
    )
    user = request.cookies.get('uname')
    user = str(user)
    mycursor = mydb.cursor()
    product_id = id
    val = (product_id,)
    sql = "SELECT Product_name, Password FROM PRODUCT WHERE Product_id= %s"
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    x = datetime.datetime.now()
    sql2 = "INSERT INTO TRANSACTION(Product_id,USERNAME,DATETIME) VALUES (%s,%s,%s)"
    val2 = (product_id, user, x.strftime("%c"))
    mycursor.execute(sql2, val2)
    mydb.commit()
    blockchain_generation()
    sql4 = "SELECT * FROM TRANSACTION_BLOCKCHAIN WHERE Block_no=(SELECT MAX(Block_no) FROM TRANSACTION_BLOCKCHAIN)"
    mycursor.execute(sql4)
    details = mycursor.fetchall()
    send_password(product_id)


@newcommers.route('/download_link/<id>', methods=['POST', 'GET'])
def to_the_authentication_page(id):
    return render_template("authentiction.html", id=id)


@newcommers.route('/download/<id>', methods=['POST', 'GET'])
def download_file(id):
    mydb = mysql.connector.connect(
        host="Anikets240802.mysql.pythonanywhere-services.com",
        user="Anikets240802",
        password="abcd1234@",
        database="Anikets240802$Ecommerce"
    )
    mycursor = mydb.cursor()

    sql = "Select Product_name from Product where Product_id =%s"
    val = (id,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    Product_name = myresult[0][0]
    path = "/Users/aniketsharma/Desktop/pythonProject/" + Product_name + " File.docx"

    return send_file(path, as_attachment=True)


@newcommers.route('/authentication_check/<id>', methods=['POST', 'GET'])
def authentication_check(id):
    mydb = mysql.connector.connect(
        host="Anikets240802.mysql.pythonanywhere-services.com",
        user="Anikets240802",
        password="abcd1234@",
        database="Anikets240802$Ecommerce"
    )
    mycursor = mydb.cursor()

    try:
        sql = "SELECT PASSWORD FROM PRODUCT WHERE Product_id=%s "

        pro_id = request.form['product_id']
        password = request.form['Product_psw']
        val1 = (pro_id,)
        mycursor.execute(sql, val1)
        myresult = mycursor.fetchone()

    except:
        return render_template("authentiction.html", info='try again', id=id)

    if password == myresult[0]:
        return render_template("download.html", id=id)
    else:
        return render_template("authentiction.html", info='Incorrect Password or Product Id', id=id)




@newcommers.route('/search', methods=['POST', 'GET'])
def search():
    mydb = mysql.connector.connect(
        host="Anikets240802.mysql.pythonanywhere-services.com",
        user="Anikets240802",
        password="abcd1234@",
        database="Anikets240802$Ecommerce"
    )
    try:
        mycursor = mydb.cursor()
        user = request.cookies.get('uname')
        user = str(user)
        psw2 = request.form['uname']
        sql = "Select * from product where Product_name=%s"
        val = (psw2,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        cost = str(myresult[0][1])
        return render_template("product.html", Description=myresult[0][4], Product_Name=myresult[0][3], Buying_price=cost,
                           id=myresult[0][0], images=myresult[0][5], User=user)
    except:
        return render_template("product_failed.html")


@newcommers.route('/cart/<id>', methods=['POST', 'GET'])
def product(id):
    mydb = mysql.connector.connect(
        host="Anikets240802.mysql.pythonanywhere-services.com",
        user="Anikets240802",
        password="abcd1234@",
        database="Anikets240802$Ecommerce"
    )
    user = request.cookies.get('uname')
    user = str(user)
    mycursor = mydb.cursor()
    product_id = id
    val = (product_id,)
    sql = "SELECT * FROM PRODUCT WHERE Product_id= %s"
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    cost = str(myresult[1])
    return render_template("product.html", Description=myresult[4], Product_Name=myresult[3], Buying_price=cost,
                           id=product_id, images=myresult[5], User=user)


def blockchain_generation():
    mydb = mysql.connector.connect(
        host="Anikets240802.mysql.pythonanywhere-services.com",
        user="Anikets240802",
        password="abcd1234@",
        database="Anikets240802$Ecommerce"
    )
    mycursor = mydb.cursor()
    sql = "SELECT * FROM TRANSACTION WHERE Transaction_id= (SELECT MAX(Transaction_id) FROM TRANSACTION)"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    a = myresult[0][1]
    b = myresult[0][3]
    c = myresult[0][0]
    d = myresult[0][2]
    prev_hash = "0000"

    sql2 = "SELECT current_hash FROM TRANSACTION_BLOCKCHAIN WHERE Block_no=(SELECT MAX(Block_no) FROM TRANSACTION_BLOCKCHAIN)"
    mycursor.execute(sql2)
    myresult2 = mycursor.fetchall()
    prev_hash = myresult2[0][0]
    transaction = {"Product_id": a, "Date": b, "Transaction_id": c, "Username": d, "last_block_hash": prev_hash}

    transaction = str(transaction)
    current_hash = hashlib.sha256(transaction.encode()).hexdigest()

    sql3 = "INSERT INTO TRANSACTION_BLOCKCHAIN(prev_hash,Data,Current_hash) VALUES(%s,%s,%s)"
    val3 = (prev_hash, transaction, current_hash)
    mycursor.execute(sql3, val3)
    mydb.commit()


def send_password(product_id):
    mydb = mysql.connector.connect(
        host="Anikets240802.mysql.pythonanywhere-services.com",
        user="Anikets240802",
        password="abcd1234@",
        database="Anikets240802$Ecommerce"
    )
    mycursor = mydb.cursor()
    sql = "SELECT PASSWORD FROM PRODUCT WHERE Product_id= %s"
    val = (product_id,)
    mycursor.execute(sql, val)
    myresult3 = mycursor.fetchall()
    user = request.cookies.get('uname')
    user = str(user)
    sql2 = "SELECT EMAIL FROM LOGIN WHERE USERNAME = %s"
    val2 = (user,)
    mycursor.execute(sql2, val2)
    details = mycursor.fetchall()
    reciver_email = details[0][0]

    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()
    password = str(myresult3[0])

    # Authentication
    s.login("anikets2048@gmail.com", "9920376331")

    # message to be sent
    message1 = "Thanks" + user + ", for buying from Mr.commerce you can use the password is" + password + " and product _id is  " + str(
        product_id)
    message = str(message1)

    # sending the mail
    s.sendmail("anikets2048@gmail.com", reciver_email, message)

    # terminating the session
    s.quit()


if __name__ == "__main__":
    newcommers.run(debug=True)
