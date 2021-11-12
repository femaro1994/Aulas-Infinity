def main():
    t1=input("Informe o nome do time 1: \n")
    t2=input("Informe o nome do time 2: \n")
    TA=int(input('Informe Quantidades de Gols do ', t1 ,': \n'))
    TB=int(input('Informe Quantidades de Gols do ', t2 ,': \n'))
    if TA>TB:
        print('O Time '+t1+' ganhou')
    elif TB>TA:
        print('O Time '+t2+' ganhou')
    elif TA==TB:
        print('Empate 😁😁😀')
main()