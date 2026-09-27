V = int(input())
tree = list(map(int, input().split()))

L = [0] * (V + 1)
R = [0] * (V + 1)

for i in range(V - 1):
    p = tree[i * 2]
    c = tree[i * 2 + 1]

    if L[p] == 0:
        L[p] = c
    else:
        R[p] = c

def preorder(s):
    if s:
        print(s, end = ' ')
        preorder(L[s])
        preorder(R[s])

def inorder(s):
    if s:
        inorder(L[s])
        print(s, end = ' ')
        inorder(R[s])

def postorder(s):
    if s:
        postorder(L[s])
        postorder(R[s])
        print(s, end = ' ')

preorder(1)
print()
inorder(1)
print()
postorder(1)
print()