import psycopg2
#import pandas as pd
import openpyxl

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

# 엑셀파일 열기
wb = openpyxl.load_workbook('D:\PythonWorkspace\src\score.xlsx')
 
# 현재 Active Sheet 얻기
ws = wb.active
# ws = wb.get_sheet_by_name("Sheet1")
 
# 국영수 점수를 읽기
for r in ws.rows:
    row_index = r[0].row   # 행 인덱스
    kor = r[1].value
    eng = r[2].value
    math = r[3].value
    sum = kor + eng + math
 
    # 합계 쓰기
    ws.cell(row=row_index, column=5).value = sum
 
    print(row_index, r[0].value, kor, eng, math, sum)
    print("===============")
 
# 엑셀 파일 저장
wb.save("D:\PythonWorkspace\src\score3.xlsx")
wb.close()
