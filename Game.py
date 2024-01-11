import random

escolha_pc = int(random.randint(1, 10))
contador = (0)
escolha_n = (0)
soma = ((escolha_n + escolha_pc) % 2 )

while True :
    escolha_ip = str(input("Ímpar [ I , i] ou Par [P , p] ? : ")).upper()

    escolha_n = int(input("Digite seu número : "))
    if soma == 0  : 
        if escolha_ip == "P" :
            contador += 1
            print(f''' -- O computador escolheu {escolha_pc} -- 
              Você venceu! Sequência de vitórias : {contador}''') 
        elif escolha_ip == "I" :
            print(f'''  -- O computador escolheu {escolha_pc} --
              Você Perdeu... Sequência de vitórias : {contador}''')
            viadagi = str(input("Deseja jogar novamente? [ S ] ou [ N ]: ")).upper()
            if viadagi == "N" :
                break
    elif soma != 0 :
        if escolha_ip == "I" :
            contador += 1
            print(f'''  -- O computador escolheu {escolha_pc} --
              Você Venceu! Sequência de vitórias : {contador}''')
        elif escolha_ip == "P" : 
            print(f'''  -- O computador escolheu {escolha_pc} --
              Você Perdeu... Sequência de vitórias : {contador}''')
            viadagi = str(input("Deseja jogar novamente? [ S ] ou [ N ]: ")).upper()
            if viadagi == "N" : 
                break
print(" -------------------------------- Obrigado por jogar! --------------------------------")
