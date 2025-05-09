Num = int(input("Digite um número inteiro: "))

if (Num % 2) == 0:
    if Num > 0:
        print(f"O número {Num} é positivo e par")
    else:
        print(f"O número {Num} é negativo e par")

else:
    if Num > 0:
        print(f"O número {Num} é positivo e impar")
    else:
        print(f"O número {Num} é negativo e impar")
