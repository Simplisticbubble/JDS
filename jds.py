import requests
import schedule
import time
import smtplib, ssl

class Person:
    def __init__(self, name, email, dashBoard):
        self.name = name
        self.email = email
        self.dashBoard = dashBoard

    def printDetail(abc):
        print("User: " + abc.name)
        print("Email: " + abc.email)
        print("DashBoard: " + abc.dashBoard)
    def getEmail(abc):
        return abc.email

    def hasdash(abc,dboard):
        if dboard == abc.dashBoard:
            return True

"List of Recipients"
ListRec = []
ListRec.append(Person("John", "ks.kevinseu@gmail.com", "MzYyMzc0MHxWSVp8REFTSEJPQVJEfDU3MzgyMDk"))
ListRec.append(Person("Kevin", "electrobubz@gmail.com", "MzYyMzc0MHxWSVp8REFTSEJPQVJEfDU3MzgyMDk"))
ListRec.append(Person("Jimmy", "Jimmy.test@gmail.com", "MzYyMzc0MHxWSVp8REFTSEJPQVJEfDU3ODQ0NzM"))

def ListAppend(name, email,dashBoard):
    ListRec.append(Person(name, email, dashBoard))

def printList():
    for i in ListRec:
        i.printDetail()
    

def postReq(abc):

    url = 'https://api.newrelic.com/graphql'
    myobj = {"query":"mutation {\n dashboardCreateSnapshotUrl(guid:\"%s\")\n}\n" % (abc), "variables":"" } 

    x = requests.post(url, json = myobj, headers={'Content-Type': 'application/json',
    'API-Key': 'NRAK-QQIVQP8HQO25QRH1EQ8M0XX57VL',}

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
def sendMail(abc):

    for i in ListRec:
        if i.hasdash(abc):
            receiver_email = i.getEmail()
            print(slicer(postReq(abc)))
            SUBJECT = "TEST"
            TEXT = slicer(postReq(abc))
            message = """\
            Subject: %s

            %s
            """ % ( SUBJECT, TEXT)
            
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login("python.test.123454321@gmail.com", password)
                server.sendmail(sender_email, receiver_email, message)


#schedule.every().day.at("10:30").do(sendMail("MzM5MzExMHxWSVp8REFTSEJPQVJEfDU2MTkwMjU"))
sendMail("MzYyMzc0MHxWSVp8REFTSEJPQVJEfDU3MzgyMDk")

