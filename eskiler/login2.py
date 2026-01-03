import csv
import re
class Login2:
    def login_control(csv_file):
        username = input("kullanıcı adınızı giriniz: ")
        with open(csv_file,"r",encoding="utf-8") as file:
            file_reader = csv.DictReader(file)
            for line in file_reader:
                if line["USERNAME"]== username:
                    for i in range(3,0,-1):
                        password = input("şifrenizi giriniz: ")
                        if line["PASSWORD"] == password:
                            print("giriş başarılı yönlendiriliyorsunuz...\n")
                            return line

                        else:
                            print(f"şifre yanlış!!(kalan deneme hakkınız: {i-1})")
                    print("hakkınız doldu giriş başarısız!!!")
                    return False

            return False
        
    def setName(line,csv_file):
        name = input("yeni isminizi giriniz: ")
        with open(csv_file,"r",encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            line = list(csv_reader)
            print(line)
            

Login2.setName(Login2.login_control("users.csv"),"users.csv")  
        