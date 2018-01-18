n = int(input())
val = []
for i in input().split():
    v = int(i)
    val.append(v)

max = 0
max_val = 0
min_val = 0

for i in val:
    if i > max_val:
        if max_val - min_val > max:
            max = max_val - min_val
        max_val = i
        min_val = i

    elif i < min_val:
        min_val = i
        if max_val - min_val > max:
            max = max_val - min_val

print(-max)