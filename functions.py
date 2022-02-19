import math, random
from send_mail import SendMail
import mysql.connector

# Generating OTP code with digits in variable "digits"
def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

# Sending email to user email
def sendemail(sendto):
    code = generateOTP()
    new_mail = SendMail(
        # Email address of the recipient
        [sendto],
        # Email subject
        'OPT',
        # Email body
        f'Hi! Your code is {code}',
        # Email address of the sender
        'OUR EMAIL HERE' 
    )
    new_mail.send('OUR EMAIL PASSWORD HERE')
    
    # Connecting to DB
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
    )
    # Creating a cursor object using the cursor() method
    mycursor = mydb.cursor()

    # SQL Command
    sql = "INSERT INTO otp (mail, code) VALUES (%s, %s)"
    val = (f"{sendto}", f"{code}")
    # Sendind SQL request
    mycursor.execute(sql, val)
    mydb.commit()

# Code verification function
def verifycode(mail,code):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
    )
    mycursor = mydb.cursor()
    
    # SQL Command
    mycursor.execute(f"SELECT * FROM `otp` WHERE mail = \"{mail}\" ORDER BY id DESC LIMIT 0, 1;")
    myresult = mycursor.fetchall()

    # Checking DB
    if myresult[0][1] == mail and myresult[0][2] == code:
        print("Succsess")
    else:
        print("Unsuccsess")