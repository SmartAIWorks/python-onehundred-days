

import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv


load_dotenv()

# my_email = 'pinedameg@gmail.com'
# email_password = os.getenv('EMAIL_PASSWORD')

# if not email_password:
#     raise ValueError('Please provide your email app password to continue.')


# to_email = 'jrmalabanan0916@gmail.com'

# html_content = "<html><body><h1>Hello from python</h1></body></html>"
# msg = MIMEMultipart()

# msg['Subject'] = 'Hi, from Python!'
# msg['From'] = my_email
# msg['To'] = to_email

# msg.attach(MIMEText(html_content, "html"))

# with smtplib.SMTP('smtp.gmail.com', 587) as connection:
#     connection.starttls()

#     connection.login(user=my_email, password=email_password)
#     connection.send_message(msg)
    




import datetime as dt
now = dt.datetime.now()

print(f"{now.year}-{now.month}-{now.day}")

from_str_date = dt.datetime.strptime('2025-10-13', '%Y-%m-%d').date()

print(from_str_date)