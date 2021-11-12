def main():
        i=1
        soma=0
        z=float(input('Informa quantas avaliações: \n'))
        while i <= z:
            x=float(input(f'Qual a nota da avalição {i} \n'))
            i += 1
            soma+=x   
        media=soma/z
        print("A média é :", media)   
main()
