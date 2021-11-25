# Fibonacci Sequence (Harder) in 133 characters: try to beat me!
# https://dmoj.ca/problem/fibonacci2

def f(n):
 if n:a,b=f(n/2);c=a*(b+b-a)%g;d=(a*a+b*b)%g;k=n%2;return c+d*k-c*k,c*k+d
 return 0,1
g=10**9+7;print f(input()%(2*g+2))[0]
