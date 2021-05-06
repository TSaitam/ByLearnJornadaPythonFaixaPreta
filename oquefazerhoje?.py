horario = float(input("Que horas são? "))
clima = input("Como está o clima lá fora? ")

if horario >= 5 and horario <= 6:
  if clima == 'frio' or clima == 'nublado' or clima == 'chuvoso':
    print("Melhor voltar pra debaixo das cobertas")
  if clima == 'ensolarado' or clima == 'quente' or clima == 'ameno':
     print("Melhor ligar o ventilador")
elif horario >= 6 and horario <= 8:
  if clima == 'frio' or clima == 'nublado' or clima == 'chuvoso':
    print("Um café quentinho seria maravilhoso")
  if clima == 'ensolarado' or clima == 'quente' or clima == 'ameno':
     print("Um banho gelado pra começar o dia")     
elif horario >=8 and horario <= 12:
  if clima == 'frio' or clima == 'nublado' or clima == 'chuvoso':
    print("Aproveitar a manhã livre pra praticar python")
  if clima == 'ensolarado' or clima == 'quente' or clima == 'ameno':
     print("Uma piscina cairia bem")
elif horario >= 12 and horario <= 18:
  if clima == 'frio' or clima == 'nublado' or clima == 'chuvoso':
    print("Aproveitar a tarde livre pra assitir um filminho daora")
  if clima == 'ensolarado' or clima == 'quente' or clima == 'ameno':
     print("Bora chamar o pessoal pra tomar um sorvete gelado")
elif horario >= 18 and horario <= 22:
  if clima == 'frio' or clima == 'nublado' or clima == 'chuvoso':
    print("Pedir uma pizza e um refri seria bem daora")
  if clima == 'fresco' or clima == 'quente' or clima == 'ameno':
     print("Jantar fora ou que tal uma balada?")  
else:
  if clima == 'frio' or clima == 'nublado' or clima == 'chuvoso':
    print("Que tal fazermos uma maratona de algum filme, série ou jogarmos algum jogo?")
  else:
    print("Dormir cedo parece ser uma boa pedida...")
