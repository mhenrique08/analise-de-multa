#Projeto - Lógica de programação básica

velocidade_do_motorista = int(input('A velocidade máxima permitida é de 80 km/h. Qual foi a sua velocidade?'))    
velocidade_maxima = 80

if velocidade_do_motorista >80 and velocidade_do_motorista <=90:
    print ('Você tomou uma multa leve (50R$)')

elif velocidade_do_motorista >90 and velocidade_do_motorista <=100:
    print ('Você tomou uma multa grave (150R$)')

elif velocidade_do_motorista>100 and velocidade_do_motorista<=150:
    print ('Você tomou uma multa gravíssima (300R$)')

elif velocidade_do_motorista >150:
    print ('Você perdeu sua carteira de motorista + Multa de 400R$)')

else:
    print ('Não houve multa, parabéns!')
