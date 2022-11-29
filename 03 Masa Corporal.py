peso=float(input('Inserta tu peso en kg: '))
estatura=float(input('Inserta tu estatura en metros: '))
masa_corporal=peso*estatura
rounded_masa_corporal=round(masa_corporal,2)
print('Tu indice de masa corporal es:' ,rounded_masa_corporal)