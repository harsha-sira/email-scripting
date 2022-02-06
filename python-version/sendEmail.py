from email.message import EmailMessage
import smtplib
import json
import time


with open('input.json') as f:
    d = json.load(f)

gmail_user = d['email_address']
gmail_password = d['app_password']
sucess_count = 0 
fail_count = 0 

try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()   # optional
    server_ssl.login(gmail_user, gmail_password)
    # ...send emails

    addresses = d['addresses']
    subject = d['subject']

    for to in addresses:
        try:
            email = EmailMessage()
            email['Subject'] = subject
            email['From'] = gmail_user
            email['To'] = to
            email.set_content(d['content'], subtype='html')

            # server_ssl.sendmail(sent_from, to, email_text)
            server_ssl.send_message(email)
            sucess_count += 1
            time.sleep(4)
            print("Message sent to-", to)
        except:
            print("Failed to send email to- ", to)
            fail_count += 1
        
    server_ssl.close()
    print("\n\n\nSucess count=%s \nFailed count=%s" % (sucess_count, fail_count))
except:
    print('Something went wrong...')

