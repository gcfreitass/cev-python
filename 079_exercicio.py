# Exercicio 079
# 
# Crie um programa onde o usuário possa digitar vários valores numériocs e 
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados em
# em ordem crescente.

num_list = []

while True:
    num = float(input("Digite um número: "))

    if num not in num_list:
        num_list.append(num)

    answer = input("Deseja encerrar o programa [S/N]? ")

    if answer.lower() == "s":
        break
print("=-" * 30)

print(f"Você digitou:\n{num_list}")
