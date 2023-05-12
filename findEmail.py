import re

text = """
SangHoon's email is sanghoon@testmail.com He can also be reached at sanghoon@gmail.com
"""

pattern = r'[\w\.-]+@[\w\.-]+'  # 이메일 형식 패턴 

result = re.findall(pattern, text) #이메일 패턴들을 리스트로 가져옴

if result:
    print("기본 예제에서 패턴 찾기 성공")
    print(result) #['sanghoon@testmail.com', 'sanghoon@gmail.com']
else:
    print('찾는 패턴이 없습니다.')