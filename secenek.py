from tabu import tabu_baslat
from _2048oyunu import baslat
from tas_kagit import play_game
def oyun_secimi():
    secenek= input(f"hangi oyunu oynamak isterseniz\n1-2048 oyunu\n2-Tabu oyunu\n3-taş-Kağıt-makas oyunu\n")
    match secenek:
        case "1":
            baslat(callback=oyun_secimi)
            
        case"2":
            tabu_baslat(callback=oyun_secimi)
            
        case "3":
            play_game(callback=oyun_secimi)