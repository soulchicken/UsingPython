# 파일 쓰기
import csv

data = [
    ["학번","학과","이름"],
    ["C123123","동양화과","김서양"],
    ["C345345","서양화과","김동양"],
    ["C456456","건축학과","김모래"]
]

file = open("./myvenv/UsingPython/student.csv","w",newline="",encoding="utf-8-sig")
writer = csv.writer(file)
for line in data:
    writer.writerow(line)
file.close()

# 파일 읽기
import csv

file = open("./myvenv/UsingPython/student.csv","r",encoding="utf-8-sig")
reader = csv.reader(file)
for data in reader:
    print(data)
file.close()