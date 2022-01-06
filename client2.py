import socket

ClientSocket = socket.socket()
host = '192.168.56.103'
port = 8889

print('Waiting for connection')

try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

def scissor(x,y):        #function scissors(x = move)(y = message)

     if(x == y):
       result = "It's a Tie"
     elif(x == 'Scissors' and y == 'Paper'):
       result = "You win"
     elif(x == 'Scissors' and y == 'Rocks'):
       result = "You lose"
     else:
       result = "Invalid move"

       return result

while True:
    move = input('Say Something: ')
    ClientSocket.send(str.encode(move))
    message = ClientSocket.recv(1024)
    opponent = message.decode('utf-8')

    if move == 'Rocks':
          if move == opponent:
               print( "It's Tie")
          elif move == 'Rocks' and opponent == 'Scissors':
               print("You win")
          elif move == 'Rocks' and opponent == 'Paper':
               print("You lose")
          else:
               print("Invalid move")
    elif move == 'Paper':
           if move == opponent:
                print("It's a Tie")
           elif move == 'Paper' and opponent == 'Scissors':
                print("You lose")
           elif move == 'Paper' and opponent == 'Rocks':
                print("You win")
           else:
                print("Invalid move")
    elif move == 'Scissor':
            if move == opponent:
                result = "It's a Tie"
            elif move == 'Scissors' and opponent == 'Paper':
                result = "You win"
            elif move == 'Scissors' and opponent == 'Rocks':
                result = "You lose"
            else:
                result = "Invalid move"
    else:
            print("Invalid Move")

ClientSocket.close()
