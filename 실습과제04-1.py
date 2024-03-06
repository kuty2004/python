def calcluate_fee(membership, parkingTime, purchased):
    if membership == "플래티넘" or membership == "골드":
        if parkingTime > 120:
            return (parkingTime -120) // 10 * 1000
        else:
            return 0
    elif membership == "실버" or membership == "프렌즈":
        if purchased >= 30000:
            if parkingTime >120:
                return (parkingTime -120) // 10 * 1000
            else: 
                return 0
        elif purchased >= 10000:
            if parkingTime > 60:
                return (parkingTime - 60) // 10 * 1000
            else:
                return 0
        else:
            return parkingTime // 10 * 1000 
    elif membership == "비회원":
        if purchased >= 50000:
            if parkingTime > 120:
                return (parkingTime - 120) // 10 * 1000
            else:
                return 0
        elif purchased >= 30000:
            if parkingTime > 60:
                return (parkingTime - 60) // 10 * 1000
            else:
                return 0 
        else:
            return parkingTime // 10 * 1000

membership = input("회원 등급 입력: ")
parkingTime = int(input("주차 시간 입력: "))
if membership == "실버" or membership ==  "프렌즈" or membership == "비회원":
    purchased = int(input("구매 금액 입력: "))
else:
    purchased = None
fee = calcluate_fee(membership, parkingTime, purchased)
print(f"주차 요금: {fee}원")