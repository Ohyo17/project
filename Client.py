import socket
import sys
HOST = "192.168.56.103"
PORT = 8888

print("Welcome to Speed ROCK, PAPER, SCISSOR\n")

win = 0
loss = 0

def rocks(x,y):
      global win,loss
      move = x
      opponent = y

      if move == opponent:

              print( "It's Tie\n")
              win = win + 1
              loss = loss + 1
              print("Player:",win,"\tOpponent:",loss,"\n")

      elif move == 'r' and opponent == 's':

              print("You win\n")
              win = win+ 1
              print("Player:" ,win, "\tOpponent:", loss,"\n")

      elif move == 'r' and opponent == 'p':

              print("You lose\n")
              loss = loss + 1
              print("Player:",win,"\tOpponent",loss,"\n")

      else:
              print("Invalid move Rocks\n")


def paper(x,y):
      global win,loss
      move = x
      opponent = y

      if move == opponent:
               print("It's a Tie\n")

               win = win + 1
               loss = loss + 1
               print("Player:",win,"\tOpponent:",loss,"\n")

      elif move == 'p' and opponent == 's':

               print("You lose\n")
               loss = loss+ 1
               print("Player:" , win,"\tOpponent:", loss,"\n")

      elif move == 'p' and opponent == 'r':

               print("You win\n")
               win = win + 1
               print("Player:",win,"\tOpponent:",loss,"\n")
      else:
           print("Invalid move Paper\n")



def scissor(x,y):
      global win,loss
      move = x
      opponent = y

      if move == opponent:
               print("It's a Tie\n")

               win = win + 1
               loss = loss + 1
               print("Player:",win,"\tOpponent:",loss,"\n")

      elif move == 's' and opponent == 'p':

               print("You win\n")
               win = win+ 1
               print("Player:" , win,"\tOpponent:", loss,"\n")

      elif move == 's' and opponent == 'r':
               print("You lose\n")
               loss = loss + 1

               print("Player:",win,"Opponent:",loss,"\n")
      else:
               print("Invalid move Scissors")



def score():
      global win,loss

      if(win>loss):
               print("You are the winner")
               print("Thank you for playing Speed Rocks,Paper,Scissor\n")
               s.close()

      elif(win == loss):
               print("It's Deuce")
               print("Thank you for playing Speed Rocks,Paper,Scissor\n")
               s.close()

      else:
               print("You are the loser")
               print("Thank you for playing Speed Rocks,Paper,Scissor\n")
               s.close()



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        while True:
               data = b""
               while data != b"\n":
                     data = s.recv(1024)
               print("Please choose 'r' for Rocks, 'p' for Paper, 's' for Scissor or exit to close the program\n")
               move = input("r,p,s: ")
               s.sendall(str.encode(move))

               data = b""
               while not data:
                     data = s.recv(1024)

               opponent = data.decode('utf-8')
               
               print("Received:", opponent)

               if move == 'r':
                       rocks(move,opponent)

               elif move == 'p':
                       paper(move,opponent)

               elif move == 's':
                       scissor(move,opponent)

               elif move == 'exit':
                       score()
                       break
                       sys.exit()
               else:
                   print("Invalid Move or words\n")
