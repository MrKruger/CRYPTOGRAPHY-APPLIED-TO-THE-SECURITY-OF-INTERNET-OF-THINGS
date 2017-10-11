"""
    TITLE: CRIPTOGRAFIA SIMÉTRICA CLÁSSICA PARA APLICAÇÃO EM PLATAFORMAS IOT
    AUTHOR: GABRIEL KRÜGER
    DATE: 07/09/17
    v1.3
"""

import numpy as np
import math
import os
from CifraCesar import CifraCesar

def Banner():
    print("""
        CCCCCCCCCCCCC                     iiii                     IIIIIIIIII     OOOOOOOOO     TTTTTTTTTTTTTTTTTTTTTTT
     CCC::::::::::::C                    i::::i                    I::::::::I   OO:::::::::OO   T:::::::::::::::::::::T
   CC:::::::::::::::C                     iiii                     I::::::::I OO:::::::::::::OO T:::::::::::::::::::::T
  C:::::CCCCCCCC::::C                                              II::::::IIO:::::::OOO:::::::OT:::::TT:::::::TT:::::T
 C:::::C       CCCCCCrrrrr   rrrrrrrrr  iiiiiiippppp   ppppppppp     I::::I  O::::::O   O::::::OTTTTTT  T:::::T  TTTTTT
C:::::C              r::::rrr:::::::::r i:::::ip::::ppp:::::::::p    I::::I  O:::::O     O:::::O        T:::::T
C:::::C              r:::::::::::::::::r i::::ip:::::::::::::::::p   I::::I  O:::::O     O:::::O        T:::::T
C:::::C              rr::::::rrrrr::::::ri::::ipp::::::ppppp::::::p  I::::I  O:::::O     O:::::O        T:::::T
C:::::C               r:::::r     r:::::ri::::i p:::::p     p:::::p  I::::I  O:::::O     O:::::O        T:::::T
C:::::C               r:::::r     rrrrrrri::::i p:::::p     p:::::p  I::::I  O:::::O     O:::::O        T:::::T
C:::::C               r:::::r            i::::i p:::::p     p:::::p  I::::I  O:::::O     O:::::O        T:::::T
 C:::::C       CCCCCC r:::::r            i::::i p:::::p    p::::::p  I::::I  O::::::O   O::::::O        T:::::T
  C:::::CCCCCCCC::::C r:::::r           i::::::ip:::::ppppp:::::::pII::::::IIO:::::::OOO:::::::O      TT:::::::TT
   CC:::::::::::::::C r:::::r           i::::::ip::::::::::::::::p I::::::::I OO:::::::::::::OO       T:::::::::T
     CCC::::::::::::C r:::::r           i::::::ip::::::::::::::pp  I::::::::I   OO:::::::::OO         T:::::::::T
        CCCCCCCCCCCCC rrrrrrr           iiiiiiiip::::::pppppppp    IIIIIIIIII     OOOOOOOOO           TTTTTTTTTTT
                                                p:::::p
                                                p:::::p
                                               p:::::::p
                                               p:::::::p
                                               p:::::::p
                                               ppppppppp
   \n""")

    print("""
+---------------------------------------------+
|   Selecione uma Opção/Selection an Option   |
+---------------------------------------------+

+---------------------------------+
| [1] Encriptar/Encrypt           |
+---------------------------------+
| [2] Decriptar/Decrypt           |
+---------------------------------+
| [3] Ajuda/Help                  |
+---------------------------------+
| [4] Créditos/Credits            |
+---------------------------------+
            """)

