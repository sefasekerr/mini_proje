from database import Database

def score_save():
    database=Database.get_connection()
    cursor = database.cursor()
    cursor.execute("select * from scores")
    i = cursor.fetchone()
    print(i)
    
score_save()