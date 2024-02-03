import socket
import threading
from queue import Queue
import time
import sys


target = sys.argv[1:] 
open_ports = []  # List to store open ports

print_lock = threading.Lock()

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        con = s.connect((target, port))
        with print_lock:
            print(f"Port {port} is open")
            open_ports.append(port)
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()

for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

start = time.time()

for worker in range(1, 100):
    q.put(worker)

q.join()

print("Open ports:", open_ports)
print("Scanning finished in", time.time() - start, "seconds")


