def getNextPeriodPos(txt, startPos):
    period = txt.find('.',startPos)
    if period != -1:
        print(period)
        return period
    else:
        return -1

def getNextLine(txt, startPos):
    nextperiod = getNextPeriodPos(txt, startPos)
    if nextperiod != -1:
        print(txt[startPos:nextperiod+1])
        return getNextLine(txt, nextperiod+1)
    else:
        return 

txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sagittis nisi at dapibus semper. Ut quis sapien vulputate, pharetra sapien vel, commodo diam. Nam tincidunt nulla sit amet neque iaculis, at interdum erat ultrices. Donec nec turpis sagittis, malesuada dui ut, pellentesque magna. Integer ultricies pharetra ex ut semper. Pellentesque ex orci, rhoncus vitae dolor in, vulputate volutpat felis. Fusce quis ornare purus."

getNextPeriodPos(txt, 0)
getNextLine(txt, 0)