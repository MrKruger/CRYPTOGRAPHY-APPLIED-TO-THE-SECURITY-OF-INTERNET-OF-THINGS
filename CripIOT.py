"""
    TITLE: CRIPTOGRAFIA SIMÉTRICA CLÁSSICA PARA APLICAÇÃO EM PLATAFORMAS IOT
    AUTHOR: GABRIEL KRÜGER
    DATE: 07/09/17
    v1.3
"""

import numpy as np                                                                                                     
import math                                                                                                             
import os

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
+-------------------------+
|   Selecione uma opção   |
+-------------------------+

+-------------------------+
| [1] Encriptar           |
| [2] Decriptar           |
| [3] Ajuda               |
| [4] Créditos            |
+-------------------------+
            """)

Banner()

try:
    option = int(input(">>> "))
    while option != 1 and option != 2 and option != 3 and option != 4:
        option = int(input(">>> "))

    if option == 1:
        class Cifra_de_Cesar(object):
            "Define a função __init__ que inicializa o estado inicial de um objeto."

            def __init__(self):
                pass

            "Define a função Encriptar que cifra um determinado texto."

            def Encriptar(self, Mensagem, Chave):
                Mensagem_Cifrada = ""
                for Letra in Mensagem:
                    if Letra.isalpha():
                        Index = ord(Letra)
                        Index += Chave

                        if Letra.isupper():
                            if Index > ord("Z"):
                                Index -= 26
                            elif Index < ord("A"):
                                Index += 26

                        elif Letra.islower():
                            if Index > ord("z"):
                                Index -= 26
                            elif Index < ord("a"):
                                Index += 26

                        Mensagem_Cifrada += chr(Index)
                    else:
                        Mensagem_Cifrada += Letra
                return Mensagem_Cifrada

            "Define a função Decriptar que decifra um determinado texto."

            def Decriptar(self, Mensagem, Chave):
                Mensagem_Cifrada = ""
                Chave = -Chave
                for Letra in Mensagem:
                    if Letra.isalpha():
                        Index = ord(Letra)
                        Index += Chave

                        if Letra.isupper():
                            if Index > ord("Z"):
                                Index -= 26
                            elif Index < ord("A"):
                                Index += 26

                        elif Letra.islower():
                            if Index > ord("z"):
                                Index -= 26
                            elif Index < ord("a"):
                                Index += 26

                        Mensagem_Cifrada += chr(Index)
                    else:
                        Mensagem_Cifrada += Letra
                return Mensagem_Cifrada

        Rodadas = 0                                                                                                             
        Numero_de_Repetições = 25                                                                                              

        Texto_Claro = input("[+] Digite um texto para ser Criptografado: ")                                                    

        lista_chaves_1 =  [5,17,25,10,18,24,6,4,9,19,20,14,22,15,7,23,3,16,1,12,2,8,21,13,11]
        lista_chaves_2 =  [2,3,15,11,25,6,21,4,19,20,18,17,13,10,12,24,1,5,16,7,9,8,22,23,14]
        lista_chaves_3 =  [16,12,24,14,8,1,15,21,23,20,3,11,9,2,17,10,18,4,25,5,19,6,13,22,7]
        lista_chaves_4 =  [24,10,23,20,12,17,7,3,1,8,16,15,11,25,22,14,18,13,19,6,4,9,21,5,2]
        lista_chaves_5 =  [4,9,19,2,15,24,22,1,20,16,17,3,23,11,14,5,6,25,13,21,12,10,7,18,8]
        lista_chaves_6 =  [7,14,22,9,8,15,20,1,11,10,3,19,18,2,16,24,23,4,13,21,25,6,12,17,5]
        lista_chaves_7 =  [21,10,19,14,13,11,2,9,18,8,25,20,1,22,23,15,24,7,16,17,4,6,3,5,12]
        lista_chaves_8 =  [4,20,11,6,18,12,7,5,14,17,3,16,19,21,22,13,23,9,15,2,10,24,8,1,25]
        lista_chaves_9 =  [14,6,4,13,18,11,2,10,23,19,7,3,20,12,21,9,16,25,5,1,15,17,22,8,24]
        lista_chaves_10 = [23,12,17,6,9,1,4,18,5,10,11,2,16,14,22,20,8,15,13,24,3,7,25,21,19]
        lista_chaves_11 = [1,16,3,25,22,2,23,4,20,12,13,14,11,15,8,19,7,5,10,21,6,18,9,24,17]
        lista_chaves_12 = [8,12,14,13,15,24,4,18,2,20,1,6,7,22,10,25,17,3,21,5,11,23,9,19,16]
        lista_chaves_13 = [20,10,6,19,7,17,9,11,2,8,14,23,18,12,16,25,5,1,4,13,24,22,3,21,15]
        lista_chaves_14 = [18,20,4,24,9,2,14,5,12,19,16,1,7,8,11,25,22,6,17,10,21,15,3,23,13]
        lista_chaves_15 = [11,12,25,23,19,9,20,22,10,14,4,1,13,5,6,2,8,7,18,16,15,24,17,3,21]
        lista_chaves_16 = [25,4,22,21,24,13,11,6,1,18,2,17,8,20,12,16,5,14,19,3,9,23,15,7,10]
        lista_chaves_17 = [6,15,12,17,11,20,23,9,5,16,2,19,3,22,8,7,1,14,24,18,10,21,4,25,22]
        lista_chaves_18 = [13,23,14,12,11,7,15,24,18,4,17,2,8,25,6,3,5,22,19,20,10,16,1,21,9]
        lista_chaves_19 = [17,14,12,13,1,24,4,18,15,3,16,10,20,22,21,9,2,25,5,19,11,23,8,7,6]
        lista_chaves_20 = [12,6,3,9,25,14,21,18,19,2,23,1,11,15,5,20,13,22,24,8,17,10,16,7,4]
        lista_chaves_21 = [10,24,20,22,23,16,12,6,18,15,5,8,17,7,2,25,14,13,4,11,9,19,21,3,1]
        lista_chaves_22 = [19,1,21,14,11,3,20,4,2,17,13,24,12,9,23,25,16,15,5,10,22,6,8,7,18]
        lista_chaves_23 = [9,23,11,14,6,10,17,24,4,22,25,16,3,8,21,1,15,7,2,18,5,13,12,19,20]
        lista_chaves_24 = [22,2,3,10,9,25,19,4,18,13,14,8,17,24,12,1,15,21,16,20,5,7,23,11,6]
        lista_chaves_25 = [3,1,13,21,12,16,8,18,11,4,10,17,24,2,15,20,14,5,22,19,9,6,25,7,23]
        lista_chaves_26 = [22,6,8,1,11,17,3,5,18,16,25,14,9,19,13,23,12,20,7,10,15,4,21,2,24]
        lista_chaves_27 = [24,20,18,21,11,9,23,22,13,1,15,6,3,25,17,12,8,7,5,19,10,4,16,2,14]
        lista_chaves_28 = [14,16,4,11,24,12,25,19,5,6,7,10,20,15,18,1,8,21,17,22,3,23,2,9,13]
        lista_chaves_29 = [1,8,18,7,10,15,5,12,24,17,19,25,9,20,2,6,23,4,22,11,16,14,13,21,3]
        lista_chaves_30 = [24,10,23,20,12,17,7,3,1,8,16,15,11,25,22,14,18,13,19,6,4,9,21,5,2]
        lista_chaves_31 = [18,14,25,7,4,10,24,15,5,17,9,23,2,12,19,1,20,6,3,21,11,22,13,8,16]
        lista_chaves_32 = [5,8,24,7,20,10,19,3,16,23,1,25,21,6,9,13,4,15,14,22,18,11,17,2,12]
        lista_chaves_33 = [24,20,9,13,25,23,6,16,21,2,1,4,17,5,19,3,12,11,8,15,7,10,14,22,18]
        lista_chaves_34 = [22,9,16,13,11,3,15,8,19,4,10,7,6,5,12,23,25,18,1,20,14,17,2,21,24]
        lista_chaves_35 = [19,5,6,22,24,1,11,23,25,9,20,13,8,16,2,21,18,7,3,12,4,10,17,15,14]
        lista_chaves_36 = [22,10,11,15,2,18,5,4,21,17,8,6,1,3,7,23,14,19,20,13,24,16,9,12,25]
        lista_chaves_37 = [3,17,9,1,15,10,5,24,16,8,20,25,13,18,12,11,14,21,23,19,4,2,22,6,7]
        lista_chaves_38 = [4,19,10,14,23,21,7,3,13,25,24,20,1,16,5,6,11,18,22,9,8,15,2,12,17]
        lista_chaves_39 = [20,10,6,19,7,17,9,11,2,8,14,23,18,12,16,25,5,1,4,13,24,22,3,21,15]
        lista_chaves_40 = [15,10,3,1,8,11,18,24,5,9,12,21,16,6,14,22,25,2,7,17,23,19,4,20,13]
        lista_chaves_41 = [3,20,12,1,23,2,19,6,17,7,24,16,21,5,18,14,11,8,25,10,22,13,4,9,15]
        lista_chaves_42 = [25,4,22,21,24,13,11,6,1,18,2,17,8,20,12,16,5,14,19,3,9,23,15,7,10]
        lista_chaves_43 = [2,6,25,16,8,13,17,15,12,9,19,10,23,14,3,20,4,1,11,7,21,22,18,24,5]
        lista_chaves_44 = [13,23,14,12,11,7,15,24,18,4,17,2,8,25,6,3,5,22,19,20,10,16,1,21,9]
        lista_chaves_45 = [11,13,5,20,21,19,14,22,4,12,25,24,1,2,8,6,7,15,16,18,23,10,9,17,3]
        lista_chaves_46 = [2,24,7,6,25,13,18,23,15,5,12,22,1,19,16,11,8,3,10,20,17,21,9,4,14]
        lista_chaves_47 = [10,24,20,22,23,16,12,6,18,15,5,8,17,7,2,25,14,13,4,11,9,19,21,3,1]
        lista_chaves_48 = [19,20,1,6,14,22,16,17,3,13,9,15,21,10,8,4,7,12,18,23,24,2,11,5,25]
        lista_chaves_49 = [4,11,7,24,6,25,20,13,12,10,1,19,3,15,5,14,21,2,18,16,8,22,23,17,9]
        lista_chaves_50 = [15,12,19,7,24,18,13,5,3,1,11,16,2,22,4,14,17,6,25,21,23,20,9,10,8]
        lista_chaves_51 = [25,7,9,16,11,8,12,4,17,24,14,2,20,10,19,6,1,3,21,13,15,23,22,5,18]
        lista_chaves_52 = [20,8,16,9,21,24,19,23,22,4,11,7,15,10,6,14,2,18,1,12,5,17,13,25,3]

        os.system("cls" or "clear")
        print("[-] Encriptando...")

        while True:

            def Lista_Inicial_Letras(Texto_Claro_Inicial):                                                                      
                Lista = []
                Repete = len(Texto_Claro_Inicial)
                for Letras in range(Repete):
                    Lista.append(Texto_Claro_Inicial[Letras])
                return Lista

            Resultado_Lista_Inicial_Letras = Lista_Inicial_Letras(Texto_Claro)                                                  

            def Define_Tamanho_Matriz(M):
                Mensagem = M

                Tamanho_Mensagem = len(Mensagem)

                y = int(math.sqrt(Tamanho_Mensagem))

                Arredonda_Num = int(math.ceil(math.sqrt(Tamanho_Mensagem)))

                Resultado_Matriz_Zeros = np.zeros((Arredonda_Num * Arredonda_Num) - Tamanho_Mensagem, dtype=np.int)

                Resultado_Matriz_Zeros_Lista = Resultado_Matriz_Zeros.tolist()

                Resultado_Matriz_Zeros_Mensagem=np.array(Mensagem + Resultado_Matriz_Zeros_Lista).reshape((Arredonda_Num, Arredonda_Num))

                if Tamanho_Mensagem == 1:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 4:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 9:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 16:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 25:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 36:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 49:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 64:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 81:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 100:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 121:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 144:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 169:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 196:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 225:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 256:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 289:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 324:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 361:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 400:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 441:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 484:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 529:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 576:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 625:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 676:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 729:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 784:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 841:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 900:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 961:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1024:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1089:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1156:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1225:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1296:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1369:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1444:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1521:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1600:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1681:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1764:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1849:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1936:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2025:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2116:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2209:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2304:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2401:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2500:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2601:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2704:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2809:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2916:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 3025:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 3136:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 3249:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 3364:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 3481:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 3600:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 3721:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 3844:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 3969:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 4096:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 4225:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 4356:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 4489:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 4624:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 4761:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 4900:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 5041:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 5184:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 5329:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 5476:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 5625:
                    Matriz = np.array(Mensagem).reshape((y, y))
                else:
                    Matriz = Resultado_Matriz_Zeros_Mensagem

                return Matriz

            Matriz = Define_Tamanho_Matriz(Resultado_Lista_Inicial_Letras)                                                      

            Matriz_Transposta = Matriz.transpose()                                                                              

            Lista_Matriz_Transposta = Matriz_Transposta.flatten().tolist()                                                     

            def Aplica_Mul_Chaves(Resultado_Lista_Cripto):
                for i in range(25):
                    L_1 = Cifra_de_Cesar().Encriptar(Resultado_Lista_Cripto, Chave=lista_chaves_1[i])
                    L_2 = Cifra_de_Cesar().Encriptar(L_1, Chave=lista_chaves_2[i])
                    L_3 = Cifra_de_Cesar().Encriptar(L_2, Chave=lista_chaves_3[i])
                    L_4 = Cifra_de_Cesar().Encriptar(L_3, Chave=lista_chaves_4[i])
                    L_5 = Cifra_de_Cesar().Encriptar(L_4, Chave=lista_chaves_5[i])
                    L_6 = Cifra_de_Cesar().Encriptar(L_5, Chave=lista_chaves_6[i])
                    L_7 = Cifra_de_Cesar().Encriptar(L_6, Chave=lista_chaves_7[i])
                    L_8 = Cifra_de_Cesar().Encriptar(L_7, Chave=lista_chaves_8[i])
                    L_9 = Cifra_de_Cesar().Encriptar(L_8, Chave=lista_chaves_9[i])
                    L_10 = Cifra_de_Cesar().Encriptar(L_9, Chave=lista_chaves_10[i])
                    L_11 = Cifra_de_Cesar().Encriptar(L_10, Chave=lista_chaves_11[i])
                    L_12 = Cifra_de_Cesar().Encriptar(L_11, Chave=lista_chaves_12[i])
                    L_13 = Cifra_de_Cesar().Encriptar(L_12, Chave=lista_chaves_13[i])
                    L_14 = Cifra_de_Cesar().Encriptar(L_13, Chave=lista_chaves_14[i])
                    L_15 = Cifra_de_Cesar().Encriptar(L_14, Chave=lista_chaves_15[i])
                    L_16 = Cifra_de_Cesar().Encriptar(L_15, Chave=lista_chaves_16[i])
                    L_17 = Cifra_de_Cesar().Encriptar(L_16, Chave=lista_chaves_17[i])
                    L_18 = Cifra_de_Cesar().Encriptar(L_17, Chave=lista_chaves_18[i])
                    L_19 = Cifra_de_Cesar().Encriptar(L_18, Chave=lista_chaves_19[i])
                    L_20 = Cifra_de_Cesar().Encriptar(L_19, Chave=lista_chaves_20[i])
                    L_21 = Cifra_de_Cesar().Encriptar(L_20, Chave=lista_chaves_21[i])
                    L_22 = Cifra_de_Cesar().Encriptar(L_21, Chave=lista_chaves_22[i])
                    L_23 = Cifra_de_Cesar().Encriptar(L_22, Chave=lista_chaves_23[i])
                    L_24 = Cifra_de_Cesar().Encriptar(L_23, Chave=lista_chaves_24[i])
                    L_25 = Cifra_de_Cesar().Encriptar(L_24, Chave=lista_chaves_25[i])
                    L_26 = Cifra_de_Cesar().Encriptar(L_25, Chave=lista_chaves_26[i])
                    L_27 = Cifra_de_Cesar().Encriptar(L_26, Chave=lista_chaves_27[i])
                    L_28 = Cifra_de_Cesar().Encriptar(L_27, Chave=lista_chaves_28[i])
                    L_29 = Cifra_de_Cesar().Encriptar(L_28, Chave=lista_chaves_29[i])
                    L_30 = Cifra_de_Cesar().Encriptar(L_29, Chave=lista_chaves_30[i])
                    L_31 = Cifra_de_Cesar().Encriptar(L_30, Chave=lista_chaves_31[i])
                    L_32 = Cifra_de_Cesar().Encriptar(L_31, Chave=lista_chaves_32[i])
                    L_33 = Cifra_de_Cesar().Encriptar(L_32, Chave=lista_chaves_33[i])
                    L_34 = Cifra_de_Cesar().Encriptar(L_33, Chave=lista_chaves_34[i])
                    L_35 = Cifra_de_Cesar().Encriptar(L_34, Chave=lista_chaves_35[i])
                    L_36 = Cifra_de_Cesar().Encriptar(L_35, Chave=lista_chaves_36[i])
                    L_37 = Cifra_de_Cesar().Encriptar(L_36, Chave=lista_chaves_37[i])
                    L_38 = Cifra_de_Cesar().Encriptar(L_37, Chave=lista_chaves_38[i])
                    L_39 = Cifra_de_Cesar().Encriptar(L_38, Chave=lista_chaves_39[i])
                    L_40 = Cifra_de_Cesar().Encriptar(L_39, Chave=lista_chaves_40[i])
                    L_41 = Cifra_de_Cesar().Encriptar(L_40, Chave=lista_chaves_41[i])
                    L_42 = Cifra_de_Cesar().Encriptar(L_41, Chave=lista_chaves_42[i])
                    L_43 = Cifra_de_Cesar().Encriptar(L_42, Chave=lista_chaves_43[i])
                    L_44 = Cifra_de_Cesar().Encriptar(L_43, Chave=lista_chaves_44[i])
                    L_45 = Cifra_de_Cesar().Encriptar(L_44, Chave=lista_chaves_45[i])
                    L_46 = Cifra_de_Cesar().Encriptar(L_45, Chave=lista_chaves_46[i])
                    L_47 = Cifra_de_Cesar().Encriptar(L_46, Chave=lista_chaves_47[i])
                    L_48 = Cifra_de_Cesar().Encriptar(L_47, Chave=lista_chaves_48[i])
                    L_49 = Cifra_de_Cesar().Encriptar(L_48, Chave=lista_chaves_49[i])
                    L_50 = Cifra_de_Cesar().Encriptar(L_49, Chave=lista_chaves_50[i])
                    L_51 = Cifra_de_Cesar().Encriptar(L_50, Chave=lista_chaves_51[i])
                    L_52 = Cifra_de_Cesar().Encriptar(L_51, Chave=lista_chaves_52[i])
                    Lista_Cifrada_2 = L_52
                return Lista_Cifrada_2

            Resultado_Aplica_Mul_Chaves = Aplica_Mul_Chaves(Lista_Matriz_Transposta)

            Rodadas = Rodadas + 1                                                                                               
            Texto_Claro = Resultado_Aplica_Mul_Chaves
            if Rodadas >= Numero_de_Repetições:
                print("[=] O resultado do texto Criptografado é: ", Texto_Claro)
                break

    elif option == 2:
        class Cifra_de_Cesar(object):
            "Define a função __init__ que inicializa o estado inicial de um objeto."

            def __init__(self):
                pass

            "Define a função Encriptar que cifra um determinado texto."

            def Encriptar(self, Mensagem, Chave):
                Mensagem_Cifrada = ""
                for Letra in Mensagem:
                    if Letra.isalpha():
                        Index = ord(Letra)
                        Index += Chave

                        if Letra.isupper():
                            if Index > ord("Z"):
                                Index -= 26
                            elif Index < ord("A"):
                                Index += 26

                        elif Letra.islower():
                            if Index > ord("z"):
                                Index -= 26
                            elif Index < ord("a"):
                                Index += 26

                        Mensagem_Cifrada += chr(Index)
                    else:
                        Mensagem_Cifrada += Letra
                return Mensagem_Cifrada

            "Define a função Decriptar que decifra um determinado texto."

            def Decriptar(self, Mensagem, Chave):
                Mensagem_Cifrada = ""
                Chave = -Chave
                for Letra in Mensagem:
                    if Letra.isalpha():
                        Index = ord(Letra)
                        Index += Chave

                        if Letra.isupper():
                            if Index > ord("Z"):
                                Index -= 26
                            elif Index < ord("A"):
                                Index += 26

                        elif Letra.islower():
                            if Index > ord("z"):
                                Index -= 26
                            elif Index < ord("a"):
                                Index += 26

                        Mensagem_Cifrada += chr(Index)
                    else:
                        Mensagem_Cifrada += Letra
                return Mensagem_Cifrada

        Rodadas = 0                                                                                                             
        Numero_de_Repetições = 25                                                                                               

        Texto_Claro = input("[+] Digite um texto para ser Decriptografado: ")                                                   

        lista_chaves_1 =  [5,17,25,10,18,24,6,4,9,19,20,14,22,15,7,23,3,16,1,12,2,8,21,13,11]
        lista_chaves_2 =  [2,3,15,11,25,6,21,4,19,20,18,17,13,10,12,24,1,5,16,7,9,8,22,23,14]
        lista_chaves_3 =  [16,12,24,14,8,1,15,21,23,20,3,11,9,2,17,10,18,4,25,5,19,6,13,22,7]
        lista_chaves_4 =  [24,10,23,20,12,17,7,3,1,8,16,15,11,25,22,14,18,13,19,6,4,9,21,5,2]
        lista_chaves_5 =  [4,9,19,2,15,24,22,1,20,16,17,3,23,11,14,5,6,25,13,21,12,10,7,18,8]
        lista_chaves_6 =  [7,14,22,9,8,15,20,1,11,10,3,19,18,2,16,24,23,4,13,21,25,6,12,17,5]
        lista_chaves_7 =  [21,10,19,14,13,11,2,9,18,8,25,20,1,22,23,15,24,7,16,17,4,6,3,5,12]
        lista_chaves_8 =  [4,20,11,6,18,12,7,5,14,17,3,16,19,21,22,13,23,9,15,2,10,24,8,1,25]
        lista_chaves_9 =  [14,6,4,13,18,11,2,10,23,19,7,3,20,12,21,9,16,25,5,1,15,17,22,8,24]
        lista_chaves_10 = [23,12,17,6,9,1,4,18,5,10,11,2,16,14,22,20,8,15,13,24,3,7,25,21,19]
        lista_chaves_11 = [1,16,3,25,22,2,23,4,20,12,13,14,11,15,8,19,7,5,10,21,6,18,9,24,17]
        lista_chaves_12 = [8,12,14,13,15,24,4,18,2,20,1,6,7,22,10,25,17,3,21,5,11,23,9,19,16]
        lista_chaves_13 = [20,10,6,19,7,17,9,11,2,8,14,23,18,12,16,25,5,1,4,13,24,22,3,21,15]
        lista_chaves_14 = [18,20,4,24,9,2,14,5,12,19,16,1,7,8,11,25,22,6,17,10,21,15,3,23,13]
        lista_chaves_15 = [11,12,25,23,19,9,20,22,10,14,4,1,13,5,6,2,8,7,18,16,15,24,17,3,21]
        lista_chaves_16 = [25,4,22,21,24,13,11,6,1,18,2,17,8,20,12,16,5,14,19,3,9,23,15,7,10]
        lista_chaves_17 = [6,15,12,17,11,20,23,9,5,16,2,19,3,22,8,7,1,14,24,18,10,21,4,25,22]
        lista_chaves_18 = [13,23,14,12,11,7,15,24,18,4,17,2,8,25,6,3,5,22,19,20,10,16,1,21,9]
        lista_chaves_19 = [17,14,12,13,1,24,4,18,15,3,16,10,20,22,21,9,2,25,5,19,11,23,8,7,6]
        lista_chaves_20 = [12,6,3,9,25,14,21,18,19,2,23,1,11,15,5,20,13,22,24,8,17,10,16,7,4]
        lista_chaves_21 = [10,24,20,22,23,16,12,6,18,15,5,8,17,7,2,25,14,13,4,11,9,19,21,3,1]
        lista_chaves_22 = [19,1,21,14,11,3,20,4,2,17,13,24,12,9,23,25,16,15,5,10,22,6,8,7,18]
        lista_chaves_23 = [9,23,11,14,6,10,17,24,4,22,25,16,3,8,21,1,15,7,2,18,5,13,12,19,20]
        lista_chaves_24 = [22,2,3,10,9,25,19,4,18,13,14,8,17,24,12,1,15,21,16,20,5,7,23,11,6]
        lista_chaves_25 = [3,1,13,21,12,16,8,18,11,4,10,17,24,2,15,20,14,5,22,19,9,6,25,7,23]
        lista_chaves_26 = [22,6,8,1,11,17,3,5,18,16,25,14,9,19,13,23,12,20,7,10,15,4,21,2,24]
        lista_chaves_27 = [24,20,18,21,11,9,23,22,13,1,15,6,3,25,17,12,8,7,5,19,10,4,16,2,14]
        lista_chaves_28 = [14,16,4,11,24,12,25,19,5,6,7,10,20,15,18,1,8,21,17,22,3,23,2,9,13]
        lista_chaves_29 = [1,8,18,7,10,15,5,12,24,17,19,25,9,20,2,6,23,4,22,11,16,14,13,21,3]
        lista_chaves_30 = [24,10,23,20,12,17,7,3,1,8,16,15,11,25,22,14,18,13,19,6,4,9,21,5,2]
        lista_chaves_31 = [18,14,25,7,4,10,24,15,5,17,9,23,2,12,19,1,20,6,3,21,11,22,13,8,16]
        lista_chaves_32 = [5,8,24,7,20,10,19,3,16,23,1,25,21,6,9,13,4,15,14,22,18,11,17,2,12]
        lista_chaves_33 = [24,20,9,13,25,23,6,16,21,2,1,4,17,5,19,3,12,11,8,15,7,10,14,22,18]
        lista_chaves_34 = [22,9,16,13,11,3,15,8,19,4,10,7,6,5,12,23,25,18,1,20,14,17,2,21,24]
        lista_chaves_35 = [19,5,6,22,24,1,11,23,25,9,20,13,8,16,2,21,18,7,3,12,4,10,17,15,14]
        lista_chaves_36 = [22,10,11,15,2,18,5,4,21,17,8,6,1,3,7,23,14,19,20,13,24,16,9,12,25]
        lista_chaves_37 = [3,17,9,1,15,10,5,24,16,8,20,25,13,18,12,11,14,21,23,19,4,2,22,6,7]
        lista_chaves_38 = [4,19,10,14,23,21,7,3,13,25,24,20,1,16,5,6,11,18,22,9,8,15,2,12,17]
        lista_chaves_39 = [20,10,6,19,7,17,9,11,2,8,14,23,18,12,16,25,5,1,4,13,24,22,3,21,15]
        lista_chaves_40 = [15,10,3,1,8,11,18,24,5,9,12,21,16,6,14,22,25,2,7,17,23,19,4,20,13]
        lista_chaves_41 = [3,20,12,1,23,2,19,6,17,7,24,16,21,5,18,14,11,8,25,10,22,13,4,9,15]
        lista_chaves_42 = [25,4,22,21,24,13,11,6,1,18,2,17,8,20,12,16,5,14,19,3,9,23,15,7,10]
        lista_chaves_43 = [2,6,25,16,8,13,17,15,12,9,19,10,23,14,3,20,4,1,11,7,21,22,18,24,5]
        lista_chaves_44 = [13,23,14,12,11,7,15,24,18,4,17,2,8,25,6,3,5,22,19,20,10,16,1,21,9]
        lista_chaves_45 = [11,13,5,20,21,19,14,22,4,12,25,24,1,2,8,6,7,15,16,18,23,10,9,17,3]
        lista_chaves_46 = [2,24,7,6,25,13,18,23,15,5,12,22,1,19,16,11,8,3,10,20,17,21,9,4,14]
        lista_chaves_47 = [10,24,20,22,23,16,12,6,18,15,5,8,17,7,2,25,14,13,4,11,9,19,21,3,1]
        lista_chaves_48 = [19,20,1,6,14,22,16,17,3,13,9,15,21,10,8,4,7,12,18,23,24,2,11,5,25]
        lista_chaves_49 = [4,11,7,24,6,25,20,13,12,10,1,19,3,15,5,14,21,2,18,16,8,22,23,17,9]
        lista_chaves_50 = [15,12,19,7,24,18,13,5,3,1,11,16,2,22,4,14,17,6,25,21,23,20,9,10,8]
        lista_chaves_51 = [25,7,9,16,11,8,12,4,17,24,14,2,20,10,19,6,1,3,21,13,15,23,22,5,18]
        lista_chaves_52 = [20,8,16,9,21,24,19,23,22,4,11,7,15,10,6,14,2,18,1,12,5,17,13,25,3]

        os.system("cls" or "clear")
        print("[-] Decriptando...")

        while True:

            def Lista_Inicial_Letras(Texto_Claro_Inicial):                                                                      
                Lista = []
                Repete = len(Texto_Claro_Inicial)
                for Letras in range(Repete):
                    Lista.append(Texto_Claro_Inicial[Letras])
                return Lista

            Resultado_Lista_Inicial_Letras = Lista_Inicial_Letras(Texto_Claro)                                                  

            def Define_Tamanho_Matriz(M):
                Mensagem = M

                Tamanho_Mensagem = len(Mensagem)

                y = int(math.sqrt(Tamanho_Mensagem))

                Arredonda_Num = int(math.ceil(math.sqrt(Tamanho_Mensagem)))

                Resultado_Matriz_Zeros = np.zeros((Arredonda_Num * Arredonda_Num) - Tamanho_Mensagem, dtype=np.int)

                Resultado_Matriz_Zeros_Lista = Resultado_Matriz_Zeros.tolist()

                Resultado_Matriz_Zeros_Mensagem=np.array(Mensagem + Resultado_Matriz_Zeros_Lista).reshape((Arredonda_Num, Arredonda_Num))

                if Tamanho_Mensagem == 1:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 4:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 9:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 16:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 25:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 36:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 49:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 64:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 81:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 100:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 121:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 144:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 169:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 196:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 225:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 256:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 289:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 324:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 361:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 400:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 441:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 484:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 529:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 576:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 625:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 676:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 729:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 784:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 841:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 900:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 961:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1024:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1089:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1156:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1225:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1296:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1369:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1444:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1521:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1600:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1681:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1764:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1849:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 1936:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2025:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2116:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2209:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2304:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2401:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2500:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2601:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2704:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2809:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 2916:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 3025:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 3136:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 3249:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 3364:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 3481:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 3600:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 3721:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 3844:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 3969:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 4096:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 4225:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 4356:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 4489:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 4624:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 4761:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 4900:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 5041:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 5184:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 5329:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 5476:
                    Matriz = np.array(Mensagem).reshape((y, y))
                elif Tamanho_Mensagem == 5625:
                    Matriz = np.array(Mensagem).reshape((y, y))
                else:
                    Matriz = Resultado_Matriz_Zeros_Mensagem

                return Matriz

            Matriz = Define_Tamanho_Matriz(Resultado_Lista_Inicial_Letras)                                                      

            Matriz_Transposta = Matriz.transpose()                                                                              

            Lista_Matriz_Transposta = Matriz_Transposta.flatten().tolist()                                                      

            def Aplica_Mul_Chaves(Resultado_Lista_Cripto):
                for i in range(25):
                    L_1 = Cifra_de_Cesar().Decriptar(Resultado_Lista_Cripto, Chave=lista_chaves_1[i])
                    L_2 = Cifra_de_Cesar().Decriptar(L_1, Chave=lista_chaves_2[i])
                    L_3 = Cifra_de_Cesar().Decriptar(L_2, Chave=lista_chaves_3[i])
                    L_4 = Cifra_de_Cesar().Decriptar(L_3, Chave=lista_chaves_4[i])
                    L_5 = Cifra_de_Cesar().Decriptar(L_4, Chave=lista_chaves_5[i])
                    L_6 = Cifra_de_Cesar().Decriptar(L_5, Chave=lista_chaves_6[i])
                    L_7 = Cifra_de_Cesar().Decriptar(L_6, Chave=lista_chaves_7[i])
                    L_8 = Cifra_de_Cesar().Decriptar(L_7, Chave=lista_chaves_8[i])
                    L_9 = Cifra_de_Cesar().Decriptar(L_8, Chave=lista_chaves_9[i])
                    L_10 = Cifra_de_Cesar().Decriptar(L_9, Chave=lista_chaves_10[i])
                    L_11 = Cifra_de_Cesar().Decriptar(L_10, Chave=lista_chaves_11[i])
                    L_12 = Cifra_de_Cesar().Decriptar(L_11, Chave=lista_chaves_12[i])
                    L_13 = Cifra_de_Cesar().Decriptar(L_12, Chave=lista_chaves_13[i])
                    L_14 = Cifra_de_Cesar().Decriptar(L_13, Chave=lista_chaves_14[i])
                    L_15 = Cifra_de_Cesar().Decriptar(L_14, Chave=lista_chaves_15[i])
                    L_16 = Cifra_de_Cesar().Decriptar(L_15, Chave=lista_chaves_16[i])
                    L_17 = Cifra_de_Cesar().Decriptar(L_16, Chave=lista_chaves_17[i])
                    L_18 = Cifra_de_Cesar().Decriptar(L_17, Chave=lista_chaves_18[i])
                    L_19 = Cifra_de_Cesar().Decriptar(L_18, Chave=lista_chaves_19[i])
                    L_20 = Cifra_de_Cesar().Decriptar(L_19, Chave=lista_chaves_20[i])
                    L_21 = Cifra_de_Cesar().Decriptar(L_20, Chave=lista_chaves_21[i])
                    L_22 = Cifra_de_Cesar().Decriptar(L_21, Chave=lista_chaves_22[i])
                    L_23 = Cifra_de_Cesar().Decriptar(L_22, Chave=lista_chaves_23[i])
                    L_24 = Cifra_de_Cesar().Decriptar(L_23, Chave=lista_chaves_24[i])
                    L_25 = Cifra_de_Cesar().Decriptar(L_24, Chave=lista_chaves_25[i])
                    L_26 = Cifra_de_Cesar().Decriptar(L_25, Chave=lista_chaves_26[i])
                    L_27 = Cifra_de_Cesar().Decriptar(L_26, Chave=lista_chaves_27[i])
                    L_28 = Cifra_de_Cesar().Decriptar(L_27, Chave=lista_chaves_28[i])
                    L_29 = Cifra_de_Cesar().Decriptar(L_28, Chave=lista_chaves_29[i])
                    L_30 = Cifra_de_Cesar().Decriptar(L_29, Chave=lista_chaves_30[i])
                    L_31 = Cifra_de_Cesar().Decriptar(L_30, Chave=lista_chaves_31[i])
                    L_32 = Cifra_de_Cesar().Decriptar(L_31, Chave=lista_chaves_32[i])
                    L_33 = Cifra_de_Cesar().Decriptar(L_32, Chave=lista_chaves_33[i])
                    L_34 = Cifra_de_Cesar().Decriptar(L_33, Chave=lista_chaves_34[i])
                    L_35 = Cifra_de_Cesar().Decriptar(L_34, Chave=lista_chaves_35[i])
                    L_36 = Cifra_de_Cesar().Decriptar(L_35, Chave=lista_chaves_36[i])
                    L_37 = Cifra_de_Cesar().Decriptar(L_36, Chave=lista_chaves_37[i])
                    L_38 = Cifra_de_Cesar().Decriptar(L_37, Chave=lista_chaves_38[i])
                    L_39 = Cifra_de_Cesar().Decriptar(L_38, Chave=lista_chaves_39[i])
                    L_40 = Cifra_de_Cesar().Decriptar(L_39, Chave=lista_chaves_40[i])
                    L_41 = Cifra_de_Cesar().Decriptar(L_40, Chave=lista_chaves_41[i])
                    L_42 = Cifra_de_Cesar().Decriptar(L_41, Chave=lista_chaves_42[i])
                    L_43 = Cifra_de_Cesar().Decriptar(L_42, Chave=lista_chaves_43[i])
                    L_44 = Cifra_de_Cesar().Decriptar(L_43, Chave=lista_chaves_44[i])
                    L_45 = Cifra_de_Cesar().Decriptar(L_44, Chave=lista_chaves_45[i])
                    L_46 = Cifra_de_Cesar().Decriptar(L_45, Chave=lista_chaves_46[i])
                    L_47 = Cifra_de_Cesar().Decriptar(L_46, Chave=lista_chaves_47[i])
                    L_48 = Cifra_de_Cesar().Decriptar(L_47, Chave=lista_chaves_48[i])
                    L_49 = Cifra_de_Cesar().Decriptar(L_48, Chave=lista_chaves_49[i])
                    L_50 = Cifra_de_Cesar().Decriptar(L_49, Chave=lista_chaves_50[i])
                    L_51 = Cifra_de_Cesar().Decriptar(L_50, Chave=lista_chaves_51[i])
                    L_52 = Cifra_de_Cesar().Decriptar(L_51, Chave=lista_chaves_52[i])
                    Lista_Cifrada_2 = L_52
                return Lista_Cifrada_2

            Resultado_Aplica_Mul_Chaves = Aplica_Mul_Chaves(Lista_Matriz_Transposta)

            Rodadas = Rodadas + 1                                                                                             
            Texto_Claro = Resultado_Aplica_Mul_Chaves
            if Rodadas >= Numero_de_Repetições:
                print("[=] O resultado do texto Decriptografado é: ", Texto_Claro.strip("0"))
                break

    elif option == 3:
        print("""
