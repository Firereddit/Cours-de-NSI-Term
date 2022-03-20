def fibo(n):
    """fonction donnant le n-ième terme de la suite de fibonacci"""
    a=0
    b=1

    print("Le", n, "ième terme de la suite de Fibonacci est:")

    for i in range(0, n):
        c= a + b
        a=b
        b=c
    print(c)

