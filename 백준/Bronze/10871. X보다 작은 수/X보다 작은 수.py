N , X = map(int,input().split())
A = list(input().split())
for i in range(N):
    if X > int(A[i]) :
        print( A[i], end = " ")