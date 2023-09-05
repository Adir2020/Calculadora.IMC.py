#Cálculo do Índice de Massa Corporal

nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura:(m) "))
peso = float(input("Digite seu peso:(kg) "))

imc = peso / (altura*altura)

print('%s, seu imc é de {:.1f} e voçê está com'.format(imc) %(nome))

if   (imc < 18.5):
    print("baixo peso")
elif (imc < 24.9):
    print("peso normal")
elif (imc < 29.9):
    print("excesso de peso")
elif (imc < 34.9):
    print("obesidade")
elif (imc > 35):
    print("obesidade extrema")    