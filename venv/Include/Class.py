def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a

print("Podaj dwie liczby")
a=input()
b=input()
a=int(a)
b=int(b)
print("gcd(",a,", ",b,") # =>",gcd(a,b))