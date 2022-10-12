import psycopg2

conn_string = "host='localhost' dbname = 'postgres' user = 'postgres' password = 'inzent01'"

conn = psycopg2.connect(conn_string)
cur = conn.cursor()



# example 1
#cur.execute("INSERT INTO numbers VALUES (%d)", (42,)) # WRONG
#cur.execute("INSERT INTO numbers VALUES (%s)", (42,)) # correct

# example 2
#cur.execute("INSERT INTO foo VALUES (%s)", "bar")    # WRONG
#cur.execute("INSERT INTO foo VALUES (%s)", ("bar"))  # WRONG
#cur.execute("INSERT INTO foo VALUES (%s)", ("bar",)) # correct
#cur.execute("INSERT INTO foo VALUES (%s)", ["bar"])  # correct

# exampel 3
#SQL = "INSERT INTO authors (name) VALUES (%s);" # Note: no quotes
#data = ("O'Reilly", )
#cur.execute(SQL, data) # Note: no % operator

# test 테이블의 모든 데이터를 가져오고 출력한다
#cur.execute("SELECT * FROM test;")
#print cur.fetchone()

cur.execute("SELECT * FROM films;")
#result = cur.fetchall()
print ( cur.fetchone() )

# 데이터를 변경했다면 반드시 .commit() 해주어야 한다
conn.commit()

# 커서를 닫고 연걸을 종료한다.
cur.close()
conn.close()