# definições de opções
option3 = """
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                                     HELP                                                     |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                                                                                              |
|=> PARA ENCRIPTAR UM TEXTO, SELECIONE A OPÇÃO 1/TO ENCRYPT A TEXT, SELECT THE OPTION 1:                       |
|   => EXEMPLO/EXAMPLE: >>> 1                                                                                  |
|               [+] Digite um texto para ser Criptografado/Type a text to be Encrypted: xxxxxxxxxxx            |
|               [-] Encriptando/Encrypting...                                                                  |
|               [=] O resultado do texto Criptografado é/The result of the Encrypted text is: yyyyyyyyyyy      |
|                                                                                                              |
|   => OBSERVAÇÕES/REMARKS:                                                                                    |
|       => O CÓDIGO ACEITA LETRAS SEM ACENTUAÇÃO E NÚMEROS/THE CODE ACCEPT UNLIMETED LETTERS AND NUMBERS.      |
|       => É POSSÍVEL ENCRIPTAR TEXTOS DE ATÉ 5625 CARACTERES POR VEZ/IT IS POSSIBLE TO ENCRYPT TEXTS OF UP    |
|          TO 5625 CHARACTERS ONCE.                                                                            |
|                                                                                                              |
|=> PARA DECRIPTAR UM TEXTO, SELECIONE A OPÇÃO 2/TO DECRYPT A TEXT, SELECT THE OPTION 2:                       |
|   => EXEMPLO/EXAMPLE: >>> 2                                                                                  |
|               [+] Digite um texto para ser Decriptografado/Type a text to be Decrypted: yyyyyyyyyyy          |
|               [-] Decriptando/Decrypting...                                                                  |
|               [=] O resultado do texto Decriptografado é/The result of the Decrypted text is: xxxxxxxxxxx    |
|                                                                                                              |
|   => OBSERVAÇÕES/REMARKS:                                                                                    |
|       => O TEXTO INSERIDO PARA DECRIPTAÇÃO DEVE OBRIGATÓRIAMENTE TER                                         |
|          SIDO ENCRIPTADO ANTES COM O MESMO ALGORÍTMO/THE TEXT INSERTED FOR DECRIPTION MUST BEEN ENCRYPTED    |
|          BEFORE THE SAME ALGORITHM.                                                                          |
|                                                                                                              |
|=> PARA PEDIR AJUDA SELECIONE A OPÇÃO 3/TO ASK FOR HELP SELECT THE OPTION 3.                                  |
|                                                                                                              |
|=> PARA VER OS CRÉDITOS SELECIONE A OPÇÃO 4/TO SEE THE CREDITS SELECT THE OPTION 4.                           |
|                                                                                                              |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                                     HELP                                                     |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
     """
option4 = """
 .S_SsS_S.    .S_sSSs           .S    S.    .S_sSSs     .S       S.     sSSSSs    sSSs   .S_sSSs
.SS~S*S~SS.  .SS~YS%%b         .SS    SS.  .SS~YS%%b   .SS       SS.   d%%%%SP   d%%SP  .SS~YS%%b
S%S `Y' S%S  S%S   `S%b        S%S    S&S  S%S   `S%b  S%S       S%S  d%S'      d%S'    S%S   `S%b
S%S     S%S  S%S    S%S        S%S    d*S  S%S    S%S  S%S       S%S  S%S       S%S     S%S    S%S
S%S     S%S  S%S    d*S        S&S   .S*S  S%S    d*S  S&S       S&S  S&S       S&S     S%S    d*S
S&S     S&S  S&S   .S*S        S&S_sdSSS   S&S   .S*S  S&S       S&S  S&S       S&S_Ss  S&S   .S*S
S&S     S&S  S&S_sdSSS         S&S~YSSY%b  S&S_sdSSS   S&S       S&S  S&S       S&S~SP  S&S_sdSSS
S&S     S&S  S&S~YSY%b         S&S    `S%  S&S~YSY%b   S&S       S&S  S&S sSSs  S&S     S&S~YSY%b
S*S     S*S  S*S   `S%b        S*S     S%  S*S   `S%b  S*b       d*S  S*b `S%%  S*b     S*S   `S%b
S*S     S*S  S*S    S%S        S*S     S&  S*S    S%S  S*S.     .S*S  S*S   S%  S*S.    S*S    S%S
S*S     S*S  S*S    S&S        S*S     S&  S*S    S&S   SSSbs_sdSSS    SS_sSSS   SSSbs  S*S    S&S
SSS     S*S  S*S    SSS   SS   S*S     SS  S*S    SSS    YSSP~YSSY      Y~YSSY    YSSP  S*S    SSS
        SP   SP          S%%S  SP          SP                                           SP
        Y    Y            SS   Y           Y                                            Y

                                                                                    by: @Mr.Kr¥g€₹
"""

# definições de funções utilizadas dentro da porra do while

