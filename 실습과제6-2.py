t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sagittis nisi at dapibus semper. Ut quis sapien vulputate, pharetra sapien vel, commodo diam. Nam tincidunt nulla sit amet neque iaculis, at interdum erat ultrices. Donec nec turpis sagittis, malesuada dui ut, pellentesque magna. Integer ultricies pharetra ex ut semper. Pellentesque ex orci, rhoncus vitae dolor in, vulputate volutpat felis. Fusce quis ornare purus."
txt = t.lower()

def findChar(cList, ch):
    count = txt.count(ch)
    if count == 0:
        cList.append([ch, None])
    else:
        cList.append([ch, count])

def countChars(txt):
    lst = []
    for i in range(ord(" "), ord("z")+1):
        findChar(lst, chr(i))
    return lst

def printList(cList):
    for ch in cList:
        print(ch)

def main():
    cList = countChars(txt)
    printList(cList)

main()
