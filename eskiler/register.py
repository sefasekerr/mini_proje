import csv
import re
class register:
    def register(csv_file):
        id_ = register.get_next_id(csv_file)
        name = input("isminizi giriniz: ")
        surname = input("soy isminizi giriniz: ")
        username = register.username_control(csv_file)
        password = register.password_control() 
        fieldnames = ["ID","USERNAME","NAME","SURNAME","PASSWORD"]
        with open(csv_file,"a",encoding="utf-8",newline='') as file:
            file_writer = csv.DictWriter(file,fieldnames=fieldnames)
            file_writer.writerow({
                "ID":id_,
                "USERNAME":username,
                "NAME":name,
                "SURNAME":surname,
                "PASSWORD":password
            })
    def username_control(csv_file):
        while True:
            username = input("kullanıcı adınız giriniz: ")
            with open(csv_file,"r",encoding="utf-8") as file:
                file_reader = csv.DictReader(file)
                for line in file_reader:
                    if line["USERNAME"]==username:
                        print("bu kullanıcı adı alınmış!!")
                        break
                else:
                    pattern_u= r"^[A-Za-z][A-Za-z0-9_]{4,19}$"
                    if not re.match(pattern_u,username):
                        print("❌ Geçersiz kullanıcı adı! (5-20 karakter, harf ile başlamalı, harf/rakam/_ içerebilir)")
                    else:
                        return username

    
    def get_next_id(csv_file):
        try:

            with open(csv_file,"r",encoding="utf-8") as file:
                file_reader = csv.DictReader(file)
                ids = [int(line["ID"]) for line in file_reader]
                    
                return max(ids) +1 if ids else 1
        except FileNotFoundError :
            return 1
        
    def password_control():
        while True:
            password = input("şifrenizini oluşturun: ")
            pattern_p = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!_]).{8,}$"
            sonuc = bool(re.match(pattern_p,password))
            if not sonuc:
                print("❌ Geçersiz şifre! (En az 8 karakter, büyük/küçük harf, rakam ve özel karakter içermeli)")
                
            else:
                return password


                