a1 = int(input("Valor inicial?: "))
n = int(input("Número de termos?: "))
q = int(input("Qual a razão? Sendo essa maior ou igual a 2: "))
sn = (a1*(q**n -1) / (q-1))
print ("Sn: ", sn)
