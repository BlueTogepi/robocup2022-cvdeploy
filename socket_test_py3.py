#!/usr/bin/env python3
import socket
import cv2

HOST = 'localhost'
PORT_PERSONTRACK = 4501
PORT_WHATSTHIS = 4502

# img = cv2.imread("test_img/PC_Webcam_M_1.jpg")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT_PERSONTRACK))
    # s.sendall(img.tobytes())
    s.sendall(b"abcde")
    data = s.recv(1024)

print('Received', repr(data))