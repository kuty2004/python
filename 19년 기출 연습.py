#1
"""
dustaverage = (29+21+18+34+67+79+18)/7
smalldustaverage = (44+44+32+60+84+112+41)/7
if 0 < dustaverage <= 15:
    print(f"미세먼지 현황 평균은 {dustaverage}이고, 좋음 등급입니다.")
elif 15 < dustaverage <= 35:
    print(f"미세먼지 현황 평균은 {dustaverage}이고, 보통 등급입니다.")
elif 35 < dustaverage <= 75:
    print(f"미세먼지 현황 평균은 {dustaverage}이고, 나쁨 등급입니다.")
elif dustaverage > 75:
    print(f"미세먼지 현황 평균은 {dustaverage}이고, 매우 보통 등급입니다.")

if 0 < smalldustaverage <= 30:
    print(f"초미세먼지 현황 평균은 {smalldustaverage}이고, 좋음 등급입니다.")
elif 30 < smalldustaverage <= 80:
    print(f"초미세먼지 현황 평균은 {smalldustaverage}이고, 보통 등급입니다.")
elif 80 < smalldustaverage <= 100:
    print(f"초미세먼지 현황 평균은 {smalldustaverage}이고, 나쁨 등급입니다.")
elif smalldustaverage > 100:
    print(f"초미세먼지 현황 평균은 {smalldustaverage}이고, 매우 보통 등급입니다.")
"""

#2
"""
age = int(input("실제 나이를 입력해주세요:"))
time = int(input("유지 시간을 입력해주세요:"))

if time < 5:
    print(f"당신의 나이는 {age - (age%10)}대이지만, 균형 나이는 80대 이상입니다. ")
elif 5 <= time < 10:
    print(f"당신의 나이는 {age - (age%10)}대이지만, 균형 나이는 70대입니다. ")
elif 10 <= time < 35:
    print(f"당신의 나이는 {age - (age%10)}대이지만, 균형 나이는 60대입니다. ")
elif 35 <= time < 50:
    print(f"당신의 나이는 {age - (age%10)}대이지만, 균형 나이는 50대입니다. ")
elif 50 <= time < 75:
    print(f"당신의 나이는 {age - (age%10)}대이지만, 균형 나이는 40대입니다. ")
elif 75 <= time < 80:
    print(f"당신의 나이는 {age - (age%10)}대이지만, 균형 나이는 30대입니다. ")
elif 80 <= time:
    print(f"당신의 나이는 {age - (age%10)}대이지만, 균형 나이는 20대입니다. ")
"""
#3
def secondword(word, first, second):
    if " " in word == False:
        return ""
    else:
        l = word.count(" ")
        fir = word.find(" ", first)
        sec = word.rfind(" ",0, second)
        if sec == fir:
            print(word[fir:].strip(),",",len(word[fir:].strip()))
            if word[fir:].strip() == " ":
                print("빈 문자열이 반환되었습니다")
        elif fir < sec:
            if word[fir:sec+1].isalpha() == False:
                if word[fir:sec+1] == "  ":
                    print(word[fir:].strip(),",",len(word[fir:].strip()))
                    if word[fir:].strip() == " ":
                        print(word[fir:].strip(),",",len(word[fir:].strip()))
                else:
                    secondword(word, first+1, second-1)
            else:
                print(word[fir:sec+1].strip(),",",len(word[fir:].strip()))
                if word[fir:sec+1].strip() == " ":
                        print("빈 문자열이 반환되었습니다")
                    
                
            
secondword("hello world",0,len("hello world"))
secondword("hello  world",0,len("hello  world"))
secondword("hello    world    ",0,len("hello    world    "))

#1,2번 구현, 3번 구현 실패(시간부족)-51분 소요 추가 시간 사용 40분? 구현 성공
