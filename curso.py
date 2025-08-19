peso = float(input("Qual seu peso(kg)?"))
altura = float(input("Qual sua altura(m)?"))

imc = peso / (altura * altura)

print(f"seu IMC é {imc:.2f}")