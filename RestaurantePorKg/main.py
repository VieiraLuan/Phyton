

print("Quilão do João")
peso_prato = float(input("Insira o peso do prato: "))
valor_por_kg = float(input("Insira o valor do kg"))
valor_a_pagar = peso_prato * valor_por_kg


if peso_prato >= 1:
    print("peso do prato maior que um o cliente irá pagar apenas R$ 80,00")

print(f"O valor do prato é de R$ {valor_a_pagar:.2f}")
