#1
"""
def calculate(t, h):
    di = (0.81*t) + (0.01 * h *(0.99*t - 14.3)) + 46.3
    return di

temp = int(input("온도를 입력해주세요:"))
humid = int(input("습도를 입력해주세요:"))
calculate(temp, humid)
if calculate(temp, humid) < 70:
    print("불쾌 지수는 쾌적함입니다.")
elif 70 <= calculate(temp, humid) < 80:
    print("불쾌 지수는 일부 사람들이 불쾌감을 느낄 수 있음입니다.")
elif 80 <= calculate(temp, humid) <= 83:
    print("불쾌 지수는 50%의 사람들이 불쾌감을 느낌입니다.")
elif 83 < calculate(temp, humid):
    print("불쾌 지수는 대부분의 사람들이 불쾌감을 느낌입니다.")
    """

#2
def addword(word):
    sen = word.strip()
    first = sen.find(" ")
    firstword = sen[:first].strip()
    secsen = sen[first+1:].strip()
    second = secsen.find(" ")
    secword = secsen[:second].strip()
    thirdsen = secsen[second+1:].strip()
    third = thirdsen.find(" ")
    thirdword = thirdsen[:third].strip()
    print(firstword + " " + thirdword)
    if first == -1:
        print("최소한 두 개 이상의 단어로 구성된 문자열을 입력해야 한다")
    if second == -1:
        print(firstword)
                    
addword("hello everyone   it’s a nice day ")
#1번 구현 성공, 2번 실패 54분 25초 소요 + 추가시간 1시간 12분 구현 성공