+***************************************************************************+
|                                   HELP                                    |
+***************************************************************************+

|=> PARA ENCRIPTAR UM TEXTO, SELECIONE A OPÇÃO 1:
    => EXEMPLO: >>> 1
                [+] Digite um texto para ser Criptografado: xxxxxxxxxxx
                [-] Encriptando...
                [=] O resultado do texto Criptografado é: yyyyyyyyyyy

    => OBSERVAÇÕES:
        => O CÓDIGO ACEITA LETRAS SEM ACENTUAÇÃO E NÚMEROS.
        => É POSSÍVEL ENCRIPTAR TEXTOS DE ATÉ 5625 CARACTERES POR VEZ.

|=> PARA DECRIPTAR UM TEXTO, SELECIONE A OPÇÃO 2:
    => EXEMPLO: >>> 2
                [+] Digite um texto para ser Decriptografado: yyyyyyyyyyy
                [-] Decriptando...
                [=] O resultado do texto Decriptografado é: xxxxxxxxxxx

    => OBSERVAÇÕES:
        => O TEXTO INSERIDO PARA DECRIPTAÇÃO DEVE OBRIGATÓRIAMENTE TER
           SIDO ENCRIPTADO ANTES COM O MESMO ALGORÍTMO.

|=> PARA PEDIR AJUDA SELECIONE A OPÇÃO 3.

|=> PARA VER OS CRÉDITOS SELECIONE A OPÇÃO 4.

+***************************************************************************+
|                                   HELP                                    |
+***************************************************************************+
     """)

    elif option == 4:
        print("""
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
""")

except KeyboardInterrupt:
    print('\n[!] Saindo...')
except ValueError:
    print('\n[!] Insira um valor correto.')
