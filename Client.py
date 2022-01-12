import socket
HOST = "192.168.56.103"
PORT = 8889

print("Welcome to Speed ROCK, PAPER, SCISSOR\n")

def rocks(x,y):

      move = x
      opponent = y

      if move == opponent:
              print( "It's Tie\n")
      elif move == 'rocks' and opponent == 'scissors':
              print("You win\n")
      elif move == 'rocks' and opponent == 'paper':
              print("You lose\n")
      else:
              print("Invalid move Rocks\n")

def paper(x,y):

      move = x
      opponent = y

      if move == opponent:
               print("It's a Tie\n")
      elif move == 'paper' and opponent == 'scissors':
               print("You lose\n")
      elif move == 'paper' and opponent == 'rocks':
               print("You win\n")
      else:
           print("Invalid move Paper\n")

def scissor(x,y):

      move = x
      opponent = y

      if move == opponent:
               print("It's a Tie\n")
      elif move == 'scissors' and opponent == 'paper':
               print("You win\n")
      elif move == 'scissors' and opponent == 'rocks':
               print("You lose\n")
      else:
               print("Invalid move Scissors")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
               move = input('rocks, paper,scissors or exit : ')
               s.sendall(str.encode(move))
               
               data = b""
               while data != b"\n":
                     data = s.recv(1024)

               data = b""
               while not data:
                     data = s.recv(1024)
               opponent = data.decode('utf-8')
               
               print("Received:", opponent)

               if move == "rocks":
                       rocks(move,opponent)

               elif move == 'paper':
                       paper(move,opponent)

               elif move == 'scissors':
                       scissor(move,opponent)

               elif move == 'exit' or move == "Exit":
                       print("Thank you for playing Speed Rocks,Paper,Scissor\n")
                       break
               else:
                   print("Invalid Move")