# kk eita porra olha o tanto de chaves
lista_chaves_1 = [5, 17, 25, 10, 18, 24, 6, 4, 9, 19, 20, 14, 22, 15, 7, 23, 3, 16, 1, 12, 2, 8, 21, 13, 11]
lista_chaves_2 = [2, 3, 15, 11, 25, 6, 21, 4, 19, 20, 18, 17, 13, 10, 12, 24, 1, 5, 16, 7, 9, 8, 22, 23, 14]
lista_chaves_3 = [16, 12, 24, 14, 8, 1, 15, 21, 23, 20, 3, 11, 9, 2, 17, 10, 18, 4, 25, 5, 19, 6, 13, 22, 7]
lista_chaves_4 = [24, 10, 23, 20, 12, 17, 7, 3, 1, 8, 16, 15, 11, 25, 22, 14, 18, 13, 19, 6, 4, 9, 21, 5, 2]
lista_chaves_5 = [4, 9, 19, 2, 15, 24, 22, 1, 20, 16, 17, 3, 23, 11, 14, 5, 6, 25, 13, 21, 12, 10, 7, 18, 8]
lista_chaves_6 = [7, 14, 22, 9, 8, 15, 20, 1, 11, 10, 3, 19, 18, 2, 16, 24, 23, 4, 13, 21, 25, 6, 12, 17, 5]
lista_chaves_7 = [21, 10, 19, 14, 13, 11, 2, 9, 18, 8, 25, 20, 1, 22, 23, 15, 24, 7, 16, 17, 4, 6, 3, 5, 12]
lista_chaves_8 = [4, 20, 11, 6, 18, 12, 7, 5, 14, 17, 3, 16, 19, 21, 22, 13, 23, 9, 15, 2, 10, 24, 8, 1, 25]
lista_chaves_9 = [14, 6, 4, 13, 18, 11, 2, 10, 23, 19, 7, 3, 20, 12, 21, 9, 16, 25, 5, 1, 15, 17, 22, 8, 24]
lista_chaves_10 = [23, 12, 17, 6, 9, 1, 4, 18, 5, 10, 11, 2, 16, 14, 22, 20, 8, 15, 13, 24, 3, 7, 25, 21, 19]
lista_chaves_11 = [1, 16, 3, 25, 22, 2, 23, 4, 20, 12, 13, 14, 11, 15, 8, 19, 7, 5, 10, 21, 6, 18, 9, 24, 17]
lista_chaves_12 = [8, 12, 14, 13, 15, 24, 4, 18, 2, 20, 1, 6, 7, 22, 10, 25, 17, 3, 21, 5, 11, 23, 9, 19, 16]
lista_chaves_13 = [20, 10, 6, 19, 7, 17, 9, 11, 2, 8, 14, 23, 18, 12, 16, 25, 5, 1, 4, 13, 24, 22, 3, 21, 15]
lista_chaves_14 = [18, 20, 4, 24, 9, 2, 14, 5, 12, 19, 16, 1, 7, 8, 11, 25, 22, 6, 17, 10, 21, 15, 3, 23, 13]
lista_chaves_15 = [11, 12, 25, 23, 19, 9, 20, 22, 10, 14, 4, 1, 13, 5, 6, 2, 8, 7, 18, 16, 15, 24, 17, 3, 21]
lista_chaves_16 = [25, 4, 22, 21, 24, 13, 11, 6, 1, 18, 2, 17, 8, 20, 12, 16, 5, 14, 19, 3, 9, 23, 15, 7, 10]
lista_chaves_17 = [6, 15, 12, 17, 11, 20, 23, 9, 5, 16, 2, 19, 3, 22, 8, 7, 1, 14, 24, 18, 10, 21, 4, 25, 22]
lista_chaves_18 = [13, 23, 14, 12, 11, 7, 15, 24, 18, 4, 17, 2, 8, 25, 6, 3, 5, 22, 19, 20, 10, 16, 1, 21, 9]
lista_chaves_19 = [17, 14, 12, 13, 1, 24, 4, 18, 15, 3, 16, 10, 20, 22, 21, 9, 2, 25, 5, 19, 11, 23, 8, 7, 6]
lista_chaves_20 = [12, 6, 3, 9, 25, 14, 21, 18, 19, 2, 23, 1, 11, 15, 5, 20, 13, 22, 24, 8, 17, 10, 16, 7, 4]
lista_chaves_21 = [10, 24, 20, 22, 23, 16, 12, 6, 18, 15, 5, 8, 17, 7, 2, 25, 14, 13, 4, 11, 9, 19, 21, 3, 1]
lista_chaves_22 = [19, 1, 21, 14, 11, 3, 20, 4, 2, 17, 13, 24, 12, 9, 23, 25, 16, 15, 5, 10, 22, 6, 8, 7, 18]
lista_chaves_23 = [9, 23, 11, 14, 6, 10, 17, 24, 4, 22, 25, 16, 3, 8, 21, 1, 15, 7, 2, 18, 5, 13, 12, 19, 20]
lista_chaves_24 = [22, 2, 3, 10, 9, 25, 19, 4, 18, 13, 14, 8, 17, 24, 12, 1, 15, 21, 16, 20, 5, 7, 23, 11, 6]
lista_chaves_25 = [3, 1, 13, 21, 12, 16, 8, 18, 11, 4, 10, 17, 24, 2, 15, 20, 14, 5, 22, 19, 9, 6, 25, 7, 23]
lista_chaves_26 = [22, 6, 8, 1, 11, 17, 3, 5, 18, 16, 25, 14, 9, 19, 13, 23, 12, 20, 7, 10, 15, 4, 21, 2, 24]
lista_chaves_27 = [24, 20, 18, 21, 11, 9, 23, 22, 13, 1, 15, 6, 3, 25, 17, 12, 8, 7, 5, 19, 10, 4, 16, 2, 14]
lista_chaves_28 = [14, 16, 4, 11, 24, 12, 25, 19, 5, 6, 7, 10, 20, 15, 18, 1, 8, 21, 17, 22, 3, 23, 2, 9, 13]
lista_chaves_29 = [1, 8, 18, 7, 10, 15, 5, 12, 24, 17, 19, 25, 9, 20, 2, 6, 23, 4, 22, 11, 16, 14, 13, 21, 3]
lista_chaves_30 = [24, 10, 23, 20, 12, 17, 7, 3, 1, 8, 16, 15, 11, 25, 22, 14, 18, 13, 19, 6, 4, 9, 21, 5, 2]
lista_chaves_31 = [18, 14, 25, 7, 4, 10, 24, 15, 5, 17, 9, 23, 2, 12, 19, 1, 20, 6, 3, 21, 11, 22, 13, 8, 16]
lista_chaves_32 = [5, 8, 24, 7, 20, 10, 19, 3, 16, 23, 1, 25, 21, 6, 9, 13, 4, 15, 14, 22, 18, 11, 17, 2, 12]
lista_chaves_33 = [24, 20, 9, 13, 25, 23, 6, 16, 21, 2, 1, 4, 17, 5, 19, 3, 12, 11, 8, 15, 7, 10, 14, 22, 18]
lista_chaves_34 = [22, 9, 16, 13, 11, 3, 15, 8, 19, 4, 10, 7, 6, 5, 12, 23, 25, 18, 1, 20, 14, 17, 2, 21, 24]
lista_chaves_35 = [19, 5, 6, 22, 24, 1, 11, 23, 25, 9, 20, 13, 8, 16, 2, 21, 18, 7, 3, 12, 4, 10, 17, 15, 14]
lista_chaves_36 = [22, 10, 11, 15, 2, 18, 5, 4, 21, 17, 8, 6, 1, 3, 7, 23, 14, 19, 20, 13, 24, 16, 9, 12, 25]
lista_chaves_37 = [3, 17, 9, 1, 15, 10, 5, 24, 16, 8, 20, 25, 13, 18, 12, 11, 14, 21, 23, 19, 4, 2, 22, 6, 7]
lista_chaves_38 = [4, 19, 10, 14, 23, 21, 7, 3, 13, 25, 24, 20, 1, 16, 5, 6, 11, 18, 22, 9, 8, 15, 2, 12, 17]
lista_chaves_39 = [20, 10, 6, 19, 7, 17, 9, 11, 2, 8, 14, 23, 18, 12, 16, 25, 5, 1, 4, 13, 24, 22, 3, 21, 15]
lista_chaves_40 = [15, 10, 3, 1, 8, 11, 18, 24, 5, 9, 12, 21, 16, 6, 14, 22, 25, 2, 7, 17, 23, 19, 4, 20, 13]
lista_chaves_41 = [3, 20, 12, 1, 23, 2, 19, 6, 17, 7, 24, 16, 21, 5, 18, 14, 11, 8, 25, 10, 22, 13, 4, 9, 15]
lista_chaves_42 = [25, 4, 22, 21, 24, 13, 11, 6, 1, 18, 2, 17, 8, 20, 12, 16, 5, 14, 19, 3, 9, 23, 15, 7, 10]
lista_chaves_43 = [2, 6, 25, 16, 8, 13, 17, 15, 12, 9, 19, 10, 23, 14, 3, 20, 4, 1, 11, 7, 21, 22, 18, 24, 5]
lista_chaves_44 = [13, 23, 14, 12, 11, 7, 15, 24, 18, 4, 17, 2, 8, 25, 6, 3, 5, 22, 19, 20, 10, 16, 1, 21, 9]
lista_chaves_45 = [11, 13, 5, 20, 21, 19, 14, 22, 4, 12, 25, 24, 1, 2, 8, 6, 7, 15, 16, 18, 23, 10, 9, 17, 3]
lista_chaves_46 = [2, 24, 7, 6, 25, 13, 18, 23, 15, 5, 12, 22, 1, 19, 16, 11, 8, 3, 10, 20, 17, 21, 9, 4, 14]
lista_chaves_47 = [10, 24, 20, 22, 23, 16, 12, 6, 18, 15, 5, 8, 17, 7, 2, 25, 14, 13, 4, 11, 9, 19, 21, 3, 1]
lista_chaves_48 = [19, 20, 1, 6, 14, 22, 16, 17, 3, 13, 9, 15, 21, 10, 8, 4, 7, 12, 18, 23, 24, 2, 11, 5, 25]
lista_chaves_49 = [4, 11, 7, 24, 6, 25, 20, 13, 12, 10, 1, 19, 3, 15, 5, 14, 21, 2, 18, 16, 8, 22, 23, 17, 9]
lista_chaves_50 = [15, 12, 19, 7, 24, 18, 13, 5, 3, 1, 11, 16, 2, 22, 4, 14, 17, 6, 25, 21, 23, 20, 9, 10, 8]
lista_chaves_51 = [25, 7, 9, 16, 11, 8, 12, 4, 17, 24, 14, 2, 20, 10, 19, 6, 1, 3, 21, 13, 15, 23, 22, 5, 18]
lista_chaves_52 = [20, 8, 16, 9, 21, 24, 19, 23, 22, 4, 11, 7, 15, 10, 6, 14, 2, 18, 1, 12, 5, 17, 13, 25, 3]

