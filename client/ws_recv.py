import websocket
from json import loads, dumps

ws = websocket.WebSocket()

headers = {
    "author: 12779011747794092616", # Test user (dummyacc2)
    "betatoken: 56748467863985672345467",
    "Authorization: DMpIrhNeKl7pWCjr7HKS-hezSatfZwpFNqAlGwGC4DE" # Test user authkey (password to generate auth key: dummypw)

}

ws.connect("ws://localhost:42042/api/events/ws", header=headers)

def recv(ws):
    return ws.recv()


def format(raw_event_data, delim: str = "\n"): # This code is wacky...
    split = raw_event_data.split(delim) # Split the data by '\n', seperating the event and the data.
    json =  split[1].split(":", 1)[1] # Seperate the data tag from the actual json needed.
    return split[0].split, json


data = recv(ws)
if data == "recognized":
    print("recognized")
else:
    print(data)
    ws.close()

while 1:
    print(recv(ws))
