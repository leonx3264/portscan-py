import socket
import threading
from queue import Queue

#print lock: lock the variable so only used once per task
print_once = threading.Lock()

server = input("enter IP: ")

def port_scan(port):
    #socket
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection = socket.connect((server,port))

        #locks print function
        with print_once:
            print("\nport:", port, "is open.")

        #closes connection when done
        connection.close()

    except:
        #if port isnt open just pass through
        pass

def threader():
    while True:
        worker = q.get()
        port_scan(worker)
        q.task_done()

q = Queue()

#range(threads)
for i in range(3000):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

#range(ports)
for worker in range(1,10000):
    q.put(worker)

q.join()

print("\nTask completed. Ports 1 to 10,000 scanned.")
close_choice = "start"
while close_choice != "":
    close_choice = input("\npress enter to close >> ")
    if close_choice == "":
        exit()
