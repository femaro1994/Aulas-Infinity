# Desenvolva um algoritmo que solicite o preço de três produtos e informe qual produto deve ser comprado, sabendo que a decisão é sempre pelo mais barato.
def main():
    p1=float(input("Qual o preço 1: \n"))
    p2=float(input("Qual o preço 2: \n"))
    p3=float(input("Qual o preço 3: \n"))
    if(p1<=p2)and(p1<=p3):
     print("produto 1 é o mais barato")
    elif(p2<=p1)and(p2<=p3):
     print("produto 2 é o mais barato")
    elif(p3<=p2)and(p3<=p2):
     print("produto 3 é o mais barato")
main()