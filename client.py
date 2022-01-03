import threading
import socket

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


def client_receive():            #Receive dari client lagi satu
    while True:
        try:
            message = s.recv(1024).decode('utf-8')
            print(message)

            move = Main()             #call input dari main
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
            s.close()
            break 

def Main():
    host = '192.168.56.103'
    port = 8888

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Waiting for connection')

    try:
       s.connect((host, port))
    except socket.error as e:
       print(str(e))

    while True:
        move = input("Move:")           #Input Rocks, Paper atau Scissors
        s.send(move.encode('utf-8'))
        return move
    s.close()

if __name__ == '__main__':
    Main()

T1 = threading.Thread(target=client_receive)
T2 = threading.Thread(target=Main)
T1.start()
T2.start()
