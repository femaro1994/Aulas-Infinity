def main():
        polu=float(input('Informe a porcentagem de poluição(%): \n'))
        polu=polu/100
        if polu>=0.5:
             print('Todos os grupos devem ser notificados a paralisarem suas atividades')
        elif polu>=0.4:
             print('As indústrias do 1º e 2º grupo são intimadas a suspenderem suas atividades')
        elif polu>=0.3:
             print('As indústrias do 1º grupo são intimadas a suspenderem suas atividades')
        elif polu>=0.25:
             print('Índice de poluição aceitável')
main()