# 202310985 채예원 kuty1004

# 1번 함수
def verifyLength(num):
    if len(num) == 9 or len(num) == 8:
        return True
    else:
        print("verifyLength 오류:번호 길이가 너무 길거나 짧음")
        return False
        


# 1번 테스트 코드
"""print("\n1. verifyLength\n")
print(verifyLength("100가 11111"))  # 오류 출력 후 False
print(verifyLength("1가  1111"))    # True
print(verifyLength("00가 1111"))    # True
print(verifyLength("000가 1111"))   # True
print(verifyLength("100 가1111"))   # True
print(verifyLength("10가111"))      # 오류 출력 후 False 
print(verifyLength("10 가1111"))    # True 
print(verifyLength("1001가1111"))   # True """

# 2번 함수 
def verifyHangul(num):
    eng = "ABCDEFGHIJKlMNOP"
    if num[2].isalpha() == True:
        if num[2].upper() in eng == True:
            return False
        else:
            return True
    elif num[3].isalpha() == True:
        if num[3].upper() in eng == True:
            return False
        else:
            return True
    else:
        print("verifyHangul 오류: 한글 위치가 적절치 않음")
        return False

# 2번 테스트 코드
"""print("\2. verifyHangul\n")
print(verifyHangul("100가 11111")) # True
print(verifyHangul("1가  1111"))   # 오류 출력 후 False 
print(verifyHangul("00가 1111"))   # True 
print(verifyHangul("000가 1111"))  # True 
print(verifyHangul("100 가1111"))  # 오류 출력 후 False 
print(verifyHangul("10가111"))     # True
print(verifyHangul("10 가1111"))   # True
print(verifyHangul("1001가1111"))  # 오류 출력 후 False """

# 3번 함수
def verifySpace(num):
    if num[3] == " ":
        return True
    elif num[4] == " ":
        return True
    else:
        print("verifySpace 오류: 공백 문자의 위치가 적절치 않음")
        return False


# 3번 테스트 코드
"""print("\n3. verifySpace\n")
print(verifySpace("100가 11111"))  # True
print(verifySpace("1가  1111"))    # True
print(verifySpace("00가 1111"))    # True
print(verifySpace("000가 1111"))   # True
print(verifySpace("100 가1111"))   # True
print(verifySpace("10가111"))      # 오류 출력 후 False 
print(verifySpace("10 가1111"))    # 오류 출력 후 False 
print(verifySpace("1001가1111"))   # 오류 출력 후 False """

# 4번 함수
def verifyLastNum(num):
    if num[len(num)-4:].isnumeric() == True:
        if 100 <= int(num[len(num)-4:]) <= 9999:
            return True
        else:
            print("verifyLastNum 오류: 뒷 번호가 100 미만임")
            return False
    else:
        print("verifyLastNum 오류: 뒷 번호가 숫자가 아님")
        return False


# 4번 테스트 코드
"""print("\4. verifyLastNum\n")
print(verifyLastNum("100가 11111"))  # True
print(verifyLastNum("1가  1111"))    # True 
print(verifyLastNum("00가 1111"))    # True 
print(verifyLastNum("000가 1111"))   # True 
print(verifyLastNum("100 가1111"))   # True 
print(verifyLastNum("10가111"))      # 오류 출력 후 False 출력
print(verifyLastNum("10 가1111"))    # True 
print(verifyLastNum("1001가1111"))   # True """

# 5번 함수
def verifyNum3(num):
    if num[:3].isnumeric() == True:
        if 100 <= int(num[:3]) <= 999:
            return 1
        else:
            print("verifyNum3 오류: 앞 번호 숫자가 100 미만임")
            return -1
    else:
        return 0


# 5번 테스트 코드
"""print("\5. verifyNum3\n")
print(verifyNum3("100가 11111"))   # 1
print(verifyNum3("1가  1111"))     # 0
print(verifyNum3("00가 1111"))     # 0
print(verifyNum3("000가 1111"))    # 오류 출력 후 -1 
print(verifyNum3("100 가1111"))    # 1
print(verifyNum3("10가111"))       # 0
print(verifyNum3("10 가1111"))     # 0
print(verifyNum3("1001가1111"))    # 1"""

# 6번 함수
def verifyNum2(num):
    if num[:2].isnumeric() == True:
        if 1 <= int(num[:2]) <= 99:
            return 1
        else:
            print("verifyNum2 오류: 앞 번호 숫자가 1 미만임")
            return -1
    else:
        return 0


# 6번 테스트 코드
"""print("\6. verifyNum2\n")
print(verifyNum2("100가 11111"))    # 1
print(verifyNum2("1가  1111"))      # 0
print(verifyNum2("00가 1111"))      # 오류 출력 후 -1 
print(verifyNum2("000가 1111"))     # 오류 출력 후 -1 
print(verifyNum2("100 가1111"))     # 1
print(verifyNum2("10가111"))        # 1
print(verifyNum2("10 가1111"))      # 1
print(verifyNum2("1001가1111"))     # 1"""

# 7번 함수
def verifyFirstNum(num):
    if verifyNum3(num) == 1 or verifyNum2(num) == 1:
        return True
    elif verifyNum3(num) == 0 or verifyNum2(num) == 0:
        print("verifyNum 오류: 앞 번호가 숫자가 아님")
        return False
    elif verifyNum3(num) == -1:
        return False
    elif verifyNum2(num) == -1:
        return False


# 7번 테스트 코드
"""print("\n7. verifyFirstNum\n")
print(verifyFirstNum("100가 11111"))     # True
print(verifyFirstNum("1가  1111"))       # 오류 출력 후 False
print(verifyFirstNum("00가 1111"))       # False
print(verifyFirstNum("000가 1111"))      # False
print(verifyFirstNum("100 가1111"))      # True
print(verifyFirstNum("10가111"))         # True 
print(verifyFirstNum("10 가1111"))       # True 
print(verifyFirstNum("1001가1111"))      # True """

# 8번 함수
def verifyLicensePlate(num):
    if verifyLength(num) == True:
        if verifyHangul(num) == True:
            if verifySpace(num) == True:
                if verifyLastNum(num) == True:
                    if verifyFirstNum(num) == True:
                        return True
                    else:
                        return False
                else:
                    return False

            else:
                return False
        else:
            return False
    else:
        return False


# 8번 테스트 코드
print("\n8. verifyLicensePlate\n")
print(verifyLicensePlate("100가 11111"))     # 글자 개수 오류, False 
print(verifyLicensePlate("1가  1111"))       # 앞 번호 숫자 갯수가 맞지 않음, False
print(verifyLicensePlate("00가 1111"))       # 앞 번호 숫자 1 미만, False 
print(verifyLicensePlate("000가 1111"))      # 앞 번호 숫자 100 미만, False 
print(verifyLicensePlate("100 가1111"))      # 한글 위치 오류, False 
print(verifyLicensePlate("100가1111 "))      # 공백 위치 오류, False 
print(verifyLicensePlate("100가 0011"))      # 뒷 번호 100 미만 오류, False
print(verifyLicensePlate("01가 1111"))       # True
print(verifyLicensePlate("200가 1111"))      # True 