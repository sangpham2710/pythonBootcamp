import smtplib
import getpass
smtp_object = smtplib.SMTP('smtp.gmail.com', 465)
smtp_object.ehlo()

# password = getpass.getpass('Password: ')
