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
