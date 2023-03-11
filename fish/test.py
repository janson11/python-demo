

s = input()
l = s.split(",")
l.sort()
s = ','.join(l)[::-1].split(",")
s = "".join(s)
print(s)

