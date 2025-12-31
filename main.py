import random as rnd
from os import remove
size =2

min_skor=0
max_skor =2
total_skor = 0
def new_board():
    board=[[0]*size for _ in range(size)]
    ad_new_board(board)
    ad_new_board(board)
    return board

def skor_print():
    skor_list = [0]
    with open("totalskor.txt","r",encoding="utf-8") as file:
        for satir in file.readlines():
            if isinstance(satir,(str,)) :
                satir = satir.strip()
                yazi ,skor = satir.split(":")
                skor = int(skor)
                skor_list.append(skor)
            
        return print(f"maksimum skor: {max(skor_list)}\n")

def kayit_güncelleme():
    max_sko = 0
    with open("totalskor.txt","r+",encoding="utf-8") as file:
        for satir in file.readlines():
            satir = satir.strip()
            if ":" in satir:
                yazi ,skor = satir.split(":")
                skor = int(skor)
                if skor>max_sko:
                    max_sko = skor
        file.seek(0)       
        file.truncate()    
        file.write(f"maksimum skor: {max_sko}\n")

    
    
def ad_new_board(board):
    empty = [(r,c)for r in range(size) for c in range(size) if board[r][c] ==0]
    if empty:
        r,c =rnd.choice(empty)
        board[r][c]= rnd.choice([2,2,2,4])
    else:
        print("game over!!")
        skor_print()
        kayit_güncelleme()
        return "q"


def kayit(board):
    global min_skor , total_skor ,max_skor
    
    with open("max_skor.txt","a",encoding="utf-8") as file:
        for row in board:
            for i in row:
                if max_skor<i:
                    max_skor=i
                    total_skor +=max_skor
        if  min_skor !=max_skor :
            file.writelines(f"güncel maksimum skor: {str(max_skor)}\n")
        min_skor=max_skor
        

def print_board(board):
    for row in board:
        print(row)
    skor_print()
    print()

def compress(row):
    new_row=[num for num in row if num !=0]
    new_row+=[0]* (size-len(new_row))
    return new_row

def merge(row):
    global total_skor
    for i in range(size-1):
        if row[i]!=0 and row[i]==row[i+1]:
            row[i]+=row[i]
            row[i+1]=0
            total_skor += row[i]
            with open("totalskor.txt","a",encoding="utf-8") as file:
                file.writelines(f"total skor: {str(total_skor)}\n")
        
    return row

def move_left(board):
    new_board=[]
    for row in board:
        row=compress(row)
        row=merge(row)
        row=compress(row)
        new_board.append(row)
    return new_board

def move_right(board):
    new_board=[]
    for row in board:
        row=row[::-1]
        row=compress(row)
        row=merge(row)
        row=compress(row)
        row=row[::-1]
        new_board.append(row)
    return new_board

def tersboard(board):
    return [list(row) for row in zip(*board)]

def move_up(board):
    board = tersboard(board)
    board = move_left(board)
    board =tersboard(board)
    return board

def move_down(board):
    board = tersboard(board)
    board = move_right(board)
    board =tersboard(board)
    return board


board = new_board()

print_board(board)

while True:
    move = input("Hamle (w=up, s=down, a=left, d=right, q=quit): ")
    if move == 'q' or ad_new_board(board) =="q":
        break
    elif move == 'a':
        board = move_left(board)
    elif move == 'd':
        board = move_right(board)
    elif move == 'w':
        board = move_up(board)
    elif move == 's':
        board = move_down(board)
    else:
        print("Geçersiz hamle!")
        continue

    ad_new_board(board)
    print_board(board)
    kayit(board)

# while True:
#     move = input("w=yukarı,s=aşağı,a=sola,s=sağa")
#     match move:
#         case "w":
#             board = move_up(board)
#         case "a":
#             board =move_left(board)
#         case "s":
#             board =move_right(board)
#         case "d":
#             board =move_down(board)
#         case "q":
#             break
#         case _:
#             print("hatalı giriş")
        
#     ad_new_board(board)
#     print_board(board)        






# board = [(r,c)for r in range(size) for c in range(size) if board[r][c] !=0]
# print(board)