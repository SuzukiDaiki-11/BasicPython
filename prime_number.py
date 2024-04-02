a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
            break

# (1)
number1 = 61
if is_prime(number1):
    print(f"{number1}は素数です。")
else:
    print(f"{number1}は素数ではありません。")

# (2)    
number2 = 10
if is_prime(number2):
    print(f"{number2}は素数です。")
else:
    print(f"{number2}は素数ではありません。")