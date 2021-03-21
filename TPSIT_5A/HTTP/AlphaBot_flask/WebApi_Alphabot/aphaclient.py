"""
Author: Bruno Luca, Genovese Tommaso, Van Cleeff Jacopo
Date: 05-01-2021
"""

import socket
import threading
import turtle
import AlphaBot
import time



server_ip = "127.0.0.1"
server_port = 7000

def client():
    robot = AlphaBot.AlphaBot()

    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    c.connect((server_ip,server_port))
    
    while True:
        msg = input(">>")
        c.sendall(msg.encode())
        echo_msg = c.recv(4096).decode()

        print(f"ECHO>> {echo_msg}")
        _,path = echo_msg.split(',')

        print(path)

        index = 0
        while index < len(path):
            distance = ''
            if path[index] == 'F':
                index = index + 1
                while index < len(path) and path[index].isnumeric():
                    distance = distance + path[index]
                    index = index + 1
                
                robot.forward()
                time.sleep(3)
                robot.stop()


            elif path[index] == 'B':
                index = index + 1
                while index < len(path) and path[index].isnumeric():
                    distance = distance + path[index]
                    index = index + 1

                robot.backward()
                time.sleep(3)
                robot.stop()

            elif path[index] == 'L':
                index = index + 1
                while index < len(path) and path[index].isnumeric():
                    distance = distance + path[index]
                    index = index + 1

                robot.left()
                time.sleep(5)
                robot.stop()

            elif path[index] == 'R':
                index = index + 1
                while index < len(path) and path[index].isnumeric():
                    distance = distance + path[index]
                    index = index + 1

                robot.right()
                time.sleep(5)
                robot.stop()

        if msg == "close":
            break
    c.close()
    print("finito")
    


if __name__ == "__main__":

    client()