# 파일 쓰기
data = "hello, my name is LEE"
with open("test.txt", "w") as fp:
    fp.write(data)

# 파일 읽기
with open("test.txt", "r") as fp:
    print("========= [파일 읽기 결과] =========")
    print(fp.read())