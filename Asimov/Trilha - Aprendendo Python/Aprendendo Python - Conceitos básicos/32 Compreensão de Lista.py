valores = list(range(10))

#maiores_que_cinco = list()

#for valor in valores:
#   if valor > 5:
#        maiores_que_cinco.append(valor)

maiores_que_cinco = [valor for valor in valores if valor > 5]

print(maiores_que_cinco)