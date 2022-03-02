import requests

res = requests.get("https://google.com")
print("응답코드 :",res.status_code) # 200이 나오면 정상, 403은 접근 권한이 없다라는 뜻

if res.status_code == requests.codes.ok:
    print("응답코드 :",res.status_code) # 응답코드 200 == requests.codes.ok
else:
    print("에러코드 :",res.status_code)

res.raise_for_status() # 문제가 생기면 바로 에러 발생, 바로 끝내버림 
# 위에 응답코드를 확인하는 과정을 1줄로 가능하게 한다.
print("스크래핑 시작!")
print(res.text)
with open("./myvenv/UsingPython/make_google.html", "w", encoding="utf-8") as google:
    google.write(res.text)