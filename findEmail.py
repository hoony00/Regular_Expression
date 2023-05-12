import re

text = """
SangHoon's email is sanghoon@testmail.com He can also be reached at sanghoon@gmail.com .com
"""

pattern = r'[\w\.-]+@[\w\.-]+'                  # 이메일 형식 패턴 

pattern2 = '.com'                               # .com 형식 패턴

result = re.findall(pattern, text)              #이메일 패턴들을 리스트로 가져옴

result2 = re.findall(pattern2, text)            # .com 패턴들을 리스트로 가져옴

if result:
    print("이메일 패턴 찾기 성공")
    print('찾은 이메일 결과:',result)           # ['sanghoon@testmail.com', 'sanghoon@gmail.com']
    print('찾은 패턴 수:',len(result))          # 찾은 수: 2
else:
    print('이메일 패턴이 없습니다.')

print("-----------------------------------")

if result2:
    print(".com 패턴 찾기 성공")
    print('찾은 .com 패턴 결과 :', result2)     #.com 찾기 결과 : ['.com', '.com']
    print('찾은 패턴 수:',len(result2))         # 찾은 수: 3
else:
    print('찾는 .com 패턴이 없습니다.')


