a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
a = int(a)
b = int(b)

def euclid(a, b):
    if a < b:
        a, b = b, a
    else:
        a, b = a, b
    
    while b != 0:
        a, b =b, a % b
    return a, b

a, _ = euclid(a,b)

print(f"最大公約数は{a}")