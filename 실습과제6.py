num = int(input("2~100 사이 정수를 입력하세요:"))

def inputdivisor(n):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
    return lst

def twohundred(n):
    list2 = [None, None]
    for j in range(2, n + 1):
        lst = []
        for i in range(1, j + 1):
            if j % i == 0:
                lst.append(i)
        list2.append(lst)
    return list2

def main(n):
    print(inputdivisor(n))
    print(twohundred(200))

main(num)
