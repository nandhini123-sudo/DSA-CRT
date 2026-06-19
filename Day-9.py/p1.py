#product of all numbers
def product_n(n):
    if n<=1:
        return 1
    return n*product_n(n-1)
print(product_n(50))
