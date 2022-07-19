#! python3.10.4
# Start
# Case study of chapter 7 OOP
# Modules
import smtplib
from email.mime.text import MIMEText


# Save in a dict and sends it with smtpd
def send_email(subject:str, message:str, from_addr, *to_addrs,
    host='localhost', port=1025, headers=None):
    """ yea yea yea saves the messages in dict
    and send them with this local host with base protocol"""
    headers = {} if headers is None else headers
    email = MIMEText(message)
    email['Subject'] = subject
    email['From'] = from_addr
    for header, value in headers.items():
        email[header] = value
    
    sender = smtplib.SMTP(host, port)
    for addr in to_addrs:
        del email['to']
        email['To'] = to_addrs
        sender.sendmail(from_addr, addr, email.as_string())
    sender.quit()

# End