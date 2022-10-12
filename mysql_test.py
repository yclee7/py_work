import pymysql

connect = pymysql.connect(host='192.168.56.123', port=3306, user='igate', password='igate', db='IGATE',\
                          charset='utf8')
cur = connect.cursor()


query = "SELECT * FROM igt_user"
cur.execute(query)
#connect.commit()




# fetchall() : 지정 테이블 안의 모든 데이터를 추출
# fetchone() : 지정 테이블 안의 데이터를 한 행씩 추출
# fetchmany(size=원하는 데이터 수) : 지정 테이블 안의 데이터를 size 개의 행을 추출

datas = cur.fetchall()

print(datas)

for data in datas:
	#print(data)
    print("Data row = (%s, %s, %s, %s, %s, %s)" %( str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]) ) )
# for row in result:
    # print("Data row = (%s, %s, %s, %s, %s, %s)" %( str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]) ) )



# while data:
#      data = cur.fetchone()
#      print(data)

cur.close()
connect.close()




# conn_string = "host='localhost' dbname = 'postgres' user = 'postgres' password = 'inzent01'"

# conn = psycopg2.connect(conn_string)
# cur = conn.cursor()



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

# cur.execute("SELECT * FROM films;")
# #result = cur.fetchall()
# print ( cur.fetchone() )

# 데이터를 변경했다면 반드시 .commit() 해주어야 한다
#conn.commit()

# 커서를 닫고 연걸을 종료한다.
# cur.close()
# conn.close()


