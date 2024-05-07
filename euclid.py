a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
a = int(a)
b = int(b)

import random
import math

def euclidean_algorithm(a, b):
    while b:
        a, b = b, a % b
    return a

def are_coprime(a, b):
    gcd = euclidean_algorithm(a, b)
    return gcd == 1

print(f"最大公約数は{a}")

if are_coprime(a, b):
    print(f"{a} と {b} は互いに素です。")
else:
    print(f"{a} と {b} は互いに素ではありません。")
