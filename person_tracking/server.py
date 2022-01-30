#!/usr/bin/env python3
import socket
import os
import cv2
import numpy as np

print("Server started")

HOST = "0.0.0.0"
PORT = int(os.environ.get('SOCKET_PORT'))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print("Listening at port %d..." % PORT)
while True:
    conn, addr = s.accept()
    data = b""
    print('Connected by', addr)
    while True:
        pkt = conn.recv(1024)
        data += pkt
        print(addr, ":", repr(pkt))
        if not data:
            print(addr, "has finished sending")
            break
    # img = np.frombuffer(data, dtype=np.uint8)
    # img = cv2.resize(img, (504, 896))
    # cv2.imwrite("test_img/received.jpg", img)
    print("Received:", repr(data))
    s.send(b"Ack from server")
