
from secenek import oyun_secimi
from dbregister import Register
from dblogin2 import Login
import users
def main():
    print(f".............OYUNUMUZA HOŞGELDİNİZ............")
    print(f"{'HESABINIZ VAR MI (R)':<15} ya da {'HESAP OLUŞTURUN (L)':>15}")
    sonuc =input("hangisi: ")
    if sonuc=="L" or sonuc=="l":
        users.user = Register.run_register()
        print("ARAMIZA HOŞGELDİNN!!\n")
        return oyun_secimi()
        
    elif sonuc=="R" or sonuc=="r":
        users.user = Login.login_control()
        return oyun_secimi()
        
    # print(f"HOŞGELDİN ÖZLETME FAZLA:) {user[1]["name"].upper()}\n")
    else :
        print("hatalı tuşlama")
        return False

main()
    
