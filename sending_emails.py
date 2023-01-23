import smtplib

yourEmail = input("Enter your email: ")
passw = input("Enter your password: ")

# specify the email server and login credentials
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(yourEmail, passw)

# specify the recipient and message
recipient = input("Enter recipient email: ")
subject = input("Enter the mail subject: ")
body = input("Enter the mail body: ")
message = f"Subject: {subject}\n\n{body}"

# send the email
server.sendmail(yourEmail, recipient, message)

# close the server
server.quit()
