#day1

"""
str1 = 'hello'
str2 = "hello2"
"""
#str3 = """hello my name is choi"""
#print(str2)

"""
listdata = [str1, "hello3", str2, '22', [1,2,3,4]]    #listdata는 단지 함수명과 같은 리스트 이름
print(listdata[3])
print(listdata[4][3])                                 #리스트 안에 리스트를 만들경우 이렇게 출력해야 함

listdata.remove('22')                                 #del listdata[3] 과 listdata.remove('22') 는 같은 동작을 수행하는 명령어 ※del listdata 로 리스트 전체를 지울수 있다
print(listdata[3])                                    #리스트 멤버중 하나를 지우면 번호가 당겨짐

listdata.append('22')                                 #리스트 멤버 추가
print(listdata[4])                                    #listdata = [str1, "hello3", str2, [1,2,3,4,], '22'] 인 상태
"""
"""
mydata = {'choi':2002, 23:'age'}                      #사전 자료 만들기 키:값
print(mydata['choi'], mydata[23])

mydata['name'] = 'sy'                                 #사전 멤버 추가
print(mydata['name'])

del mydata['choi']                                    #사전 멤버 삭제
print(mydata)

print(mydata.keys())                                  #키 추출
print(mydata.values())                                #값 추출
print(mydata.items())
"""
"""
tupledata = (1,2,3)                                   #[]는 리스트, ()는 튜플
print(tupledata)                                      #리스트는 멤버값 수정, 멤버 추가 가능 / 튜플은 불가
"""

