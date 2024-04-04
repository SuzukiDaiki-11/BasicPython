a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
# (1)
a = 10
b = 20

while True:
    if a % b == 0:
        break
    a ,b = b, a%b

print('最大公約数は', b,'です。')

# (2)
a = 14
b = 91

while True:
    if a % b == 0:
        break
    a ,b = b, a%b

print('最大公約数は', b,'です。')

# (3)
a = 91
b = 14

while True:
    if a % b == 0:
        break
    a ,b = b, a%b

print('最大公約数は', b,'です。')