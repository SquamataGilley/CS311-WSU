import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def Email_Function():
# A simple user input function to get user credentials, we have this hard coded at work but this is more user friendly
            # Be Advised #
    # This Gmail API does require Outside applications to use your gmail account, this isnt a worry for me though
    # since im always using the same email to automate these, hence this won't work without allowing 3rd party
    # applications to have access to your account
    # THIS WILL CRASH IF YOUR ACCOUNT DOESNT ALLOW LESS SECURE APPS, thank you
    sender = input("What is your gmail address? ")
    password = input("What is your gmail password? ")
        
# Here we set up our MIME for the message and its contents
    message = MIMEMultipart()
    # Defines the header from which the email is sent from
    message['From'] = sender
    # Another simple user input call to find who the email is going to
    print("To test this next part, I'd enter your own email address\nto be sure it is sending")
    receiver = input("Who is getting this email? ")
    # Directly assigned from the previous question asked
    message['To'] = receiver
    # More questions to fill in these blanks
    subject = input("What will go in the subject line? ")
    message['Subject'] = subject
    # One last question to fill in the body
    bodyTXT = input("What will go in the body of the message? ")
    body = bodyTXT
    # This simple line just puts all of the afformentioned variables into the right spot and compiles the message
    message.attach(MIMEText(body, 'plain'))

# Down here we have the capability to send files too, at work we are sending automated PDFs named sequentially
    # so the program can find and send the right ones
    # I opted out of making this functioning as the user would have to hard code all this in but its not too
    # difficult if one wants to try

    fileName = r'D:\HDD - Desktop\PC.txt'
# open the file in binary
    binary_pdf = open(fileName, 'rb')
    payload = MIMEBase('application', 'octate-stream', Name = fileName)
# Attachment will be named AIA_Form with the date attached
    Attachment_Name = input("What is the name you would like to assign this file? ")
    payload = MIMEBase('application', 'pdf', Name = Attachment_Name)
    payload.set_payload((binary_pdf).read())
 
# enconding the binary into base64
    encoders.encode_base64(payload)
 
# add header with pdf name
    payload.add_header('Content-Decomposition', 'attachment', filename = Attachment_Name)
    message.attach(payload)
# Sets up Googles SMTP port and sets up SSL security
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
# logs in with the provided credentials and sends the email to the recipient
    session.login(sender, password)
    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()

# Last but not least, this calls the Email_Function that was defined above
Email_Function()
