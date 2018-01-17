
n = int(input())  # the number of relationships of influence
tree = {}
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]
    if x not in tree:  # creating new key in the dict
        tree[x]=[y]
    else:
        tree[x].append(y)  # adding node to existing key

# Write an action using print

def check(key):
    if key not in tree :
        return 1
    else:  # if key is in the tree add result to list for item
        g=[]
        for item in tree[key]:
            g.append(check(item))
        return 1 + max(g)

lista = []
for key in tree:
    lista.append(check(key))
result = max(lista)
# The number of people involved in the longest succession of influences
print(result)