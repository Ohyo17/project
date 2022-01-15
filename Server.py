import socket
from signal import signal, SIGPIPE, SIG_DFL  
signal(SIGPIPE,SIG_DFL)

HOST = ""
PORT = 8889


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
                s.bind((HOST, PORT))
                s.listen()
                conn1, addr1 = s.accept()
                with conn1:
                       print("Connected to", addr1)
                       conn2, addr2 = s.accept()
                       with conn2:
                              print("Connected to", addr2)
                              while True:
                                    try:
                                        conn1.sendall(b"\n")
                                        conn2.sendall(b"\n")
                                        data = b""
                                        while not data:
                                                 data = conn1.recv(1024)
                                        conn2.sendall(data)
                                        data = b""
                                        while not data:
                                                    data = conn2.recv(1024)
                                        conn1.sendall(data)
                                    except:
                                           s.close()
