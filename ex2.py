import math
print("\t CONVERSOR DE MOEDA: \n")

print("SELECIONE A MOEDA A SER CONERTIDA: ")

b = input("REAL PARA DÓLAR -----> \n'1'\n"
          "REAL PARA EURO ------> \n'2'\n"
          "SAIR ----------------> \n'3'\n")


if b == '3':
    print("\t OBRIGADO POR USAR MEU PROGRAMA!!!\n")
    sair2 = input("\t PRECIONE 3 PARA SAIR\n")
    if sair2 == '3':
        exit()

elif b == '1':
    print("\t REAL PARA DÓLAR: \n")

    print("O VALOR DO DÓLAR ATUAL: 5,03 ")
    v = float(input("DIGITE O VALOR EM R$  A SER CONVERTIDO EM DÓLAR: "))

    resp = v / 5.03

    print("\t O VALOR EM DÓLAR: ", resp,"\n")

elif b == '2':
    print("\t REAL PARA EURO: \n")

    print("O VALOR DO EURO ATUAL: 6,14 ")
    s = float(input("DIGITE O VALOR EM R$ A SER CONVERTIDO EM EURO: "))

    reps = s / 6.14 

    print("\t O VALOR EM EURO: ", reps, "\n")












