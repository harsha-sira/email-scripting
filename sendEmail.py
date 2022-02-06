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
            email.set_content('<div>Dear sir,<div><br></div><div>I am one of the thousand Engineers who obtained 476 visa in order to work in Australia which will fulfill&nbsp;Australia\'s&nbsp;skill shortage. But unfortunately, the&nbsp;Australian border was closed due to Covid19 and it was open almost 2 years later. Thousands of 476 Visa holder\'s visas got expired due to this.&nbsp;&nbsp;</div><div><br></div><div>Recently Prime Minister has informed that Government is allowing extending 485 expired visas but has not mentioned anything regarding the 476 Visas. I had&nbsp;spent lot of time, money, and effort on granting this visa, yet expired it with no fault&nbsp;of me.&nbsp;</div><div><br></div><div>I kindly request from you raise&nbsp;your&nbsp;voice on behalf of thousands of expired 476 visa holders like me. Please help thousands of engineers to restore their expired visas. This action will help to drastically reduce the skill shortage in Australia.<br></div><div><br></div><div>Thanks,</div><div><br></div><div>Name: Harsha Sandamal Siriwardana</div><div>Mobile Number: 94716315445</div><div>Residential&nbsp;Address: Gamachchige watta, Malimbada,Palatuwa,Matara,Sri Lanka.<wbr>81050</div></div>,', subtype='html')

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

