import re
pattern1 = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$"
pattern = r"^[A-Za-z][A-Za-z0-9_]{4,19}$"



username = "sefasekerr"
password = "pekmezzz"

# sonuc = bool(re.match(pattern,username))
# print(sonuc)

# sonuc1 = bool(re.match(pattern1,password))
# print(sonuc1)


def password_control():
        while True:
            password = input("şifrenizini oluşturun: ")
            pattern_p = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!_]).{8,}$"
            sonuc = bool(re.match(pattern_p,password))
            if not sonuc:
                print("❌ Geçersiz şifre! (En az 8 karakter, büyük/küçük harf, rakam ve özel karakter içermeli)")
                
            else:
                
                return password
password_control()


pattern_u= r"^[A-Za-z][A-Za-z0-9_]{4,19}$"