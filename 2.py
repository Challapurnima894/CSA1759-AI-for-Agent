N = 8

def safe(b,r,c):
    for i in range(r):
        if b[i][c] or (c-r+i>=0 and b[i][c-r+i]) or (c+r-i<N and b[i][c+r-i]):
            return False
    return True

def solve(b,r):
    if r==N:
        for x in b: print(*x)
        return True
    for c in range(N):
        if safe(b,r,c):
            b[r][c]=1
            if solve(b,r+1): return True
            b[r][c]=0
    return False

board=[[0]*N for _ in range(N)]
solve(board,0)
