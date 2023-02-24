import requests
from plyer import notification
from bs4 import BeautifulSoup
import time

def notifyMe(title, message): 
    notification.notify(
        title= title,
        message = message,
        app_icon = "favicon.ico",
        timeout = 20
    )

def webData(url): 
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
        html_doc = webData('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(html_doc, 'html.parser') 
        mystr = ""

        for tr in soup.find_all ('tbody')[1].find_all('tr'):
            mystr += tr.get_text() 
        myList = (mystr.split("\n\n")) 


        states = ['Delhi','West Bengal', 'Maharashtra','Patna',] 
            dataList = (item.split('\n'))
            if dataList[1] in states:
                notify_title= 'Cases of Covid-19 In India'
                notify_text= f" State: {dataList[1]}\n Indian Cases : {dataList[2]} & Foreign Cases : {dataList[3]}\n Cured : {dataList[4]}\n Deaths : {dataList[5]}"
                notifyMe(notify_title, notify_text)
                time.sleep(2)
        time.sleep(3600) 



        