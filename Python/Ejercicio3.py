peso = float(input('Cuál es tu peso en kg? '))
altura = float(input('Cuál es tu estatura en metros?'))
imc = peso / (altura**2)

print(f'Tu índice de massa corporal es {imc:.2f}')
