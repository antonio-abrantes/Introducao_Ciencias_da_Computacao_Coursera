total_segundos = int(input("Numero de segundos: "))

horas = total_segundos // 3600
segs_restantes = total_segundos % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(horas, "horas,", minutos, "minutos e", segs_restantes_final, "segundos")