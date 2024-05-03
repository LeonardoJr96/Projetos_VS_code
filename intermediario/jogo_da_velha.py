A = ["A1", '|', "A2", '|', "A3"]
B = ["B1", '|', "B2", '|', "B3"]
C = ["C1", '|', "C2", '|', "C3"]

game = [ A, B, C ]

list_player = ["X", "O"]

def inicial_list():
   ordener = ["A", "B", "C"]
   for listi in range(3):
      for i in range(5):
         if i % 2 == 0:
            
            if i == 0:
               game[listi][i] = f'{ordener[listi]}{i + 1}'
            if i == 2:
               game[listi][i] = f'{ordener[listi]}{i}'
            elif i == 4:
               game[listi][i] = f'{ordener[listi]}{i - 1}'
               
         else:
            game[listi][i] = '|'

def view():
   for i in range(3):
      print(game[i])

def select(opt, player):
   match opt:
      case 'a1':
         A[0] = player
   
      case 'a2':
         A[2] = player
      
      case 'a3':
         A[4] = player
      
      case 'b1':
         B[0] = player
      
      case 'b2':
         B[2] = player
          
      case 'b3':
         B[4] = player
      
      case 'c1':
         C[0] = player
      
      case 'c2':
         C[2] = player
      
      case 'c3':
         C[4] = player

def line(number):
   for listi in range(3):
      if game[listi][0] == 'X' and game[listi][2] == 'X' and game[listi][4] == 'X':
         number = 1
      elif game[listi][0] == 'O' and game[listi][2] == 'O' and game[listi][4] == 'O':
         number = -1
         
   if number == 1:
      return True
   elif number == -1:
      return True
   
def column():
   for i in range(5):
      if A[i] == 'X' and B[i] == 'X' and C[i] == 'X':
         return True
      elif A[i] == 'O' and B[i] == 'O' and C[i] == 'O':
         return True
   
def oblique():
   if A[0] == 'X' and B[2] == 'X' and C[4] == 'X':
      return True
   elif A[4] == 'X' and B[2] == 'X' and C[0] == 'X':
      return True
   elif A[0] == 'O' and B[2] == 'O' and C[4] == 'O':
      return True
   elif A[4] == 'O' and B[2] == 'O' and C[0] == 'O':
      return True
                  
def game_win():
   number = 0 
   if line(number) == True:
      return True
   elif column() == True:
      return True
   elif oblique() == True:
      return True

def play_game():
   
   finished = False
   
   while finished != True:
      number = 0
      
      while number < 9:
         view()
         
         select_player = str(input('Select sector: '))
         time = number % 2
         
         if time == 0:
            player = list_player[0]
         else:
            player = list_player[1]                  
         
         select(select_player, player)
         
         number += 1
         
         if game_win() == True:
            number = 9
         
      view()
         
      finish = str(input('Try new game? '))
      
      if finish == 'no' or finish == 'n':
         finished == True
         return print(f'jogador x venceu tantos ')
      
      else:
         inicial_list()
         number = 0
   
play_game()
