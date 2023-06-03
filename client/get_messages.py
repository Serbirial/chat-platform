import requests

API_URL = "http://localhost:42042/api/message/1/messages"

def get_messages():
    r = requests.get(API_URL)
    return r

msgs = get_messages()
for msg in msgs.json():
    print(f"msg ({msg['id']}): {msg['content']}")