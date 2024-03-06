txt = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc"

def getNextPeriodPos(txt, startPos):
    period = txt.find(".", startPos)
    if period != -1:
        return period
    return -1

def getNextLine(txt, startPos):
    period = getNextPeriodPos(txt, startPos)
    if period != -1:
        return txt[startPos:period+1].strip()
    return txt[startPos:].strip()
    
def countWordsInLine(line):
    a = line.count(" ")
    b = line.count("\n")
    c = line.count("\t")
    return a+b+c+1

def countPunctuationsInLine(line):
    a = line.count(".")
    b = line.count('""')
    c = line.count("''")
    d = line.count("?")
    e = line.count("!")
    f = line.count(",")
    g = line.count(":")
    h = line.count(";")
    return a+b+c+d+e+f+g+h

def main(txt):
    first = getNextPeriodPos(txt, 0)
    firstline = getNextLine(txt, 0)
    print("1:", firstline)
    print("Num of Words in Line #1:", countWordsInLine(firstline.strip()))
    print("Num of Punctations in Line #1:", countPunctuationsInLine(firstline.strip())) 

    second = getNextPeriodPos(txt, first+1)
    secondline = getNextLine(txt, first+1)
    print("2:", secondline)
    print("Num of Words in Line #2:", countWordsInLine(secondline.strip()))
    print("Num of Punctations in Line #2:", countPunctuationsInLine(secondline.strip())) 

    third = getNextPeriodPos(txt, second+1)
    thirdline = getNextLine(txt, second+1)
    print("3:", thirdline)
    print("Num of Words in Line #3:", countWordsInLine(thirdline.strip()))
    print("Num of Punctations in Line #3:", countPunctuationsInLine(thirdline.strip()))

    forth = getNextPeriodPos(txt, third+1)
    forthline = getNextLine(txt, third+1)
    print("4:", forthline)
    print("Num of Words in Line #4:", countWordsInLine(forthline.strip()))
    print("Num of Punctations in Line #4:", countPunctuationsInLine(forthline.strip()))

    fifth = getNextPeriodPos(txt, forth+1)
    fifthline = getNextLine(txt, forth+1)
    print("5:", fifthline)
    print("Num of Words in Line #5:", countWordsInLine(fifthline.strip()))
    print("Num of Punctations in Line #5:", countPunctuationsInLine(fifthline.strip()))
    

main(txt)

#구현 실패 50분 소요, 구현 성공 1시간 5분 소요