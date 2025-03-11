N = int(input())
fst_person, snd_person = map(int, input().split())
if fst_person > snd_person:
    fst_person, snd_person = snd_person, fst_person

M = int(input())
family = {}
for m in range(M):
    x, y = map(int, input().split())
    if not family[x]:
        family[x] = []
    family[x].append(y)
    family[y].append(x)

answer = -1
stack = [fst_person]
cnt = 0
while stack:
    current = stack.pop()
    cnt += 1
