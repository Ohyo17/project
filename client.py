import threading
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.56.103', 8888))

def rocks(x,y):           #function Rocks(x = move)(y = message)

    if(x == y):
       result = "It's Tie"
    elif(x == 'Rocks' and y == 'Scissors'):
       result = "You win"
    elif(x == 'Rocks' and y == 'Paper'):
       result = "You lose"
    else:
       result = "Invalid move"
       return result

def paper(x,y):          #function paper(x = move)(y = message)

    if(x == y):
      result = "It's a Tie"
    elif(x == 'Paper' and y == 'Scissors'):
      result = "You lose"
    elif(x == 'Paper' and y == 'Rocks'):
      result = "You win"
    else:
      result = "Invalid move"
      return result

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

def client_send():            #Apa yang kita nak send kat client lagi satu
    while True:
        move = input("Move:")
        client.send(str.encode(move))
        return move
        
def client_receive():            #Receive dari client lagi satu
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)

            move = client_send()             #call input dari client_send
            print(move)

            if(move == 'Rocks'):             #call function untuk hantar data kat function diorang untuk process result
                result = rocks(move,message) #tapi tak pasti call function ni letak kat mana sepatutnya
                print(result)
            elif(move == 'Paper'):
                result = paper(move,message) 
                print(result)
            elif(move == 'Scissor'):
                result = scissor(move,message)
                print(result)
            else:
                print("Invalid Move")

        except:
            print('Error!')
            client.close()
            break 
