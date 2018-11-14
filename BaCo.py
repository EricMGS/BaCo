#############################################################################################################
#                                                Author: EricMGS                                            #
#                                                 . .-. .. -.-.                                             #
#                                              Date: marco de 2018                                          #
#                                                                                                           #
#   Programa que converte base numericas, da base 2 ate 62. Tem como valor de saida maximo 100 caracteres   #
#############################################################################################################


#tabela de digitos para conversao de acordo com a posicao da string
digitos = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

#converte um valor para a base desejada
def Converte (entrada, base_entrada, base_saida):
    
    #transforma letras em numeros para efeito de calculo
    def DigitoDec (digito):
        for x in range(base_entrada):
            if digito == digitos[x]:
                return x
        return 'Erro'
    
    #converte a entrada em decimal
    decimal = 0
    expoente = 0
    for x in range(len(entrada) - 1, 0, -1):
        if DigitoDec (entrada [x]) == 'Erro':
            return 'Erro'
        else:
            decimal += DigitoDec(entrada[x]) * base_entrada ** expoente
            expoente += 1
    
    #converte decimal para a saida
    count = 0
    saida = ''
    while decimal:
        x = int(decimal % base_saida)
        saida += digitos[x]
        decimal //= base_saida
        count += 1
    return saida[::-1]

# . .-. .. -.-.
