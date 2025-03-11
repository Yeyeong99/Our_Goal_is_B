N = int(input())
fst_person, snd_person = map(int, input().split())

M = int(input())
family = {}
for m in range(M):
    x, y = map(int, input().split())
    if x not in family.keys():
        family[x] = []
    if y not in family.keys():
        family[y] = []
    family[x].append(y)
    family[y].append(x)

answer = -1
stack = [fst_person]
cnt = 0
visited = [0] * (N + 1)
while stack:
    current = stack.pop()
    if current == snd_person:
        visited[current] = 1
        break
    if snd_person in family[current]:
        visited[current] = 1
        visited[snd_person] = 1
        cnt += 1
        break
    elif family[current] and not visited[current]:
        visited[current] = 1
        stack += family[current][::-1]
        cnt += 1

if visited[snd_person]:
    print(cnt)
else:
    print(answer)