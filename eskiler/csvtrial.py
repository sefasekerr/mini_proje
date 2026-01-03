import csv
from random import randint
with open("deneme.csv","r",encoding="utf-8") as file :
    csv_reader = csv.DictReader(file)
    liste = list(csv_reader)
    rnd = randint(1,len(liste))
    
    text = next(i for i in liste if int(i["ID"])==rnd)
    print((text["BASEWORD"]))
    print(text["HELPERWORD"])
    helper = text["HELPERWORD"].split(";")
    temiz = [kelime.strip("[]")for kelime in helper]
    print(temiz)
    
print(
f"___________________\n"
f"|Sefa tabu oyunu :)|\n"
f"|{"":>5}*{text['BASEWORD']:<12}|\n"
f"|                  |\n"
f"|>Yasaklı Kelimeler|"
)
for kelime in temiz:
    print(f"|{"":>5}*{kelime:<12}|")
print(
f"|                  |\n"
f"‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n")
# f"|{"":>5}{temiz[0]:<13}|\n"
# f"|{"":>5}{temiz[1]:<13}|\n"
# f"|{"":>5}{temiz[2]:<13}|\n"
# f"|                  |\n"
# f"|                  |\n"
# # )

