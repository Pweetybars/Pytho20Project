from email.message import EmailMessage
import ssl 
import smtplib

email_sender = 'pweetybars@gmail.com'
email_password = 'xbsokbhtpmwgrxue'

email_receivers = [ 'sunsereyrothnak@gmail.com' ] 

#first we get the password from our account and we import EmailMessage from email.message 
#then we create variable Email Sender, password, email receiver. 

subject = 'Hello'
body = """ I study with you. """

em = EmailMessage()

em['From'] = email_sender
em['To'] = email_receivers
em['subject'] = subject 
em.set_content(body)
#then we use function from EmailMessage 
#which it was taking those specification to fill in those email form. 

context = ssl.create_default_context()
#then we import ssl and smtp library to login and send the gmail. 
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smpt: 
    smpt.login(email_sender, email_password)
    smpt.sendmail(email_sender, email_receivers, em.as_string())


