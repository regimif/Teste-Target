# Ver arquivo readme.md para explicação mais detalhada
# Ajustamos cada valor em um dicionário python.
faturamento_estados = {
    "SP" : 67836.43,
    "RJ" : 36678.66,
    "MG" : 29229.88,
    "ES" : 27165.48,
    "Outros" : 19849.53
}

# Somamos cada valor de value no dicionário.
faturamento_total = sum(faturamento_estados.values())

# Calculamos cada estado, e transformamos o valor em porcentagem em um novo dicionário.
percentuais = {
    estado : (valor / faturamento_total) * 100
    for estado, valor in faturamento_estados.items()
}

# Iteramos pelo dicionário 'percentuais' e formatamos o valor percentual de cada estado.
print("Percentual de cada estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
