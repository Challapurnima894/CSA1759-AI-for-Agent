def ab(d,a,b,m):
    if d==0: return 1
    for _ in range(2):
        if m: a=max(a,ab(d-1,a,b,0))
        else: b=min(b,ab(d-1,a,b,1))
        if a>=b: break
    return a if m else b
print(ab(3,-9,9,1))
