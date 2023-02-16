def alarm(h,m):
    if m < 40:
        h -= 1
        m += 60
        m -= 40
    elif m >= 40:
        m -= 40
    if h < 0:
        h += 24
    if h > 23 and m > 59:
        print("Invalid Number")
    print("OUTPUT",h, m)
hours = int(input("HOURS>"))
mins = int(input("MINUTES>"))
alarm(hours,mins)
