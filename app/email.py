# Email File

# MY MAILGUN EMAIL ADDRESS IS SET TO PAY-PER EMAIL, SO UNFORTUNATELY I WILL NOT RUN THIS FILE.

import os
from dotenv import load_dotenv

load_dotenv() # Searches the ".env" file for environment variables.

MAILGUN_SENDER_ADDRESS = os.getenv("MAILGUN_SENDER_ADDRESS", default="demo")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN", default="demo")
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY", default="demo")


import requests

def send_mail_with_mailgun(recipient_address=MAILGUN_SENDER_ADDRESS,
                           subject="[Shopping Cart App] Testing 123",
                           html_content="<p>Hello World</p>"
                           ):
    print("SENDING EMAIL TO:", recipient_address)
    print("SUBJECT:", subject)
    print("HTML:", html_content)

    try:
        request_url = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"
        message_data = {
            'from': MAILGUN_SENDER_ADDRESS,
            'to': recipient_address,
            'subject': subject,
            'html': html_content,
        }
        #print(message_data)
        response = requests.post(request_url,
            auth=('api', MAILGUN_API_KEY),
            data=message_data
        )
        print("RESULT:", response.status_code)
        response.raise_for_status()
        print("Email sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending email: {str(e)}")

send_mail_with_mailgun()

price = 4.99
send_mail_with_mailgun(html_content=f"The total is ${price}")

my_content = """

    <img
        src="https://img.freepik.com/free-vector/flat-ice-cream-collection_23-2148982427.jpg"
        alt="image of an ice cream"
        height=100
    >

    <h1>Ice Cream Shop Menu</h1>

    <p>Most popular flavors:</p>

    <ul>
        <li>Vanilla Bean </li>
        <li>Choc </li>
        <li>Strawberry</li>
    </ul>
"""
send_mail_with_mailgun(html_content=my_content)