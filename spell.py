def spell(n):
    if n==1:
        return "one"
    elif n==2:
        return "two"
    elif n==3:
        return "three"
    elif n==4:
        return "four"
    elif n==5:
        return "five"
    elif n==6:
        return "six"
    elif n==7:
        return "seven"
    elif n==8:
        return "eight"
    elif n==9:
        return "nine"
    elif n==10:
        return "ten"
    elif n==11:
        return "eleven"
    elif n==12:
        return "twelve"
    elif n==13:
        return "thirteen"
    elif n==14:
        return "fourteen"
    elif n==15:
        return "fifteen"
    elif 15 < n < 20:
        return number(n%10)+"teen"
    elif n==20:
        return "twenty"
    elif n==30:
        return "thirty"
    elif n==40:
        return "forty"
    elif n==50:
        return "fifty"
    elif 20 <=n and n%10==0 and n<100:
        return number(n//10)+"ty"
    elif 20 < n < 100:
        return number(n//10*10)+"-"+number(n%10)
    else:
        return f"Not yet implemented: number({n:d})"

