def tratar_erro_conversao_string_nao_inteira():
    # Tentar executar um trecho de código que sabemos que poderá acontecer algum erro
    try: # tente
        # convertendo o que o usuário tigitou de str para int e sabemos que pode acontecer algum erro
        numero = int(input("Digite o número: "))
    except Exception as erro: # quando ocorre algum erro executa o código daqui de dentro do except
        print("mensagem de ero", erro)

# Apresenta essa mensagem dando erro ou não
print("Programa finalizado com sucesso")      


if __name__ == "__main__":
    import os
    os.system("cls")
    tratar_erro_conversao_string_nao_inteira()