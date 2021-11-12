#Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não. Para estar em condições, um dos seguintes requisitos deve ser satisfeito: 
#1) Ter no mínimo 65 anos de idade. 
#2) Ter trabalhado no mínimo 30 anos. 
#3) Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos. 
#Com base nas informações acima, faça um algoritmo que leia: o número do empregado (código), o ano de seu nascimento e o ano de seu ingresso na empresa.
#O programa deverá escrever a idade e o tempo de trabalho do empregado e a mensagem 'Requerer aposentadoria' ou 'Não requerer'.
# *Nasc=1961 2021-1961=60
# *Nasc=1956 2021-1956=65
# *Traba=1991 2021-1991=30
# *Traba=1991 2021-1996=25 

def main():
            from datetime import date # importação da biblioteca caléndario
            ano_atual=int(date.today().strftime('%Y'))# date.today().strftime('%Y'), pega a data atual,e depois  o strtime transforma em sting(%Y pega o ano)   
            # o int na frente trans forma a variavel sring em inteiro
            #datetime.date.time.now().year
            
            print("Ano Atual: ",ano_atual,"\n")
            
            cod=int(input("Qual seu código de menbro da empresa: \n"))
            ano_nas=int(input("Qual o ano do seu nascimento: \n"))
            ano_emp=int(input("Qual o ano de seu ingresso: \n"))
            delt_nas=ano_atual-ano_nas
            delt_emp=ano_atual-ano_emp
            if delt_nas>=65 or delt_emp>=30:
                print(cod," Aposentado condições  1 ou 2 cumpridas, aposentado 😁😁😀")
            elif delt_nas>=60 and delt_emp>=25:
                print(cod," Aposentado condição  3 cumprida, aposentado 😗😗😮")     
            else:
                print(cod," Vá trabalhar, This is Brazil")    
main()
