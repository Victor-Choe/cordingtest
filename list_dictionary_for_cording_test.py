# a= [1,2,3,4,5,6,7,8]
#
# print(len(a))
# print(a[3])
# print(a[1:3])
# print(5 in a)
# print(a.count(4))
# print(a.index(5))
# a.append(9)
# print(a)
# a.pop(4)
# print(a)
# a.pop()
# print(a)
# a.pop(0)
# print(a)
# del a[1] #인덱스에 해당하는값 삭제
# print(a)
# a.sort() #정렬
# a.reverse()
# print(a)
# a.insert(3,5) 인덱스 3번째에 5 삽입
# print(a)

#파이썬 리스트는 자료형과 상관없이 자유롭게 때려박기 가능.
#
# 리스트에 없는 것에 대한 에러처리는?
# 만약 a[9] 로 하면 없는 인덱스기에 콘솔창에 에러가 표시됨.IndexError 이런식으로. 그럼
# 아래의 방식으로 예외 처리
#
# try:
#     print(a[9])
# except IndexError:
#     print(존재하지 않는 인덱스)
#
# 파이썬에서 값 삭제의 경우 del a[인덱스] 로 인덱스 삭제를 하거나 a.remove(값) 으로 값 삭제 가능
#
# 파이썬의 리스트는 연속된 공간에 요소를 배치하는 배열의 장점과 다양한 타입을 연결할 수 있는 연결리스트의 장점을 모두 취한 형태이기에 실제로 리스트를 잘 사용하기만 해도
# 겁나 강력하다. 때문에 파이썬은 아에 원시 자료형은 제공하지도 않는다. 애초에 리스트는 요소에 대한 포인터 목록을 갖고있는 구조체로 선언되어 있으며 리스트에 요소를 추가하거나 조작하기 시작하면
# ob_item의 사이즈를 조절해나가는 방식으로 구현되어 있음
#
# 딕셔너리의 경우 내부는 해시 테이블로 구현되어있다 대부분 시간 복잡도가 O(1) 이기에 최대한 활용해야함
# 3.7 부터는 입력 순서가 유지됨.
#
# a={'key1':'value1','key2':'value1','key3':'value1','key4':'value1',}
# try:
#     print(a['key6'])
# except KeyError:
#     print("존재하지 않는 키")
#
# #딕셔너리에 있는 키/값은 for 반복문으로도 조회 가능
#
# for k,v in a.items():
#     print(k,v)
#
# del a['key1']
# print(a)

