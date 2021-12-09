# Programa que lê um AFD com o alfabeto {a, b}
#Autor: Lais de Fátima Sousa Gomes

#Estados
Q = []
#quando terminar de escrever os estados, digite "vazio" que será o estado vazio
est_temp = ''
while est_temp != 'vazio':
  est_temp = input('digite o nome do estado - para finalizar, escreva o estado vazio como "vazio": ')
  Q.append(est_temp)

qtd_estados  = len(Q)



#estado inicial
q0 = input("dos estados em Q, qual é o estado inicial? ")


#estados finais
F = []
val = ''
while val != 'fim':
    val = input('digite o nome do estado final - para finalizar, escreva "fim": ')
    if val != 'fim':
      F.append(val)




#função de transição
func_trans = {}
for i in Q:
  concA = 'valor para o estado '+ i + ' em a'
  valA = input(concA)
  concB = 'valor para o estado '+ i + ' em b'
  valB = input(concB)
  func_trans[(i, 'a')] = valA
  func_trans[(i, 'b')] = valB


palavra = input('palavra que se deseja processar: ')
qAtual = q0
for i in palavra:
  qAtual = func_trans[(qAtual, i)]

if qAtual in F:
  print('ACEITA')
else:
  print('REJEITA')


  
  
