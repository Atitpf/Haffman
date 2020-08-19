from collections import Counter

text = list(input())
newtext = [(col, sim) for sim, col in Counter(text).items()]
code, vivod, dichaff, df = [], [], [], {}
newtext.sort()

if len(newtext) == 1:
    dichaff.append((newtext[0][1], 0))
while len(newtext) > 1:
    a = newtext[0][0] + newtext[1][0]
    b = newtext[0][1] + newtext[1][1]
    newtext.append((a, b))
    dichaff.append((newtext[0][1], 0))
    dichaff.append((newtext[1][1], 1))
    del newtext[0]
    del newtext[0]
    newtext.sort()

for i in dichaff:
    if len(i[0]) == 1:
        code.append((i[0]))
for i in code:
    for a in dichaff:
        if i in str(a[0]):
            if i not in df.keys():
                df[i] = []
                df[i].append(str(a[1]))
            else:
                df[i].append(str(a[1]))
for key, value in df.items():
    value.reverse()
    value = ''.join(value)
    df[key] = value
for i in text:
    if i in df.keys():
        a = df[i]
        vivod.append(a)
vivod = ''.join(vivod)

print(len(code), len(vivod))
for key, value in df.items():
    print(key + ':' + ' ' + value)
print(vivod)