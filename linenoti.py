import requests
import time
import pyautogui
import threading
from datetime import datetime
#pip3 install opencv-python
url = 'https://notify-api.line.me/api/notify'
token = 'line_token'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

pyautogui.FAILSAFE= True
now = datetime.now()
current_time = now.strftime("%H%M%S")
print("Current Time =", current_time)

def disconnect():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H%M%S")
        btn_disconnect = pyautogui.locateOnScreen('images/btn-click1.jpg', confidence=0.9)
        if btn_disconnect is not None:
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'saveimages\disconnect'+str(current_time)+'.jpg')
            img = {'imageFile': open('saveimages/disconnect'+str(current_time)+'.jpg','rb')}
            data = {'message':'เกมหลุด'}
            headers = {'Authorization':'Bearer ' + token}
            session = requests.Session()
            session_post = session.post(url, headers=headers, files=img, data =data)
            print(session_post.text) 
            time.sleep(30)

thrdisconnect = threading.Thread(target=disconnect)
thrdisconnect.start()

