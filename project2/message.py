"""
Program to send emails:
!ATTENTION!=Google blocks sign-in attempts from apps which do not use modern security standards (mentioned on their support page). 
You can however, turn on / off this safety feature by this link: https://www.google.com/settings/security/lesssecureapps
"""
import smtplib
# We access e-mail
print("\t\tSign in")
my_email = str(input("Insert your email:"))
my_password = str(input("Insert your password:"))
# Insertion of the receiver and message
receiver = str(input("Insert the recipient's email:"))
message = str(input("Insert the message you want to send:"))
print("I am connecting with the Server...")
# This setup works for gmail
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
# Encrypted email
server.starttls()
# Sending the message
server.login(my_email, my_password)
server.sendmail(my_email, receiver, message)
print("~Email successfully sent~")
server.close()
