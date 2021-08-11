

from lxml import html
import requests 
from time import sleep
import time
import schedule
import smtplib

# Mail_id of the user to be notified with the availability status of the product
receiver_email_id = "EMAIL_ID_OF_USER"

def check(url):
    headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, loke Gecko) Chrome/42.0.2311 90 Safari/537.36'}

    # ading headers to show that we are a browser who is sending GET request 
    page = requests.get(url, headers = headers)
    for i in range(20):
        # because continous checks in milliseconds or few seconds will block your request
        sleep(3)

        # parsing the html context
        doc = html.fromstring(page.content)

        # checking availability of the products 
        XPATH_AVAILABILITY = "//div[@id ="availability"]//text()"
        RAW_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)
        AVAILABILITY = "".join(RAW_AVAILABILITY).strip() if RAW_AVAILABILITY else None
        return AVAILABILITY

def sendemail(ans, product):
    GMAIL_USERNAME = "YOUR_GMAIL_ID"
    GMAIL_PASSWORD = "YOUR_GMAIL_PASSWORD"

    recipient = receiver_email_id
    body_of_email = ans
    email_subject = product + "product availability"

    # creates SMTP session
    s = smtplib.SMTP("smtp.gmail.com", 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(GMAIL_USERNAME, GMAIL_PASSWORD)

    # message to be sent
    headers = "\r\n".join(["from: " + GMAIL_USERNAME,
                        "subject: " + email_subject,
                        "to: " + recipient,
                        "mine-version: 1.0",
                        "content-type: text/html"])
    content = headers + "\r\n\r\n" + body_of_email
    s.sendmail(GMAIL_USERNAME, recipient, content)
    s.quit()

def ReadAsin():
    # Asin Id is the product Id which needa to be provided by the user
    Asin = "B077PWK5BT"
    url = "http://www.amazon.in/dp/" + Asin
    print("Processing: " + url)
    ans = check(url)
    arr = [
        'Only 1 left in stock .... Super Hurry kid',
        'Only 2 left in stock .... Hurry Kid',
        'In stock ... Buy it quickly kid'
    ]
    print(ans)
    if ans in arr:
        # sending email to user if in case product available
        sendemail(ans, Asin)

# scheduling same code to run multiple 
# times after every 1 minute
def job():
    print("Tracking......")
    ReadAsin()

schedule.every(1).minutes.do(job)

while True:
    # running all pending tasks/jobs
    schedule.run_pending()
    time.sleep(1)
    