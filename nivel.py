nome = input(" digite seu nome: ")
xp = int(input(" digite seu XP: "))

mensagem1 = " O heroi de nome " + nome + " esta no nível ferro "
mensagem2 = " O heroi de nome " + nome + " esta no nível bronze "
mensagem3 = " O heroi de nome " + nome + " esta no nível prata "
mensagem4 = " O heroi de nome " + nome + " esta no nível ouro "
mensagem5 = " O heroi de nome " + nome + " esta no nível platina "
mensagem6 = " O heroi de nome " + nome + " esta no nível Ascendente "
mensagem7 = " O heroi de nome " + nome + " esta no nível Imortal "
mensagem8 = " O heroi de nome " + nome + " esta no nível radiante "

if xp <= 1000:
      print (mensagem1)

if xp >= 1001 and xp <= 2000:
      print (mensagem2)


if xp >= 2001 and xp <= 5000:
      print (mensagem3)

if xp >= 5001 and xp <= 8000:
      print (mensagem4)

if xp >= 8001 and xp <= 9000:
      print (mensagem5)

if xp >= 9001 and xp <= 10000:
      print (mensagem6)

if xp >= 10001 and xp < 11000:
      print (mensagem7)

if xp >= 11000:
      print (mensagem8)









