
# Passo 1: Solicitar o orçamento mensal
def __solicitar_orcamento() -> float:
   limite_despesas = 0
   while limite_despesas <= 0:
       try:
          limite_despesas = float(input("Digite seu limite de gastos mensal: "))
          if limite_despesas <= 0:
            print("O valor deve ser maior que zero, digite novamente o valor: ")
       except  ValueError as error:    
           print("!!!ERRO!! Insira um número válido")
   return limite_despesas

#__solicitar_orcamento()

# Passo 2: Solicitar as despesas mensais em diferentes categorias
def __solicitar_despesas_alimentacao() -> float:
    despesas_alimentacao = 0
    while despesas_alimentacao <= 0:
        try:
            despesas_alimentacao = float(input("Digite seus gastos com Alimentação: "))
            if despesas_alimentacao <= 0:
                print("Valor deve ser maior que zero, digite novamente o valor: ")
        except ValueError as error:
            print("!!!ERRO!! Insira um número válido")
    return despesas_alimentacao
        
#__solicitar_despesas_alimentacao()    


def __solicitar_despesas_transporte()-> float:
    despesas_transporte = 0
    while despesas_transporte <= 0:
        try:
            despesas_transporte = float(input("Digite sua dispesa com Transporte: "))  
            if despesas_transporte <= 0:
                print("Valor deve ser maior que zero, digite novamente o valor: ")
        except ValueError as error:
              print("!!!ERRO!! Insira um número válido")   
              
    return despesas_transporte      

#__solicitar_despesas_transporte()    


def __solicitar_despesas_lazer() -> float:
    despesas_lazer = 0
    while despesas_lazer <= 0:
        try:
            despesas_lazer = float(input("Digite as despesas de Lazer: "))
            if despesas_lazer <= 0:
                print("Valor deve ser maior que zero, digite novamente o valor: ")
        except ValueError as error:
             print("!!!ERRO!! Insira um número válido")  
             
    return despesas_lazer   

#__solicitar_despesas_lazer()     

# Passo 4: Comparar o total de despesas com o orçamento
def __solicitar_despesas_saude() -> float:
    despesas_saude = 0
    while despesas_saude <= 0:
        try:
            despesas_saude = float(input("Digite os valores gastos com Saúde: ")) 
            if despesas_saude <= 0:
                print("Valor deve ser maior que zero, digite novamente o valor: ")
        except ValueError as error:
            print("!!!ERRO!! Insira um número válido")   
            
    return despesas_saude 

#__solicitar_despesas_saude()   

# Passo 3: Calcular o total de despesas
def __calcular_total_despesas(alimentacao: float, transporte: float, lazer: float, saude: float) -> float:
   total_despesas = alimentacao + transporte + lazer + saude
   return total_despesas

# Passo 4: Comparar o total de despesas com o orçamento
def __comparar_orcamento_com_despesas(orcamento: float, total_despesas: float) -> str:
    if orcamento < total_despesas:
        return("Você !!!UlTRAPASSOU SEU LIMITE!!!", total_despesas)
    else:
        return("Você !!!Está DENTRO DO ORÇAMENTO!!!", total_despesas)   
        
# Passo 5: Exibir os resultados
def __exibir_resultados(orcamento: float, alimentacao: float, transporte: float, lazer: float, saude: float, total_dispesas: float, resultado: str):
    
    print("O valor do Orçamento mensal foi: ", orcamento)   
    print("O gasto com alientação foi: ", alimentacao)
    print("O gasto com Transporte foi: ", transporte)
    print("O gaso com lazer foi: ", lazer)
    print("O gasto com saúde foi: ", saude)
    print("O valor total das despesas: ", total_dispesas)
    print(resultado) 

    
def controle_de_despesas():

    orcamento = __solicitar_orcamento()
    alimentacao = __solicitar_despesas_alimentacao()
    transporte = __solicitar_despesas_transporte()
    lazer = __solicitar_despesas_lazer()
    saude = __solicitar_despesas_saude()
    total_despesas = __calcular_total_despesas(alimentacao, transporte, lazer, saude)
    resultado = __comparar_orcamento_com_despesas(orcamento, total_despesas)
    __exibir_resultados(orcamento, alimentacao, transporte, lazer, saude, total_despesas, resultado)


        
                
                    
    
    

