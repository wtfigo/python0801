import datetime

x = [1984, 1982, 1990, 1985, 1976, 1991]
i = 0
j = len(x)
now = datetime.datetime.now()
while i < j:
    k = x[i]
    print(now.year - k)
    i += 1