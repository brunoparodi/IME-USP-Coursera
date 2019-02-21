segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))

horas = segundos // 3600
dias = horas // 24
horas_final = horas % 24
seg_restante = segundos % 3600
minutos = seg_restante // 60
seg_final = seg_restante % 60

print(dias,'dias,',horas_final,'horas,',minutos,'minutos e',seg_final,'segundos ')
