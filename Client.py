import socket
HOST = "192.168.56.103"
PORT = 8889

print("Welcome to Speed ROCK, PAPER, SCISSOR\n")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
               move = input('Rocks, Paper, Scissors or Exit : ')
               s.sendall(str.encode(move))
               
               data = b""
               while data != b"\n":
                     data = s.recv(1024)

               data = b""
               while not data:
                     data = s.recv(1024)
               opponent = data.decode('utf-8')
               
               print("Received:", opponent)

               if move == "Rocks":
                       if move == opponent:
                             print( "It's Tie\n")
                       elif move == 'Rocks' and opponent == 'Scissors':
                             print("You win\n")
                       elif move == 'Rocks' and opponent == 'Paper':
                             print("You lose\n")
                       else:
                             print("Invalid move Rocks\n")

               elif move == 'Paper':
                       if move == opponent:
                             print("It's a Tie\n")
                       elif move == 'Paper' and opponent == 'Scissors':
                             print("You lose\n")
                       elif move == 'Paper' and opponent == 'Rocks':
                             print("You win\n")
                       else:
                             print("Invalid move Paper\n")

               elif move == 'Scissors':
                       if move == opponent:
                             print("It's a Tie\n")
                       elif move == 'Scissors' and opponent == 'Paper':
                             print("You win\n")
                       elif move == 'Scissors' and opponent == 'Rocks':
                             print("You lose\n")
                       else:
                             print("Invalid move Scissors")

               elif move == 'Exit':
                       print("Thank you for playing Speed Rocks,Paper,Scissor\n")
                       break
               else:
                   print("Invalid Move")
