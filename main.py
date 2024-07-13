salario = float(input("informe o salário: "))

if salario <= 3000:
    print("Você é o programador Junior")
elif salario > 3000 and salario <= 6000:
    print("Você é o programador pleno")
elif salario > 6000 and salario <= 15000:
    print("Você é o programador senior")
else:
    print("Você é o gerente de projetos")

