def F(n):
    if n > 0:
        F(n // 4)
        print(n)
        F (n - 1)
print(F(5))