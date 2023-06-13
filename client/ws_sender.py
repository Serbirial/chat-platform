import websocket
import time

ws = websocket.WebSocket()

headers = {
    "author: 8702477546426596933", # Test user (dummyacc1)
    "betatoken: BETA_TOKEN_HERE",
    "Authorization: j1mbsV492HZ2kZcTh26frabdPt5vKII42763fDPAaP0" # Test user authkey (password to generate auth key: dummypw)

}


test_data = 'event: new_message\ndata: {"content": "REPLACE", "destination": "guild:1"}'

ws.connect("ws://localhost:42042/api/events/ws", header=headers)

def recv(ws):
    return ws.recv()

data = recv(ws)
if data == "recognized":
    print("recognized")
else:
    print(data)
    ws.close()

while 1:
    uip = input("msg> ")
    ws.send(test_data.replace("REPLACE", uip))
    print(recv(ws))
    time.sleep(5)