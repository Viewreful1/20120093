import sys
rl = lambda: sys.stdin.readline()
#sys.stdin = open('sample.txt', 'r')

def d(cur, A, VST):
    print(cur, end=' ')
    VST[cur] = True
    for nxt, exist in enumerate(A[cur]):
        if exist and VST[nxt] is False:
            d(nxt, A, VST)

def b(cur, A, VST):    
    Q = []
    VST[cur] = True
    Q.append(cur)
    while Q:
        cur = Q[0]; Q.pop(0)
        print(cur, end=' ')
        for nxt, exist in enumerate(A[cur]):
            if exist and VST[nxt] is False:
                VST[nxt] = True
                Q.append(nxt)                

V, E, S = list(map(lambda x: int(x), rl().split()))
A = [[False for i in range(1000 + 1)] for j in range(1000 + 1)]
for n in range(E):
    s, e = map(lambda x: int(x), rl().split())
    A[s][e], A[e][s] = True, True    
    
VST = [False for i in range(1000 + 1)]
d(S, A, VST); print()
VST = [False for i in range(1000 + 1)]
b(S, A, VST)