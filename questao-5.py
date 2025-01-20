# Ver arquivo readme.md para explicação mais detalhada.
# Obtemos o input do usuário.
input_usuario = input("Digite uma string:")

# Criamos uma string vazia para armazenar a nossa futura string invertida.
string_invertida = ""

# Iteramos sobre cada caractere do input, e o adicionamos inversamente na nova string
# Imprimimos o valor
for i in range(len(input_usuario) -1, -1, -1):
    string_invertida += input_usuario[i]
print("String invertida:", string_invertida)