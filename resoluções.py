# Questão Número 1 (valor de SOMA)
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K
print(f"O valor da soma da questão 1 é: {SOMA}.")

# Questão Número 2 (Fibonacci)
print(f"Questão número 2:")
def fibonacci(valor):
    a, b = 0, 1
    while b <= valor:
        if b == valor:
            return True
        a, b = b, a + b
    return False

valor = int(input("Informe um número: "))
if fibonacci(valor):
    print(f"O número {valor} pertence à sequência de Fibonacci.")
else:
    print(f"O número {valor} NÃO pertence à sequência de Fibonacci.")

# Questão Número 3 (Faturamento Diário)
print(f"Questão número 3:")
import json

dados = '''
[
    {"dia": 1, "valor": 1000.0},
    {"dia": 2, "valor": 0.0},
    {"dia": 3, "valor": 500.0},
    {"dia": 4, "valor": 2000.0}
]
'''
faturamento_d = json.loads(dados)

valores = [dia["valor"] for dia in faturamento_d if dia["valor"] > 0]

menor_valor = min(valores)
maior_valor = max(valores)
media = sum(valores) / len(valores)
faturamento_superior = sum(1 for valor in valores if valor > media)

print(f"Menor valor: R${menor_valor:.2f}")
print(f"Maior valor: R${maior_valor:.2f}")
print(f"Dias acima da média: {faturamento_superior}")

# Questão Número 4 (Faturamento Mensal)
faturamento_mensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento_mensal.values())

print("Percentual de representação por estado:")
for estado, valor in faturamento_mensal.items():
    percentual = (valor / total) * 100
    print(f"{estado}: {percentual:.2f}%")

# Questão Número 5 (String)