def getLetterList(text):
    letterList = []
    Repete = len(text)
    for letter in range(Repete):
        letterList.append(text[letter])
    return letterList

def Define_Tamanho_Matriz(M):
    mensagem = M

    Tamanho_Mensagem = len(mensagem)

    y = int(math.sqrt(Tamanho_Mensagem))

    Arredonda_Num = int(math.ceil(math.sqrt(Tamanho_Mensagem)))

    Resultado_Matriz_Zeros = np.zeros((Arredonda_Num * Arredonda_Num) - Tamanho_Mensagem, dtype=np.int)

    Resultado_Matriz_Zeros_Lista = Resultado_Matriz_Zeros.tolist()

    Resultado_Matriz_Zeros_Mensagem = np.array(mensagem + Resultado_Matriz_Zeros_Lista).reshape((
        Arredonda_Num,
        Arredonda_Num
    ))

    quadrados = [x * x for x in range(76)]
    if Tamanho_Mensagem in quadrados:
        matriz = np.array(mensagem).reshape((y, y))
    else:
        matriz = Resultado_Matriz_Zeros_Mensagem

    return matriz

def Aplica_Mul_Chaves(calc, Resultado_Lista_Cripto):
    for i in range(25):
        L_1 = calc(Resultado_Lista_Cripto, lista_chaves_1[i])
        L_2 = calc(L_1, lista_chaves_2[i])
        L_3 = calc(L_2, lista_chaves_3[i])
        L_4 = calc(L_3, lista_chaves_4[i])
        L_5 = calc(L_4, lista_chaves_5[i])
        L_6 = calc(L_5, lista_chaves_6[i])
        L_7 = calc(L_6, lista_chaves_7[i])
        L_8 = calc(L_7, lista_chaves_8[i])
        L_9 = calc(L_8, lista_chaves_9[i])
        L_10 = calc(L_9, lista_chaves_10[i])
        L_11 = calc(L_10, lista_chaves_11[i])
        L_12 = calc(L_11, lista_chaves_12[i])
        L_13 = calc(L_12, lista_chaves_13[i])
        L_14 = calc(L_13, lista_chaves_14[i])
        L_15 = calc(L_14, lista_chaves_15[i])
        L_16 = calc(L_15, lista_chaves_16[i])
        L_17 = calc(L_16, lista_chaves_17[i])
        L_18 = calc(L_17, lista_chaves_18[i])
        L_19 = calc(L_18, lista_chaves_19[i])
        L_20 = calc(L_19, lista_chaves_20[i])
        L_21 = calc(L_20, lista_chaves_21[i])
        L_22 = calc(L_21, lista_chaves_22[i])
        L_23 = calc(L_22, lista_chaves_23[i])
        L_24 = calc(L_23, lista_chaves_24[i])
        L_25 = calc(L_24, lista_chaves_25[i])
        L_26 = calc(L_25, lista_chaves_26[i])
        L_27 = calc(L_26, lista_chaves_27[i])
        L_28 = calc(L_27, lista_chaves_28[i])
        L_29 = calc(L_28, lista_chaves_29[i])
        L_30 = calc(L_29, lista_chaves_30[i])
        L_31 = calc(L_30, lista_chaves_31[i])
        L_32 = calc(L_31, lista_chaves_32[i])
        L_33 = calc(L_32, lista_chaves_33[i])
        L_34 = calc(L_33, lista_chaves_34[i])
        L_35 = calc(L_34, lista_chaves_35[i])
        L_36 = calc(L_35, lista_chaves_36[i])
        L_37 = calc(L_36, lista_chaves_37[i])
        L_38 = calc(L_37, lista_chaves_38[i])
        L_39 = calc(L_38, lista_chaves_39[i])
        L_40 = calc(L_39, lista_chaves_40[i])
        L_41 = calc(L_40, lista_chaves_41[i])
        L_42 = calc(L_41, lista_chaves_42[i])
        L_43 = calc(L_42, lista_chaves_43[i])
        L_44 = calc(L_43, lista_chaves_44[i])
        L_45 = calc(L_44, lista_chaves_45[i])
        L_46 = calc(L_45, lista_chaves_46[i])
        L_47 = calc(L_46, lista_chaves_47[i])
        L_48 = calc(L_47, lista_chaves_48[i])
        L_49 = calc(L_48, lista_chaves_49[i])
        L_50 = calc(L_49, lista_chaves_50[i])
        L_51 = calc(L_50, lista_chaves_51[i])
        L_52 = calc(L_51, lista_chaves_52[i])
        Lista_Cifrada_2 = L_52
    return Lista_Cifrada_2

