import requests
import schedule
import time
import smtplib, ssl


def postReq():

    url = 'https://api.newrelic.com/graphql'
    myobj = {"query":"mutation {\n dashboardCreateSnapshotUrl(guid:\"MzM5MzExMHxWSVp8REFTSEJPQVJEfDU2MTkwMjU\")\n}\n", "variables":""}

    x = requests.post(url, json = myobj, headers={'Content-Type': 'application/json',
    'API-Key': 'NRAK-O5HEY4B7NGN57IFWYFABWK22ZCJ',}

    )

    #print the response text (the content of the requested file):

    
    
    return(x.text);



def slicer(pdfFile):

    
    return(pdfFile[39:121])


smtp_server = "smtp.gmail.com"
sender_email = "python.test.123454321@gmail.com"
receiver_email = "python.test.123454321@gmail.com"



# Send email here
port = 465  # For SSL
password = "fxfynlpbuyubncgv"

# Create a secure SSL context
context = ssl.create_default_context()
def sendMail():
    print(slicer(postReq()))
    SUBJECT = "TEST"
    TEXT = slicer(postReq())
    message = """\
    Subject: %s

    %s
    """ % ( SUBJECT, TEXT)
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("python.test.123454321@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)



sendMail()
