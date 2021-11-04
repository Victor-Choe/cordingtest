#로마 숫자 계산식.

# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

#조건. 로마숫자는 왼쪽에서 오른쪽으로 큰수에서 작은수를 써서 구성하며 그 예로  12는 XII,  27 XXVII 이런식으로 표현된다.
#예외. 숫자 4 같은경우 IIII 가 아닌 IV 의 형식으로 표현하며 , 큰 수가 오른쪽에 오는경우는 뺏셈을 의미

# 입력값 예제

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Input: s = "IX"
# Output: 9
# Input: s = "IV"
# Output: 4

def romanToInt(s):
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    #previous 에 첫 문자를 기본값으로 넣어주지 않으면 IV 같은경우 previous 가 0 이라 계산이 되지 않기에 previous 에 첫 문자값s[0] 을 대입 
    empty=s[0]
    previous=romans[empty]
#들어오는 값들을 미리 딕셔너리로 구현,return 할 total 변수 생성
#이때 예외의 경우는 기존값보다 다음값이 큰 경우 이므로 기존값을 나타내는 previouse 변수 생성

#total 변수에는 입력값들을 계속 적립시키고 만약 기존값보다 큰 숫자가 나오는경우 기존에 더해즌 previous 까지 고려하여 뺀 후 토탈에 더함.
    for i in s.reverse():
        if romans[i]>previous:
            total+=romans[i]-2*previous
        else: 
            previous=romans[i]
            total+=romans[i]
    return total

# leet code 최종 코드
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         total = 0
#         empty=s[0]
#         previous=romans[empty]
#         for i in s:
#             if romans[i]>previous:
#                 total+=romans[i]-2*previous 
#             else:
#                 previous=romans[i]
#                 total+=romans[i]
#         return total

#다른사람이 푼 좋은 방법 : 4랑 9, 40,90,400,900 을 미리 치환하여 예외처리함.

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         translations = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         number = 0
#         s = s.replace("IV", "IIII").replace("IX", "VIIII")
#         s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#         s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#         for char in s:
#             number += translations[char]
#         return number

#초기값 대신 역순으로 푸는 방법

# def romanToInt(self, s: str) -> int:
# 	res, prev = 0, 0
# 	dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
# 	for i in s[::-1]:          # rev the s
# 		if dict[i] >= prev:
# 			res += dict[i]     # sum the value iff previous value same or more
# 		else:
# 			res -= dict[i]     # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc 
# 		prev = dict[i]
# 	return res