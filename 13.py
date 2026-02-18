def minimax(d,m):
    if d==0: return 1
    return max(minimax(d-1,0),minimax(d-1,0)) if m else \
           min(minimax(d-1,1),minimax(d-1,1))
print(minimax(3,1))
