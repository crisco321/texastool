import smtplib
import ssl

ctx = ssl.create_default_context()
password = "qwertyuiopasdfgh"    # Your app password goes here
sender = "somename@gmail.com"    # Your e-mail address
receiver = "recipient@gmail.com" # Recipient's address
message = """
Hello from Python.
"""

with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
