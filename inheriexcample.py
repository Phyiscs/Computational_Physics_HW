
A=-1/3
B=1/5
for n in range(1,100000):
    A=float(A-1/(3+4*n))
    B=float(B+1/(5+4*n))

PI=float(4*(1+A+B))
print(PI)
