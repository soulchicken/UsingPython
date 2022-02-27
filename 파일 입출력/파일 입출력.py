## 파일 쓰기 과정
file = open("./myvenv/UsingPython/text.txt", "w") # text.txt 파일을 w(쓰기) 모드로 열겠다.
file.write("123123") # "123123"을 text.txt에 입력하겠다.
file.close() # text.txt 파일을 닫겠다.

## 파일 추가 과정
file = open("./myvenv/UsingPython/text.txt", "a") # text.txt 파일을 a(추가) 모드로 열겠다.
file.write("\n456456") # "456456"을 text.txt에 추가로 입력하겠다.
# file.close() # text.txt 파일을 닫겠다.


## 파일 읽기 과정
# file = open("text.txt", "r") # text.txt 파일을 r(읽기) 모드로 열겠다.
# data = file.read() # text.txt을 읽겠다. (data 변수에 파일 내용을 넣는다.)
# file.close() # text.txt 파일을 닫겠다.

## 파일 한 줄씩 읽기
'''
123123
456456
이 출력된다.
'''
file = open("./myvenv/UsingPython/text.txt","r")
while True:
  data = file.readline()
  print(data, end = "")
  if data == "":
    break
file.close()