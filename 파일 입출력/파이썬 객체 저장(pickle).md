# 파이썬 객체 (pickle)

## 파이썬 객체 저장

```python
import pickle
# 데이터를 딕셔너리 형태로 생성했다고 치자
data = {
    "파이썬" : "문법은 편하다",
    "자바" : "문법은 귀찮다"
}
# "wb" : w는 쓰기모드라는 뜻이고 b는 컴퓨터가 바로 읽을 수 있는 데이터 형식이라는 뜻
file = open("./myvenv/UsingPython/data.pickle","wb")
# dump 함수로 data를 file에 넣게 된다.
pickle.dump(data,file)
file.close()
```

## 파이썬 객체 읽기

```python
import pickle
# "rb" : r은 읽기모드. b는 데이터 형식
file = open("./myvenv/UsingPython/data.pickle","rb")
data = pickle.load(file)
print(data)
file.close()
```

## with 사용하기

### 사용 전

```python
file = open("./myvenv/UsingPython/text.txt","r")
data = file.read()
file.close()
```

### 사용 후 : with 들여쓰기가 끝난 부분부터 파일 close

```python
with open("./myvenv/UsingPython/text.txt","r") as file:
    data = file.read()
```
