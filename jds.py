import requests
import schedule
import time
import smtplib, ssl
from datetime import datetime

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
    def getName(abc):
        return abc.name

    def hasdash(abc,dboard):
        if dboard == abc.dashBoard:
            return True
    def hasName(abc,uName):
        if uName == abc.name:
            return True
    def getGUID(abc):
        return abc.dashBoard

"List of Recipients"
ListRec = []
ListRec.append(Person("John", "ks.kevinseu@gmail.com", "MzYyMzc0MHxWSVp8REFTSEJPQVJEfDU3MzgyMDk"))
ListRec.append(Person("Kevin", "electrobubz@gmail.com", "MzYyMzc0MHxWSVp8REFTSEJPQVJEfDU3MzgyMDk"))
ListRec.append(Person("Jimmy", "Jimmy.test@gmail.com", "MzYyMzc0MHxWSVp8REFTSEJPQVJEfDU3ODQ0NzM"))
#ListRec.append(Person("Lance", "leeshihhom@hotmail.com", "MzYyMzc0MHxWSVp8REFTSEJPQVJEfDU3MzgyMDk"))
#ListRec.append(Person("Shu","shufoldof@gmail.com", "MzYyMzc0MHxWSVp8REFTSEJPQVJEfDU3MzgyMDk"))

def ListAppend(name, email,dashBoard):
    ListRec.append(Person(name, email, dashBoard))

def printList():
    print("--------------------------------------Recipients--------------------------------------------")
    for i in ListRec:
        i.printDetail()
    print("----------------------------------------------------------------------------------")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
class ErrorLog:
    def __init__(self, time, dashBoard):
        self.time = time
        self.dashBoard = dashBoard
    
    def printLogDetail(abc):
        print("time: " + abc.time)
        print("DashBoard guid: " + abc.dashBoard)

ListErrorLog = []
ListErrorLog.append(ErrorLog(current_time, "MzYyMzc0MHxWSVp8REFTSEJPQVJEfDU3MzgyMDk"))

def printLog():
    print("-------------------------------------ERROR-LOG---------------------------------------------")
    for i in ListErrorLog:
        i.printLogDetail()
    print("----------------------------------------------------------------------------------")

class AuditLog():
    def __init__(self,name, email,time, dashBoard):
        self.name = name
        self.email = email
        self.time = time
        self.dashBoard = dashBoard
    def printAuditDetail(abc):
        print("Name: "+ abc.name + "    Email: "+ abc.email)
        print("time: " + abc.time + "   DashBoard guid: " + abc.dashBoard)
ListAuditLog = []
ListAuditLog.append(AuditLog("Kevin", "electrobubz@gmail.com", current_time, "MzYyMzc0MHxWSVp8REFTSEJPQVJEfDU3MzgyMDk"))

def printAuditLog():
    print("----------------------------------------Audit-Log------------------------------------------")
    for i in ListAuditLog:
        i.printAuditDetail()
    print("----------------------------------------------------------------------------------")

def postReq(abc):

    url = 'https://api.newrelic.com/graphql'
    myobj = {"query":"mutation {\n dashboardCreateSnapshotUrl(guid:\"%s\")\n}\n" % (abc), "variables":"" } 

    x = requests.post(url, json = myobj, headers={'Content-Type': 'application/json',
    'API-Key': 'NRAK-QQIVQP8HQO25QRH1EQ8M0XX57VL',}

    )

    #print the response text (the content of the requested file):
    print(x.text)
    if "error" in x.text:
        ListErrorLog.append(ErrorLog(current_time, abc))

    return(x.text);



def slicer(pdfFile):
    if "error" in pdfFile:
        return("error!-no dashboard found")
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
    TEXT = slicer(postReq(abc))
    
    for i in ListRec:
        if i.hasdash(abc):
            receiver_email = i.getEmail()
            
            SUBJECT = "TEST"
            
            message = """\
            Subject: %s

            %s
            """ % ( SUBJECT, TEXT)
            
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login("python.test.123454321@gmail.com", password)
                server.sendmail(sender_email, receiver_email, message)
            ListAuditLog.append(AuditLog(i.getName(), receiver_email, current_time, abc))

def sendUser(abc):
    for i in ListRec:
        if i.hasName(abc):
            receiver_email = i.getEmail()
            TEXT = slicer(postReq(i.getGUID()))
            SUBJECT = "TEST"
            message = """\
            Subject: %s

            %s
            """ % ( SUBJECT, TEXT)

            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login("python.test.123454321@gmail.com", password)
                server.sendmail(sender_email, receiver_email, message)
            ListAuditLog.append(AuditLog(i.getName(), receiver_email, current_time, abc))

sendUser("Kevin")


#schedule.every().day.at("10:30").do(sendMail("MzYyMzc0MHxWSVp8REFTSEJPQVJEfDU3MzgyMDk"))
#schedule.every().day.at("11:30").do(sendMail("MzYyMzc0MHxWSVp8REFTSEJPQVJEfDU3ODQ0NzM")
#sendMail("MzYyMzc0MHxWSVp8REFTSEJPQVJEfDU3MzgyMDk")

#printLog()
#printAuditLog()
#printList()