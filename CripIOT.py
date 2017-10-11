"""
    TITLE: CRIPTOGRAFIA SIMÉTRICA CLÁSSICA PARA APLICAÇÃO EM PLATAFORMAS IOT
    AUTHOR: GABRIEL KRÜGER
    DATE: 07/09/17
    v1.3
"""

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

Banner()

try:
    option = 0
    while option not in range(1, 5):
        option = int(input(">>> "))

    if option == 1:
        # text to be encrypted - text is a list of letters
        text = input("[+] Digite um texto para ser Criptografado/Type a text to be Encrypted: ")

        os.system("cls" or "clear")
        print("[-] Encriptando/Encrypting...")

        c = CifraCesar()
        text = c.encrypt(text)

        print("[=] O resultado do texto Criptografado é/The result of the Encrypted text is: ", text)

    elif option == 2:
        text = input("[+] Digite um texto para ser Decriptografado/Type a text to be Decrypted: ")

        os.system("cls" or "clear")
        print("[-] Decriptando/Decrypting...")
        c = CifraCesar()
        text = c.decrypt(text)
        print("[=] O resultado do texto Decriptografado é/The result of the Decrypted text is: ", text)

    elif option == 3:
        print(option3)

    elif option == 4:
        print(option4)

except KeyboardInterrupt:
    print('\n[!] Saindo/Getting out...')
except ValueError:
    print('\n[!] Insira um valor correto/Insert a correct value.')
