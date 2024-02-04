import threading
from queue import Queue
import time
from scapy.all import *
import sys
import subprocess

# Use sys.argv[1] to get the first command-line argument (index 1)
target = sys.argv[1] if len(sys.argv) > 1 else None

if not target:
    print("Please provide a target IP address.")
    sys.exit(1)

open_ports = []  # List to store open ports
print_lock = threading.Lock()

def syn_scan(port):
    src_port = RandShort()
    response = sr1(IP(dst=target) / TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0)
    if response and response.haslayer(TCP):
        with print_lock:
            if response[TCP].flags == 0x12:  # SYN-ACK
                open_ports.append(str(port))  # Convert the port to a string before appending
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

# Convert the list of open ports to a string with commas
open_ports_string = ','.join(open_ports)

# Now you can use open_ports_string and target in your subprocess command
subprocess.run(["DDOS.exe", open_ports_string, target])
