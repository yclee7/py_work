import psycopg2
#import pandas as pd

conn_string = "host='localhost' dbname = 'postgres' user = 'postgres' password = 'inzent01'"

conn = psycopg2.connect(conn_string)
cur = conn.cursor()



# 일반적인 쿼리
cur.execute("SELECT * FROM films;")
result = cur.fetchall()
print ( result )

for row in result:
    print("Data row = (%s, %s, %s, %s, %s, %s)" %( str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]) ) )

#cur.close()

# pandas를 통한 쿼리
#pd.read_sql("SELECT * FROM films", conn )
#result = cur.fetchall()
#print ( pd )

# 데이터를 변경했다면 반드시 .commit() 해주어야 한다
conn.commit()

# 커서를 닫고 연걸을 종료한다.
cur.close()
conn.close()


