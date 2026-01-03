import csv
import re
import datetime
class Register2:
    
    def __init__(self,csv_file,name,surname):
        self.__name =name
        self.__surname =surname
        self.__username =Register2.username_control(csv_file)
        self.__password =Register2.password_control()
        self.created_date = datetime.datetime.now()
        self.id=Register2.get_next_id(csv_file)
        Register2.kayit(self,csv_file)
        
    @property
    def name(self):
        
        return self.__name
        
    @property
    def surname(self):
        return self.__surname

    @property
    def username(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password



    @name.setter
    def setName(self,value):
        pattern_u= r"^[A-Za-z]{1,25}$"
        if not re.match(pattern_u,value):
            print("❌ Geçersiz isim ")
        else:
            self.__name=value



    @surname.setter
    def setSurname(self,value):
        pattern_u= r"^[A-Za-z]$"
        if not re.match(pattern_u,value):
            print("❌ Geçersiz isim ")
        else:
            self.__surname = value

    @name.setter
    def setUserame(self,value):
        pattern_u= r"^[A-Za-z][A-Za-z0-9_]{4,19}$"
        if not re.match(pattern_u,value):
            print("❌ Geçersiz kullanıcı adı! (5-20 karakter, harf ile başlamalı, harf/rakam/_ içerebilir)")
        else:
            self.__username=value

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
                    
                    
    def kayit(self,csv_file):
        fieldnames = ["ID","USERNAME","NAME","SURNAME","PASSWORD","CREATEDDATE"]
        with open(csv_file,"a",encoding="utf-8",newline='') as file:
            file_writer = csv.DictWriter(file,fieldnames=fieldnames)
            file_writer.writerow({
                "ID":self.id,
                "USERNAME":self.username,
                "NAME":self.name,
                "SURNAME":self.surname,
                "PASSWORD":self.password,
                "CREATEDDATE":self.created_date
            })
                    
    def __repr__(self):
        return f"{self.name}-{self.surname}-{self.username}-{self.password}-{self.id}-{self.created_date}"
    
    
item1 = Register2("users.csv","sefa","şeker")
print(item1)
print(item1.name)

print(item1.name)

print(item1)
    