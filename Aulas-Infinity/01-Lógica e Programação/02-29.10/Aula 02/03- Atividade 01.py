def main():
        i=1
        while i<=5:
                ocu=float(input(f'Informe a quantidades de respiradores do Hospital {i}: \n'))
                qnt=float(input(f'Informe a porcentagem de ocupação(%) do Hospital {i}: \n'))
                qnt=qnt/100
                if qnt>0.6 or ocu<50:
                        ocu+=5
                        print('Foram adicionados 5 respiradores',ocu)
                        i+=1
                else:
                        print('Nada aconteceu 😁😁😁😁')
                        i+=1

main()
