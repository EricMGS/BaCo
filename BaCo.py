#############################################################################################################
#                           Desenvolvedores: EricMGS, FabioHF, LCapalbo, OsmarV, DivanPS                    #
#                                              Data: Março de 2018                                          #
#                                                                                                           #
#   Programa que converte bases numéricas, da base 2 até 62. Tem como valor de saída máximo 100 dígitos     #
#############################################################################################################

#Tabela de dígitos para conversão de acordo com a posição da string
digitos = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

#Converte um valor para a base desejada
def Converte (entrada, base_entrada, base_saida):
    
    #Transforma letras em números para efeito de cálculo
    def DigitoDec (digito):
        for x in range(base_entrada): #o laço será executado no máximo de vezes o número da base de entrada
            if digito == digitos[x]:
                return x
        return 'Erro' #se o digito estiver fora do intervalo da base é retornado um erro
    
    #converte a entrada em decimal
    decimal = 0
    expoente = 0
    for x in range(len(entrada), 0, -1):
        if DigitoDec (entrada [x - 1]) == 'Erro': #se a transformação de letras em números retornor erro é retornado um erro de conversão
            return 'Erro'
        else:
            decimal += DigitoDec(entrada[x - 1]) * base_entrada ** expoente
            expoente += 1
    
    #converte decimal para a saida
    count = 0
    saida = '' #define a variável saída como string
    while decimal:
        x = int(decimal % base_saida)
        saida += digitos[x]
        decimal //= base_saida
        count += 1
    return saida[::-1] #retorna a string 'saida' invertida