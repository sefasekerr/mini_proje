import pyodbc
from cachetools import cached,TTLCache
import time 
import sys
database = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=192.168.1.6;"
    "Database=ETRADE4;"
    "UID=sa;"
    "PWD=Sefa1234;",
    autocommit=True  
            )

@cached(cache=TTLCache(maxsize=32,ttl=1))
def get_product():
    cursor = database.cursor()
    cursor.execute("select * from ITEMS")
    print("from sql")
    return cursor.fetchall()


s = time.time()
d=get_product()
print(sys.getsizeof(d))
print("zaman: ",(time.time()- s))

s = time.time()
d=get_product()
print(sys.getsizeof(d))
print("zaman: ",(time.time()- s))


s = time.perf_counter()
d=get_product()
print(sys.getsizeof(d))
print("zaman: ",(time.perf_counter()- s)*1e6)


