total_segs = int(input("Informe os segudos que deseja converter: "))

horas = total_segs // 3600
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(horas,"horas, ",minutos,"minutos, ",segs_restantes_final,"segudos.")