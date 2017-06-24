#!

import smtplib

sender = 'abekuluiz@gmail.com'
receiver =['samirah.maison@gmail.com']

message ="""from:from person<lewisfilew2005@yahoo.com>
To: TO Person <samirah.maison@gmail.com>
Subject:SMTP e-mail test

This is a test email message.
"""


smtpObj = smtplib.SMTP('smtp.gmail.com', 587) 
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login("abekuluiz@gmail.com","")
message ="hey Miss Maison, how have you been"

smtpObj.sendmail("abekuluiz@gmail.com","samirah.maison@gmail.com",message)
smtpObj.quit()



print"successfully sent mail"
print "Error:unable to send email"


