
import random
random_number = random.randint(0, 1)

print("Bem vindo a pizza planet.")
# Pedindo pizza.

pizza_tamanho = input("Qual o tamanho da pizza que você quer? Pequena, média, grande. ").lower()
pizza_peperoni = input("Você quer peperone ? Sim, não. ").lower()
pizza_quijo_extra = input("Você quer queijo extra? Sim, não. ").lower()

conta = 0
if pizza_tamanho == "pequena":
  conta += 15
elif pizza_tamanho == "média" or pizza_tamanho == "media":
  conta += 20
elif pizza_tamanho == "grande":
  conta += 25

if pizza_peperoni == "sim":
  if pizza_tamanho == "pequena":
    conta += 2
  else:
    conta += 3
if pizza_quijo_extra == "sim":
  conta += 1
result = print(f"Você escolheu pizza de tamanho {pizza_tamanho}. Peperoni {pizza_peperoni}. Queijo extra {pizza_quijo_extra}. Sua conta final é de {conta}$.")
"\n"
# conta/gorgeja calculadora

gorjeta = int(input("Quanto você quer dar de gorgeta em porcentagem. 10, 12, 15? "))
calculando_gorjeta = conta * gorjeta / 100
conta_total = conta + calculando_gorjeta
pessoas = int(input("Quantas pessoas você tem com você? "))
total_para_cada_pessoa = conta_total / pessoas
arredondando_conta_total = round(total_para_cada_pessoa, 2)
resultado_conta_cada_pessoa = print(f"Cada pessoa irá ajudar com a conta total em {arredondando_conta_total}$.")

# calculadora de massa corporal
"\n"
print("Ao usar a nossa pizzaria você ganhou um calculo de massa corporal!")
massa_corporal = input("Você quer calcular a sua massa corporal? Sim, não.").lower()
if massa_corporal == "sim":
  altura = float(input("Qual a sua altura? "))
  peso = float(input("Qual o seu peso?"))
  calculo_massa_corporal = peso / altura ** 2
  massa_corporal_arredondada = round(calculo_massa_corporal)
  if massa_corporal_arredondada < 18.5:
    print(f"Sua massa corporal é de {massa_corporal_arredondada}, você esta abaixo do peso.")
  elif massa_corporal_arredondada < 25:
    print(f"Sua massa corporal é de {massa_corporal_arredondada}, você esta com o peso na medida certa.")
  elif massa_corporal_arredondada < 30:
    print(f"Sua massa corporal é de {massa_corporal_arredondada}, você esta acima do peso.")
  elif massa_corporal_arredondada < 35:
    print(f"Sua massa corporal é de {massa_corporal_arredondada}, você esta obeso.")
  else:
    print(f"Sua massa corporal é de {massa_corporal_arredondada}, você esta clinicamente diagnosticado com obesidade.")

# jogo

jogo = input(print("Você ganhou também a oportunidade de jogar um jogo, se você ganhar o jogo, a sua pizza sai de graça! Mas se você perder, sua conta final vai dobrar. Você quer jogar? Sim, não. ")).lower()

