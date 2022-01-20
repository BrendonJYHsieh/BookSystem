import tkinter as tk
import os
import tkinter.font as tkFont
from logging import setLogRecordFactory
from pprint import pprint

from httplib2 import Response
from Google import Create_Service,convert_to_RFC_datetime


def set_request():
    global event_request_body
    event_request_body['summary'] = summary_strv.get()
    event_request_body['description'] = description_strv.get()

def insert():
    global event_id
    if not event_id:
        response = service.events().insert(calendarId=calendar_id_test_room,body=event_request_body).execute()
        event_id = response['id']
        pprint(response)

def update():
    global event_id
    if event_id:
        response = service.events().update(calendarId=calendar_id_test_room,eventId=event_id,body=event_request_body).execute()
def delete():
    global event_id
    if event_id:
        response = service.events().delete(calendarId=calendar_id_test_room, eventId=event_id).execute()
        event_id = ''

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

calendar_id_test_room = 'hm70pphunkl787oic7910df7ls@group.calendar.google.com'
request_body = {
    'summary' : 'test room'
}

#response = service.calendars().insert(body=request_body).execute()
#print(response)

colors = service.colors().get().execute()
#pprint(colors)

hour_adjust = -8
event_request_body = {
  'summary': '軟體工程討論會議',
  'location': 'discord',
  #'description': '貓貓咪咪',
  'description': '大貓咪',
  'start': {
    'dateTime': convert_to_RFC_datetime(2021,10,26,20 + hour_adjust,30),
    'timeZone': 'Asia/Taipei',
  },
  'end': {
    'dateTime': convert_to_RFC_datetime(2021,10,26,21 + hour_adjust,30),
    'timeZone': 'Asia/Taipei',
  },
  'colorId':5,
  'status':'confirmed',
  'transparency':'opaque',
  'visibility':'private',
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=1'
  ],
  'attendees': [
    {'email': 'lpage@example.com'},
    {'email': 'sbrin@example.com'},
  ]
}



event_id = ''
window = tk.Tk()
tkFont.Font(family='Consolas', size=15)#要放在window = tk.Tk()之後
window.title('測試新增更新刪除events')
window.geometry('600x200')

summary_label = tk.Label(window,text = "Summary")
description_label = tk.Label(window,text = "description")

summary_strv = tk.StringVar()
summary_strv.set(event_request_body['summary'])
summary_entry = tk.Entry(window, textvariable=summary_strv)

description_strv = tk.StringVar()
description_strv.set(event_request_body['description'])
description_entry = tk.Entry(window, textvariable=description_strv)

insert_btn = tk.Button(window,text='新增',command=insert)
update_btn = tk.Button(window,text='更新',command=update)
delete_btn = tk.Button(window,text='刪除',command=delete)

set_btn = tk.Button(window,text='輸入完成',command=set_request)

insert_btn.place(x=0,y=0,width=200,height=40)
update_btn.place(x=200,y=0,width=200,height=40)
delete_btn.place(x=400,y=0,width=200,height=40)
set_btn.place(x=0,y=150,width=600,height=40)

summary_label.place(x=0,y=50)
summary_entry.place (x=200,y = 50,width=400,height=30)

description_label.place(x=0,y= 100)
description_entry.place (x=200,y = 100,width=400,height=30) 

window.mainloop()