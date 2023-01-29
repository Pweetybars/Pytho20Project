import requests
import schedule
import time

def send_message():
    resp= requests.post('https://textbelt.com/text', {
        'phone' : '+855974447772',
        'message': 'Hey, Good Morning. /n I love You <3 \n Stay Safe \n from VADH - Your Boyfriend',
        'key': 'textbelt'
    })
    print(resp.json())

schedule.every().day.at('06:30').do(send_message)
