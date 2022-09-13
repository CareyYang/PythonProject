# s = {i for i in range(1500, 2700) if i % 7 == 5}
# print(s)

pv1, pv2, pt, ps, pl = (input("请输入：").split())
v1 = int(pv1)
v2 = int(pv2)
t = int(pt)
s = int(ps)
l = int(pl)
s1 = 0
s2 = 0
rt = 0
w = 0
while s1 < l and s2 < l:
    if s1 - s2 >= t:
        w = s
    if w != 0:
        s1 += 0
        w -= 1
    else:
        s1 += v1
    s2 += v2
    rt += 1

if s1 >= l > s2:
    print("R")
elif s2 >= l > s1:
    print("T")
else:
    print("D")
print(rt)