if jogo == "sim":
  passo1 = input("Você se encontra em frente a um labirinto, você escolhe começar indo para a direita ou esquerda?  ").lower()
  if passo1 == "direita":
    passo2 = input("Você esta a frente de um lago, e do outro lado do lago tem uma ilha, você vai ir 'nadando' ou 'vai esperar um  barco?' ").lower()
    if passo2 == "esperar um barco" or passo2 == "esperar" or passo2 == "esperar barco":
      passo3 = input("Você precisa escolher entre três portas, vermelha, amarela, azul, qual delas você escolhe? ").lower()
      if passo3 == "azul":
        arredondando_conta_total = 0
        print(f"Parabéns! Você zerou a sua conta total, sua conta total agora é de {arredondando_conta_total}$. ")
      elif passo3 == "vermelha" or passo3 == "amarela":
        conta_total = arredondando_conta_total * 2
        print(f"Infelizmente você abriu a porta e deu de cara com um dragão, você saiu correndo tropeçou e quebrou o braço. Sua conta total agora é de {conta_total}$.")
        jogo2 = input(print("Mas você tem mais uma oportunidade de zerar a sua conta, jogando outro jogo de cara ou coroa. Se você perder, sua conta vai dobrar mais uma vez. Quer jogar ? Sim ou não."))
        if jogo2 == "sim":
          cara_coroa = input("Você quer cara ou coroa? ")
          if random_number == 0:
            resultado_jogo = "cara"
            if resultado_jogo == cara_coroa:
              arredondando_conta_total = 0
              print(f"Parabéns! Você escolher {cara_coroa} e caiu {resultado_jogo}. Você zerou a sua conta, sua conta total agora é de {arredondando_conta_total}")
            else:
              conta_total_final = conta_total * 2
              print(f" Infelizmente você perdeu, você escolheu {cara_coroa} e caiu {resultado_jogo}. Sua conta total agora é de {conta_total_final}$.")
          elif random_number == 1:
            resultado_jogo = "coroa"
            if resultado_jogo == "coroa":
              if resultado_jogo == cara_coroa:
                arredondando_conta_total = 0
                print(f"Parabéns! Você escolher {cara_coroa} e caiu {resultado_jogo}. Você zerou a sua conta, sua conta total agora é de {arredondando_conta_total}")
              else:
                conta_total_final = conta_total * 2
                print(f" Infelizmente você perdeu, você escolheu {cara_coroa} e caiu {resultado_jogo}. Sua conta total agora é de {conta_total_final}$.")  
        else:
          print(f"Sua conta total continua de {conta_total}$.")
    elif passo2 == "nadando":
      conta_total = arredondando_conta_total * 2
      print(f"Infelizmente você fez a escolha errada, você tentou ir nadando cansou no meio do caminho e se afogou. Sua conta total agora é de {conta_total}$.")
      jogo2 = input(print("Mas você tem mais uma oportunidade de zerar a sua conta, jogando outro jogo de cara ou coroa. Se você perder, sua conta vai dobrar mais uma vez. Quer jogar ? Sim ou não."))
      if jogo2 == "sim":
       cara_coroa = input("Você quer cara ou coroa? ")
       if random_number == 0:
         resultado_jogo = "cara"
         if resultado_jogo == cara_coroa:
           arredondando_conta_total = 0
           print(f"Parabéns! Você escolher {cara_coroa} e caiu {resultado_jogo}. Você zerou a sua conta, sua conta total agora é de {arredondando_conta_total}")
         else:
          conta_total_final = conta_total * 2
          print(f"Infelizmente você perdeu, você escolher {cara_coroa} e caiu {resultado_jogo} sua conta total agora é de {conta_total_final}$.")   
       elif random_number == 1:
         resultado_jogo = "coroa"
         if resultado_jogo == cara_coroa:
           arredondando_conta_total = 0
           print(f"Parabéns! Você escolher {cara_coroa} e caiu {resultado_jogo}. Você zerou a sua conta, sua conta total agora é de {arredondando_conta_total}")
         else:
           conta_total_final = arredondando_conta_total * 2
           print(f"Infelizmente você perdeu, você escolher {cara_coroa} e caiu {resultado_jogo}. Sua conta total agora é de {conta_total_final}$.")
      else:
        print(f"Sua conta total continua de {conta_total}$.")
    else:
      print(f"Sua conta total continua de {conta_total}$.")   
  elif passo1 == "esquerda":
    conta_total = arredondando_conta_total * 2
    print(f"Infelizmente você fez a escolha de lado errado, você entrou para a esquerda e caiu em um buraco. Sua conta total agora é de {conta_total}$.")
    jogo2 = input(print("Mas você tem mais uma oportunidade de zerar a sua conta, jogando outro jogo de cara ou coroa. Se você perder, sua conta vai dobrar mais uma vez. Quer jogar ? Sim ou não."))
    if jogo2 == "sim":
       cara_coroa = input("Você quer cara ou coroa? ")
       if random_number == 0:
         resultado_jogo = "cara"
         if resultado_jogo == cara_coroa:
           arredondando_conta_total = 0
           print(f"Parabéns! Você escolheu {cara_coroa} e caiu {resultado_jogo}, você zerou a sua conta. Sua conta agora é de {arredondando_conta_total}")
         else:
          conta_total_final = conta_total * 2
          print(f"Infelizmente você perdeu, você escolheu {cara_coroa}, e caiu {resultado_jogo }. Sua conta total agora é de {conta_total_final}$.")   
       elif random_number == 1:
         resultado_jogo = "coroa"
         if resultado_jogo == cara_coroa:
           arredondando_conta_total = 0
           print(f"Parabéns! Você escolheu {cara_coroa} e caiu {resultado_jogo}, você zerou a sua conta. Sua conta agora é de {arredondando_conta_total}")        
         else:
           conta_total_final = conta_total * 2
           print(f"Infelizmente você perdeu, você escolheu {cara_coroa}, e caiu {resultado_jogo }. Sua conta total agora é de {conta_total_final}$.")
    else:
      print(f"Sua conta total continua de {conta_total}$.")
       
elif jogo == "nao":
  print(f"Sua conta total continua de {arredondando_conta_total}$.")
