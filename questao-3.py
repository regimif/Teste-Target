# Ver arquivo readme.md para explicação mais detalhada
# Importamos o modulo json e abrimos o arquivo para leitura com load.
import json

with open("dados.json", "r") as file:
    dados = json.load(file)

# Filtramos os valores maiores que 0
valores_validos = [item["valor"] for item in dados if item["valor"] > 0]

# Nos valores filtrados, obtemos o seu mínimo, máximo e média.
menor_valor = min(valores_validos)
maior_valor = max(valores_validos)
media = sum(valores_validos) / len(valores_validos)

# Filtramos os dias exatos onde obtivemos lucro acima da média.
dias_acima_media = [item["dia"] for item in dados if item["valor"] > media]

# Resultados são impressos.
print(f"Menor valor obtido do mês: {menor_valor}")
print(f"Maior valor obtido do mês: {maior_valor}")
print(f"Media mensal: {media}")
print(f"São {str(len(dias_acima_media))} dias de lucro acima da média! São eles: {dias_acima_media}.")