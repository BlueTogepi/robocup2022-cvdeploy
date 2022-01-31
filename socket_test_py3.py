#!/usr/bin/env python3
import socket
import cv2
import struct

HOST = 'localhost'
PORT_PERSONTRACK = 4501
PORT_WHATSTHIS = 4502

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

img = cv2.imread("test_img/PC_Webcam_M_1.jpg")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT_PERSONTRACK))
    send_msg(s, img.tobytes())
    data = s.recv(1024)

print('Success, Time =', data.decode())