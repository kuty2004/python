def find(s, ss, pos):
    period = []
    while True:
        nextpos = s.find(ss, pos)
        if nextpos == -1:
            break
        pos = nextpos + 1
        period.append(nextpos)
    return period

def getNextPeriodPos(txt, startPos):
    return find(txt, ".", startPos)

def getNextLine(txt, startPos):
    if startPos >= len(txt):
        return None
    idx_list = getNextPeriodPos(txt, startPos)
    if idx_list == []: 
        return txt[startPos:]
    else:
        idx = idx_list[0]
        line = txt[startPos:idx + 1].strip()
        print(line)
        getNextLine(txt, idx + 1)

def main(txt, startPos):
    print(getNextPeriodPos(txt, startPos))
    print(getNextLine(txt, startPos))

t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sagittis nisi at dapibus semper. Ut quis sapien vulputate, pharetra sapien vel, commodo diam. Nam tincidunt nulla sit amet neque iaculis, at interdum erat ultrices. Donec nec turpis sagittis, malesuada dui ut, pellentesque magna. Integer ultricies pharetra ex ut semper. Pellentesque ex orci, rhoncus vitae dolor in, vulputate volutpat felis. Fusce quis ornare purus."
main(t, 0)
