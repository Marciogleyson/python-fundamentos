# Ex. 1: Solicitar um número inteiro e apresentar se ele é menor que 15 ou maior que 15
# Ex. 2: Solicitar o nome de um animal e apresentar a quantidade de caracteres
# Ex. 3: Solicitar um texto, remover espaços do começo transformando em minúsculo
# Ex. 4: Solicitar o nome de uma empresa e remover o texto 'LTDA', assim como, 'SA'.
# Ex. 5: Solicitar o nome do curso e apresentar se o curso começa com SuperDev, caso contrário apresentar que não começa com SuperDev
# Ex. 6: Solicitar uma idade e apresentar se é:
#   - Adulto
#   - Criança
#   - Adolescente
#   - Idoso
#  UTILIZAR WHILE para estes exercícios abaixo:
# Ex. 7: Solicitar o nome da empresa e verificar se termina com LTDA, apresentar que é uma empresa 'Sociedade de responsabilidade limitada', caso terminar com SA apresentar que é uma empresa 'Sociedade Anônima
# Ex. 8: Solicitar 5 vezes o nome do dia da semana
# Ex. 9: Solicitar o nome da cidade e a quantidade de habitantes para quatro cidades.
# Ex. 10: Solicitar o nome e altura de 6 alunos, descobrir  qual a maior altura e apresentar
# Ex. 11: Solicitar nome e preço de 5 notebooks, descobrir qual o nome e o valor do notebook que tem o menor preço
# Ex. 12: Solicitar o preço do petróleo e tratar o erro (neste não precisa de while, somente try/except)
# Ex. 12: Solicitar o peso da carne e tratar o erro (neste precisa de while e try/except)
# Ex. 13: Solicitar o salário do pedreiro (neste precisa de while e try/catch), passos para resolver:
#         Solicitar o salário
#         Adicionar o try/except
#         Fazer com que repita com while
#         Validar que o salário mínimo é de R$ 4000,00
#         Validar que o salário máximo é R$ 15000,00
# Ex. 13: Solicitar nome do projeto, categoria e seu custo, apresentar conforme abaixo:
#           - Quantidade de projetos da categoria 'Cross Fit'
#           - Quantidade de projetos da categoria 'Pilates'
#           - Quantidade de projetos da categoria 'Fisioculturismo'
# Ex. 14: Solicitar nome, nota 1, nota 2 e nota 3 até que o usuário digite 'fim'.
# Ex. 14: (continuação) Calcular a média das notas e apresentar.
# Ex. 14: (continuação) Descobrir qual o status da média e apresentar
#        Critérios de média:
#        Até 4.99 reprovado
#        Até 6.99 em exame
#        Até 10 aprovado
# Ex. 14: (continuação) Descobrir e apresentar qual é a menor nota 1
# Ex. 14: (continuação) Descobrir e apresentar qual é a maior nota 2
# Ex. 14: (continuação) Descobrir e apresentar qual é a maior média e o nome do aluno
# Ex. 14: (continuação) Descobrir e apresentar qual é a menor média e o nome do aluno
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que tem "Enzo" em seu nome
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que o nome começa com "Valentina"
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que o status é reprovado
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que o status é aprovado
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que o status é em exame

def exemplo_numero():
    numero = int(input("Digite o numero: "))
    if numero < 15:
        print("O Número e menor que 15")
    else:
         print("Número Maior que 15")    

#exemplo_numero()    

def exemplo_animal():
    animal = str(input("Digite o nome do animal: "))
    print("O nome do animal tem", len(animal), "caracteres")

#exemplo_animal()    

def exemplo_texto():
    texto = (input("Digite um texto: "))
    print(texto.lstrip().lower())

#exemplo_texto()

def solicitar_empresa():
    empresa = (input("Digite o nome da Empresa: ")) 
    empresa2 = empresa.upper().replace("LTDA", "").replace("SA", "")
    print(empresa2)

#solicitar_empresa()    

def nome_curso():
    curso = input("Digite o nome do Curso: ")
    if curso.upper().startswith("SUPERDEV"):
        print("O Curso e SuperDev")
    else:
        print("O Curso não é SuperDev")   

#nome_curso()         

def exemplo_idade():
    idade = int(input("Digite a idade: "))
    if idade <= 12:
        print("Idade de Criança")
    elif idade > 12 or idade < 18:
        print("E um Adolecente")
    elif idade > 18 or idade < 64:
        print("Adulto")     

    else:
        print("E idoso")   

exemplo_idade()            
