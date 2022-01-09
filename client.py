import socket
import sys

def getinput():
    isCleanInput = False
    options = ('R', 'P', 'S')

    while(isCleanInput is False):
        clientInput =input("Enter R, P, or S: ").upper()

        if clientInput in options:
            isCleanInput = True

    return clientInput

def usage():
    print('USAGE: python client.py <ADDRESS> <PORT> <BUFFERSIZE>')
    exit(0)

choices = ('R', 'P', 'S')

target = ('192.168.56.103', 8889)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(target)
bufferSize = 1024
status = clientSocket.recv(bufferSize)
player = '-1'

if b'0' in status:
    player = '1'
elif b'1' in status:
    player = '2'

print(status)

if b'queue' in status:
    while status == 'queue':
        print('The room is full, you have been added to the queue.')

        status = clientSocket.recv(bufferSize)
    print(status)
    print('You are now connected!')

isPlaying = True

while isPlaying:
    clientInput = getinput()

    if clientInput:
        clientSocket.send(clientInput.encode('utf-8') + str.encode(player))
        result = clientSocket.recv(bufferSize)

        if b'wait' in result:
            print('Waiting for your opponent!')

            result = clientSocket.recv(bufferSize)
            result = clientSocket.recv(bufferSize)

        if b'0' in result:
            print('The match was a draw!')
        elif b'1' in result and player == '1':
            print('You won!')
        elif b'1' in result and player == '2':
            print('You lost!')
        elif b'2' in result and player == '1':
            print('You lost!')
        elif b'2' in result and player == '2':
            print('You Won!')

        print('Disconnecting to make room for other players. Thank you for playing SPEED-RPS!')

        clientSocket.close()
        isPlaying = False

def reQueue():
    isPlaying = False
