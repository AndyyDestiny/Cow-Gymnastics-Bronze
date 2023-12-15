a = [eval(i) for i in input().split(" ")]
scores = []
tests = a[0]
cows = a[1]
for i in range(tests):
    scores.append([eval(i) for i in input().split(" ")])

pairs = 0
for i in range(cows):
    better_than = []
    for n in range(tests):
        index = scores[n].index(i + 1)
        for z in range(cows):
            if z > index:
                better_than.append(scores[n][z])
    for k in range(cows):
        times = 0
        for num in better_than:
            if num == k + 1:
                times += 1
        if times == tests:
            pairs += 1

print(pairs)

