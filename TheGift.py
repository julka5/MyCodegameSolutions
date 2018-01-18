n = int(input())  # number of participants
c = int(input())  # price of the gift
budgets = []  # the list of budgets of participants
for i in range(n):
    b = int(input())
    budgets.append(b)

budgets.sort()
average = c//len(budgets)
if sum(budgets) >= c:
    for i in range(n-1):
        if budgets[0] <= average:
            k = budgets[0]
        else:
            k = average
        budgets.pop(0)
        c -= k
        average = c//len(budgets)
        print(k)
    print(c)
else: print("IMPOSSIBLE")