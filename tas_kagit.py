import random
from abc import ABC,abstractmethod
import users
class Player(ABC):
    def __init__(self,name):
        self.name = name
        self.score = 0
        self.moveHistory = []
        
    @abstractmethod
    def make_move(self):
        pass
    
class computerPlayer(ABC):
    def __init__(self):
        self.name = "bilgisayar"
        self.score = 0
        self.moveHistory = []
        
    @abstractmethod
    def make_move(self):
        pass
    
    
class HumanPlayer(Player):
    def make_move(self):
        move=input("hamleni yap taş/kağıt/makas: ")
        self.moveHistory.append(move)
        return move        
        
class RandomComputerPlayer(computerPlayer):
    def make_move(self):
        move=random.choice(["taş","kağıt","makas"])
        self.moveHistory.append(move)
        return move    
    
def kazanan(player_move,computer_move):
    if player_move == computer_move:
        return "berabere"
    elif (player_move=="taş" and computer_move=="makas") or (player_move=="makas" and computer_move=="kağıt")or(player_move=="kağıt" and computer_move=="taş"):
        return "oyuncu"
    else:
        return "bilgisayar"
        


def play_game(callback=None):
    name =users.user["name_"]
    player  =HumanPlayer(name) 
    computer = RandomComputerPlayer()

    while True:
        player_move = player.make_move()
        computer_move = computer.make_move()
        
        print(f"{player.name} hamlesi: {player_move}")
        print(f"{computer.name} hamlesi: {computer_move}")
        
        winner = kazanan(player_move,computer_move)
        
        if winner=="oyuncu":
            print(f"kazanan {player.name}")
            player.score +=1
            
        elif winner=="bilgisayar":
            print(f"kazanan {computer.name}")
            computer.score += 1
        else:
            print("berabere")
            
        print(f"{'skor':<5}|{player.name:<8}:{player.score:<3} | {computer.name:<00}:{computer.score}|")
        
        cont = input("devam etmek istiyor musunuz? (e/h): ")
        if cont != "e":
            print("oyun bitti!")
            print(f"toplam skor: {player.name:<10}:{player.score:<3} | {computer.name:<10}:{computer.score:<3}|")
            print(f"hamle geçmişi {player.moveHistory}")
            print(f"hamle geçmişi {computer.moveHistory}")
            return callback
            
            
            break