Banner()

try:
    option = 0
    while option not in range(1, 4):
        option = int(input(">>> "))

    if option == 1:
        countLoop = 0  # index of a loop
        numOfLoops = 25  # to use in while

        # text to be encrypted - text is a list of letters
        text = input("[+] Digite um texto para ser Criptografado/Type a text to be Encrypted: ")

        os.system("cls" or "clear")
        print("[-] Encriptando/Encrypting...")

        for i in range(25):
            Resultado_Lista_Inicial_Letras = getLetterList(text)

            Matriz = Define_Tamanho_Matriz(Resultado_Lista_Inicial_Letras)

            Matriz_Transposta = Matriz.transpose()

            Lista_Matriz_Transposta = Matriz_Transposta.flatten().tolist()

            cifra = CifraCesar()  # instance the class just when it is used
            text = Aplica_Mul_Chaves(cifra.encrypt, Lista_Matriz_Transposta)

        print("[=] O resultado do texto Criptografado é/The result of the Encrypted text is: ", text)

    elif option == 2:
        text = input("[+] Digite um texto para ser Decriptografado/Type a text to be Decrypted: ")

        os.system("cls" or "clear")
        print("[-] Decriptando/Decrypting...")

        for i in range(25):
            Resultado_Lista_Inicial_Letras = getLetterList(text)

            Matriz = Define_Tamanho_Matriz(Resultado_Lista_Inicial_Letras)

            Matriz_Transposta = Matriz.transpose()

            Lista_Matriz_Transposta = Matriz_Transposta.flatten().tolist()

            cifra = CifraCesar()
            text = Aplica_Mul_Chaves(cifra.decrypt, Lista_Matriz_Transposta)

        print("[=] O resultado do texto Decriptografado é/The result of the Decrypted text is: ", text)

    elif option == 3:
        print(option3)

    elif option == 4:
        print(option4)

except KeyboardInterrupt:
    print('\n[!] Saindo/Getting out...')
except ValueError:
    print('\n[!] Insira um valor correto/Insert a correct value.')
