Inverso = float (input('Ingrese la cantidad que va invertir: '))
interes = float(input('Ingrese el interes anual: '))
tiempo = float(input('Ingrese los años de las inversion: '))

total =str(((Inverso* interes/100))*tiempo)
print('El total de sus interes generados en',tiempo, 'años es de', total)