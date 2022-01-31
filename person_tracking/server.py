#!/usr/bin/env python3
import socket
import os
import cv2
import numpy as np
import struct
import time

print("Server started")

HOST = "0.0.0.0"
PORT = int(os.environ.get('SOCKET_PORT'))
CAM_WIDTH = int(os.environ.get('CAM_WIDTH'))
CAM_HEIGHT = int(os.environ.get('CAM_HEIGHT'))

def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)

def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)

def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print("Listening at port %d..." % PORT)
while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    start = time.time()
    data = recv_msg(conn)
    img = np.frombuffer(data, dtype=np.uint8)
    img = np.reshape(img, (CAM_WIDTH, CAM_HEIGHT, 3))
    end = time.time()
    cv2.imwrite("test_img/received.jpg", img)
    conn.send(str(end - start).encode())
