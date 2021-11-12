# Guardar um número sorteado entre 1 e 10 e pedir para que o usuário tente acertar este valor. 
# Avise a ele se o número que ele informou é maior ou menor do número sorteado e mostre a mensagem quando ele acertar!
# Faça antes do código um fluxograma para estruturar melhor o raciocínio.
#Para sortear um número entre 1 e 10, utilize o seguinte comando: random.randrange(1,10)

# def main():
#         i=1
#         while i<=5:
#                 ocu=float(input('Informe a quantidades de respiradores: \n'))
#                 qnt=float(input('Informe a porcentagem de ocupação(%): \n'))
#                 qnt=qnt/100
#                 if qnt>0.6 or ocu<50:
#                         ocu+=5
#                         print('Foram adicionados 5 respiradores',ocu)
#                         i+=1
#                 else:
#                         print('Nada aconteceu 😁😁😁😁')
#                         i+=1

# main()

def main():
        import random
        i= random.randrange(1,10)
        print('\n O número é ',i)
        print("\n Escreva um número de 1 a 10 \n")
        x=int(input())
        while x!=i:
            if i>x:
                print("\nErrou cara Número maior que o sorteado 🤣🤣😂\n")
                x=int(input('\nEscreva um número de 1 a 10 de novo \n'))
            else:
                print("\nErrou cara Número menor que o sorteado 🤣🤣😂\n")
                x=int(input('\nEscreva um número de 1 a 10 de novo \n'))
            
        print("\n Acertou 😁😁😀")

            
       

main()
