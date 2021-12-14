def fib(n):
  """la fonction vous donne le n ième terme de la suite de Fibonacci"""
  if n<=2:
    return 1
  return fib(n-1)+fib(n-2)

t=fib(5)

print(t)