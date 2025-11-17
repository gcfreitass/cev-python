# Desafio 078
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
# qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

num_list = []

for n in range(0, 5):
    number_input = num_list.append(float(input(f"Digite o {n+1}º número: ")))

print("=-" * 30)
print(f"Você digitou os valores {num_list}")

num_list_max_value = max(num_list)
num_list_min_value = min(num_list)

print(f"O maior valor digitado foi {num_list_max_value} nas posições ", end="")
print(*[i+1 for i, v in enumerate(num_list) if num_list[i] == num_list_max_value], sep="...", end="")

print()

print(f"O menor valor digitado foi {num_list_min_value} nas posições ", end="")
print(*[i+1 for i, v in enumerate(num_list) if num_list[i] == num_list_min_value], sep="...", end="")
