import re

# 문자열에서 'Computer System'이라는 패턴을 찾는 예제
text = "My computer system is the best computer system"
pattern = "computer system"

result = re.search(pattern, text)

if result:
    print("기본 예제에서 패턴 찾기 성공")
    print("찾은 패턴 :",result.group())  # 'Computer System' 출력
else:
    print('찾는 패턴이 없습니다.')
