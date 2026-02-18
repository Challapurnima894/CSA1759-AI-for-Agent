states=['A','B','C']
neighbors={'A':['B'],'B':['A','C'],'C':['B']}
colors=['R','G']

def solve(a={}):
    if len(a)==3: return a
    s=[x for x in states if x not in a][0]
    for c in colors:
        if all(a.get(n)!=c for n in neighbors[s]):
            a[s]=c
            r=solve(a)
            if r: return r
            del a[s]
print(solve())
