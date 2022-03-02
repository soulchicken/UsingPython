# CSV 파일 입출력

## csv (comma-separated values)
- 콤마로 구분된 텍스트 파일
- `import csv` : csv 모듈을 받아와야한다.

## csv 파일 쓰기
```python
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
```
- 실행 이후 생성된 파일
```
학번,학과,이름
C123123,동양화과,김서양
C345345,서양화과,김동양
C456456,건축학과,김모래
```

## csv 파일 읽기
```python
import csv
file = open("./myvenv/UsingPython/student.csv","r",encoding="utf-8-sig")
reader = csv.reader(file)
for data in reader:
    print(data)
file.close()
```
- 실행 이후 콘솔에 출력된 모습
```
['학번', '학과', '이름']
['C123123', '동양화과', '김서양']
['C345345', '서양화과', '김동양']
['C456456', '건축학과', '김모래']
```