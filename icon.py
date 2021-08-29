import socket
import threading

## table = [['location', 'pheripheral_id', 'status', 'test-time', 'test-result', 'disinfection', 'disinfection-time'], 
## [geohash, id, status, test-time, test-result, ]]

HEADER= 64
port = 5050
FORMAT= 'utf-8'
DISCONNECT_MESSAGE= "Disconnected"
host= socket.gethostbyname(socket.gethostname())
# creating socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#now to bind the socket
address= (host, port)
server.bind(address)

def handle_client(conn, addr):
  print(f"[New connection] {addr} connected")
  connected = True
  while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
      msg_length = int(msg_length)
      msg = conn.recv(msg_length).decode(FORMAT)
      print(msg)
      if msg == DISCONNECT_MESSAGE:
        connected = False
      print(f"[{addr}] {msg}")
      return msg
  conn.close()


def start():
  server.listen()
  print(f"[Listening] Server is listening on {host} ")
  while True:
    conn, addr = server.accept()
    #thread to the handle_client function
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    # shows us how many threads are open on the process
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("server is listening......")
start()
