import requests

API_URL = "http://localhost:42042/api/"

def send_message(content):
    r = requests.post(url, json={
        "content": content
    })
    return r

while True:
    user_input = input("input >")
    if user_input == "/refresh":
        pass
    else:
        send_message(user_input)