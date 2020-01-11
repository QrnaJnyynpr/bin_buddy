import smtplib
from credentials import bin_email, password, target_email

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

smtpObj.ehlo()
(250, b'mx.google.com at your service, [216.172.148.131]\nSIZE 35882577\
n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')

smtpObj.starttls()
(220, b'2.0.0 Ready to start TLS')

smtpObj.login(bin_email, password)
(235, b'2.7.0 Accepted')

smtpObj.sendmail(bin_email, target_email, 'Subject: \nTime to take the bin out!')
{}
smtpObj.quit()
(221, b'2.0.0 closing connection ko10sm23097611pbd.52 - gsmtp')