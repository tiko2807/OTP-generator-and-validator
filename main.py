from functions import *

# Asking the user to enter the email to send the verification code
emailsend = input("Enter your email: ")
# Sending mail
sendemail(emailsend)

# Asking the user to enter the email for checking it in DB
email = input("Enter your email: ")
# Asking the user to enter the code for checking it in DB
code = input("Enter your code: ")

# Checking DB
verifycode(email,code)