import threading
from queue import Queue
import time
from scapy.all import *
import sys

target = sys.argv[1:]
open_ports = []  # List to store open ports

print_lock = threading.Lock()

def syn_scan(port):
    src_port = RandShort()
    response = sr1(IP(dst=target) / TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0)
    if response and response.haslayer(TCP):
        with print_lock:
            if response[TCP].flags == 0x12:  # SYN-ACK
                open_ports.append(port)
                print(f"Port {port} is open")
            elif response[TCP].flags == 0x14:  # RST
                print(f"Port {port} is closed")
    else:
        pass

def threader():
    while True:
        worker = q.get()
        syn_scan(worker)
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


