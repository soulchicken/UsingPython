# request

## requests 모듈

### get 방식 : resquests.get() 매소드로 해당 사이트를 호출

- 응답을 확인하게 위해 `status_code`를 사용한다.
- 응답코드 200이면 `codes.ok` (정상 접근)
- 응답코드 403은 접근 권한이 없다라는 의미
- `raise_for_status() ` : 더 접근권한이 없으면 에러 발생

```python
import requests

res = requests.get("https://google.com")
print("응답코드 :",res.status_code) # 200이 나오면 정상, 403은 접근 권한이 없다라는 뜻

if res.status_code == requests.codes.ok:
    print("응답코드 :",res.status_code) # 응답코드 200 == requests.codes.ok
else:
    print("에러코드 :",res.status_code)
```

</br>

```python
import requests

res = requests.get("https://google.com")
res.raise_for_status() # 문제가 생기면 바로 에러 발생, 바로 끝내버림 
```

## 쓰기모드를 사용해 구글 사이트를 html 파일로 저장

```python
with open("./myvenv/UsingPython/make_google.html", "w", encoding="utf-8") as google:
    google.write(res.text)
```
