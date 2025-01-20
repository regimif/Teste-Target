Olá! 👋
Aqui neste arquivo, estarão as respostas para o teste da Target. 👇

#

Questão 1 - Dado os valores disponibilizados:

- Declaramos variáveis e valores conforme obtidos anteriormente
- Criamos um loop de while, para processar as operações com o passo a passo dado (enquanto 'K' for menor que 'indice')

RESPOSTA: soma = 91

Curiosidade: Se fôssemos utilizar um console.log dentro do while loop, teríamos iterações que resultarão nos seguintes resultados:
1,3,6,10,15,21,28,36,45,55,66,78,91
O resultado final segue sendo 91.

##

Questão 2 - Verificar se o input está presente numa sequencia fibonacci.

Podemos separar o código em 2 grandes seções, mas que necessitam uma da outra.
Primeira (Função 'gerar_fibonacci'):
- É passado um parametro chamado 'numero' que será chamado ainda na função, e estará vinculado ao nosso while loop futuro;
- A variável 'Fib' cria uma lista com os numeros 0 e 1, para começar nossa sequência Fibonacci;
- Agora vem a parte detalhada do código, onde 'Fib -1' representa o último número da nossa lista, e haverá um while loop enquanto o último número não bater com o número do usuário;
- 'Fib.append' acrescenta na lista enquanto estiver no loop, a soma do ultimo numero (fib -1) e do penultimo numero (fib -2);
- O loop termina, e é retornado a lista 'Fib' até o último número gerado.

Segunda seção ('While True'):
- Usamos o 'try', em python, para de fato tentar executar um código, e fazer algo caso não seja possível executá-lo;
- Em 'input_usuario', pegamos o input do usuário, que espera-se que seja um valor numérico int;
- Em 'sequencia_fib', acessamos a função 'gerar_fibonacci', criada na seção anterior, e passamos para ela agora o valor do input do usuário;
- Criamos uma condição 'if' para verificar se o input ('input_usuario') está dentro da lista fibonacci ('sequencia_fib');
- Em 'except', criamos um meio de lidar caso o input não seja o que esperamos. Um número ou deve estar ou não na sequencia, sendo assim, para cairmos no erro de exceção ValueError, o input do usuário provavelmente não seria numérico.

Observação: 'Except' não possui um 'break', para parar o código, e estando dentro de um 'while loop', o código é processado novamente com a mensagem de input. Isso é feito exclusivamente para não haver necessidade de rodar o código novamente caso caia na exceção.

Exemplo: Digite um número para verificar se ele está na sequência Fibonacci: 100000
O número 100000 NÃO está na sequência Fibonacci

Digite um número para verificar se ele está na sequência Fibonacci: 139583862445
O número 139583862445 está na sequência Fibonacci

IMPORTANTE: Se tratando de números absurdamente grandes (cerca de 21 digitos) o código pode apresentar inconsistências com outros geradores de sequências fibonacci online. Uma solução ainda mais segura seria utilizar uma fórmula de matemática de quadrado perfeito. Utilizando-a, percebe-se que os valores de geradores onlines podem estar incorretos, pois os valores permanecem consistentes com o código atual utilizado.

##

Questão 3 - Manipulação de dados json.

- Aqui, começamos importando o módulo 'json', para podermos trabalhar com suas propriedades e abrir o arquivo 'dados.json'.
- Abrimos o arquivo, agora com o nome de 'file', usando a função json 'load'.
- Filtramos os valores acima de 0, pois esses deveriam ser desconsiderados nos nossos cálculos, utilizando a variável 'valores_validos', onde temos acesso ao valor de cada item SE o valor do item em específico (dia) for maior que 0.
- Utilizamos funções Python comuns e autoexplicativas para obtermos nas variáveis 'menor_valor', 'maior_valor' o mínimo e o máximo, respectivamente, da variável 'valores_validos'. Para a média, somamos todos os valores na nossa variável de validação, e dividimos pelo número de itens válidos, na mesma variável.
- Criamos uma variavel 'dias_acima_media' para filtrar, dessa vez, por dia, os itens que estão com o seu valor individual acima da média mensal.
- Imprimimos todos os resultados. Contamos na impressão para melhor visualização a quantidade de dias ao todo acima da média mensal, simplesmente contando o valor total de itens na nossa lista 'dias_acima_media'.

Observação: Não foram feitas alterações ao imprimir valores. Optei por dar mais destaque aos tipos de resultado que podemos obter com o arquivo json. Podemos colocar o símbolo de qualquer moeda desejada, antes do valor, e formatar os números decimais impressos, semelhante ao que faremos na questão 4, para facilitar a leitura.

##

Questão 4 - Transformando valores brutos em percentuais de um todo

- Salvamos toda renda dos estados em um dicionário, sendo a sigla do estado 'key', e o montante 'value', seguindo o padrão de dicionario (key:value).
- Somamos todo o faturamento utilizando 'sum', ele será o nosso todo (100%).
- Criamos um novo dicionario chamado 'percentuais', com um valor associado para cada estado, por meio de uma conta matemática (é dividido a renda pelo faturamento total, vezes 100). Utilizamos também um for para iterar sobre cada item  do dicionário original, em outras palavras, estamos iterando sobre um interável, e se tratando de dicionários, a prática é conhecida como Compreensão de Dicionários.
- Por fim, imprimimos o resultado para cada estado e seu respectivo percentual no todo, formatando ainda o resultado para apenas duas casas decimais, com a formatação matemática '.2f', facilitando a leitura.

##

Questão 5 - Inverter strings

- Obtemos o input do usuário como 'input_usuario';
- Criamos uma string vazia para armazenar nossa futura string invertida ('string_invertida');
- Fazemos uma iteração sobre cada caractere do input do usuário na nova string, utilizando um for loop. Cada um dos -1 serve de instruções para a função range. O código começará no último index (start em -1), terminará depois do index 0 (end em -1) e percorrerá a string em ordem decrescente (o terceiro -1);
- Colocamos cada último caractere na sua nova posição da nova string em string_invertida;
- Imprimimos o resultado.

Exemplo: Digite uma string: String 123
String invertida: 321 gnirtS