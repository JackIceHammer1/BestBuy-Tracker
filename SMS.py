import smtplib
def send(message):
    email = 'EMAIL' # Replace with your email
    password = 'PASSWORD' # Replace with your password
    phone_number = '0000000000'  # Replace with your phone number
    carrier_domain = '@mms.att.net'  # Replace with your carrier's domain

    to_email = phone_number + carrier_domain
    server = smtplib.SMTP('smtp.live.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, to_email, message)
    server.quit()
