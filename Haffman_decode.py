a = input().split()
x, y = int(a[0]), int(a[1])
dichaff, vivod = {}, []
for i in range(x):
    b = list(input().split())
    dichaff[b[1]] = b[0].replace(':','')
    if len(dichaff[b[1]]) == 0:
        dichaff[b[1]] = ' '
c = input()
x = 1
while len(c) != 0:
    d = str(c[0:x:])
    if d in dichaff.keys():
        vivod.append(dichaff[d])
        c = c[x:]
        x = 0
    x += 1
vivod = ''.join(vivod)
print(vivod)