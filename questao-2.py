# Ver arquivo readme.md para explicação mais detalhada.
# Gera a sequencia fibonacci até que o número gerado seja maior ou igual que o numero passado pelo usuario, no parâmetro numero.
def gerar_fibonacci(numero):
    fib = [0, 1]
    while fib[-1] < numero:
        fib.append(fib[-1] + fib[-2])
    return fib

# Obtemos o input digitado pelo usuário, que vira o parâmetro de função gerar_fibonacci, e lidamos com ele no try com uma condição if e else caso o número esteja ou não na lista Fibonacci.
while True:
    try:
        input_usuario = int(input("Digite um número para verificar se ele está na sequência Fibonacci: "))
        sequencia_fib = gerar_fibonacci(input_usuario)

        if input_usuario in sequencia_fib:
            print(f"O número {input_usuario} está na sequência Fibonacci :)")
        else:
            print(f"O número {input_usuario} NÃO está na sequência Fibonacci :(")
        break

    except ValueError:
        print("Digite um número válido.")