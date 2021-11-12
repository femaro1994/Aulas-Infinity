def main():
        bran = float(input('Informa o total de votos brancos \n'))
        nul =  float(input('Informa o total de votos nulos \n'))
        vali=  float(input('Informa o total de votos validos \n'))
        t= bran+nul+vali
        print('\n % votos brancos:',(bran/t)*100,'\n')
        print('\n % votos nulos:',(nul/t)*100,'\n')
        print('\n % votos brancos:',(vali/t)*100,'\n')
main()