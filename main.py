#importações
import time as t

# Declarando variavel de pontos
pontos = 0

#inicio do quiz 
print('''
    Este quiz tem como objetivo, testar seus conhecimentos sobre a Era Napoleônica. \nAo final, descubra o quanto entende do assunto.
''')

t.sleep(3)

#PERGUNTA 1
print('O governo napoleônico durou 15 anos e pode ser dividido em dois períodos distintos. Quais são?')

print('\n[A] Consulado e Império.')
print('[B] Consulado e Revolução Francesa.')
print('[C] Império e República.')
print('[D] Consolado e República.')

resposta = str(input('\nInsira a resposta...   '))
t.sleep(2)
if(resposta == 'A' or resposta == 'a'):
    print('\n Parabéns! Você acertou!')
    pontos = pontos + 20
    print(f'\n Você tem {pontos} pontos agora')
else:
    print('\n Ops. Não foi desta vez')
    print('\n a resposta certa era: A')

#PERGUNTA 2
print('\nDurante o longo governo napoleônico, Napoleão reaproximou o estado francês da Igreja.\n Reconhecendo assim que religião?')

print('\n[A] Ateísmo.')
print('[B] Politeísmo.')
print('[C] Catolicismo.')
print('[D] Candomblé.')

resposta2 = str(input('Insira a resposta...   '))
t.sleep(2)
if(resposta2 == 'C' or resposta2 == 'c'):
    print('\n Parabéns! Você acertou!')
    pontos = pontos + 20
    print(f'\n Você tem {pontos} pontos agora')
else:
    print('\n Ops. Não foi desta vez')
    print('\n a resposta certa era: C')

#PERGUNTA 3
print('\n Napoleão assumiu o governo francês tendo que cargo?')

print('\n[A] Primeiro cônsul.')
print('[B] Rei.')
print('[C] Presidente.')
print('[D] Imperador.')

resposta3 = str(input('Insira a resposta...   '))
t.sleep(2)
if(resposta3 == 'A' or resposta3 == 'a'):
    print('\n Parabéns! Você acertou!')
    pontos = pontos + 20
    print(f'\n Você tem {pontos} pontos agora')
else:
    print('\n Ops. Não foi desta vez')
    print('\n a resposta certa era: A')

#PERGUNTA 4
print('\n "Napoleão havia conquistado grande parte da Europa, exceto sua maior adversária.", este enunciado\n esta referindo-se à que país?')

print('\n[A] Inglaterra.')
print('[B] Prússia.')
print('[C] Rússia.')
print('[D] Áustralia.')

resposta4 = str(input('Insira a resposta...   '))
t.sleep(2)
if(resposta4 == 'A' or resposta4 == 'a'):
    print('\n Parabéns! Você acertou!')
    pontos = pontos + 20
    print(f'\n Você tem {pontos} pontos agora')
else:
    print('\n Ops. Não foi desta vez')
    print('\n a resposta certa era: A')

#PERGUNTA 5
print('\n O que decretava o Bloqueio Continental?')

print('\n[A] Proibia o tráfico de escravos da África ao Brasil.')
print('[B] Proibia a comercialização de produtos e bens com os ingleses.')
print('[C] Proibia a venda de materiais de guerra aos ingleses e aos prussianos.')
print('[D] Proibia a comecialização de produtos e bens com os russos.')

resposta5 = str(input('Insira a resposta...   '))
t.sleep(2)
if(resposta5 == 'B' or resposta5 == 'b'):
    print('\n Parabéns! Você acertou!')
    pontos = pontos + 20
    print(f'\n Você tem {pontos} pontos agora')
else:
    print('\n Ops. Não foi desta vez')
    print('\n a resposta certa era: B')

t.sleep(2)
print('\nConfira a tabela de notas a seguir...')

print('\n0 pontos: Ruim!')
print('\n20 pontos: Bom!')
print('\n40 pontos: Medio!')
print('\n60 pontos: Ótimo!')
print('\n100 pontos: exelente!')