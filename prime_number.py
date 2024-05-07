n = input("nの値を入力: ")


# TODO
n = int(n)

try:
    n = int(n)
except ValueError:
    print("整数を入力してください。")
    exit()

def is_prime(n):
    
    if n <= 0:
        raise ValueError("自然数を入力してください。")
    if n < 2 :
        return False
    for i in range(2,n):
        if (n % i == 0):
            return False
    else:
        return True

if is_prime(n):
    print(f"{n} は素数です。")
else:
    print(f"{n} は素数ではありません。")
