b=[" "]*9
for i in range(9):
    print(b[0:3],b[3:6],b[6:9])
    m=int(input())
    b[m]="X" if i%2==0 else "O"
