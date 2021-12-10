
#                       TEORIA DOS AUTOMATOS E LINGUAGENS FORMAIS
#        Programaque simula o processamento de qualquer AFD sob o alfabeto {a, b}
#
#                             Autor: Lais de Fátima Sousa Gomes
#                                     Matrícula: 504405
#
#
#___________________________________________________________________________________

#ler todos os estados e retorna uma lista contendo-os
def le_estados(Q):
  est_temp = ''
  while est_temp != 'vazio':
    est_temp = input('digite o nome do estado - para finalizar, escreva o estado vazio como "vazio": ')
    if (est_temp in Q) == False:
      Q.append(est_temp)
    elif (est_temp in Q) == True:
      print("Estado já presente na lista. Digite outro!")
  return Q


# Dentre o conjunto de estados Q, essa função define qual é o estado inicial
def estado_inicial(Q):
  q0 = ''
  while (q0 in Q)==False:
    q0 = input("Dos estados em Q, qual é o estado inicial? ")
    if (q0 in Q)== False:
      print("Digite um estado presente em Q. Tente novamente!")
  return q0

# define o estados finais
def estados_finais(Q):
  F = []
  val = ''
     
  while val != 'fim':
    val = input('digite o nome do estado final - para finalizar, escreva "fim": ')
    
    if (val in Q) or val == 'fim':
      if val != 'fim':
        F.append(val)
    elif (val in Q) == False:
      print("Estado digitado não está presente em Q, tente outro")

  return F


def Delta(Q):
  #um dicionário
  func_trans = {}
  for i in Q:
    if i != 'vazio':
      valA = input('valor para o estado '+ i + ' em a: ')
      valB = input('valor para o estado '+ i + ' em b: ')
      func_trans[(i, 'a')] = valA
      func_trans[(i, 'b')] = valB
  return func_trans



def afd(delta, q0, F, palavra):
  qAtual = q0
  for i in palavra:
    qAtual = delta[(qAtual, i)]
  if (qAtual in F):
    return "ACEITA"
  else:
    return "REJEITA"

# ________________________________________________________________________________________________________

#lendo o conjunto de estados
Q = le_estados([])
print(Q)
print('\n')
#definindo os estados iniciais e finais
q0 = estado_inicial(Q)
print(q0)
F = estados_finais(Q)
print(F)
print('\n')

#lendo a função de transição de estados
func_trans = Delta(Q)
print('funcao de transiçao')
print(func_trans)
print("--")

#Testando a palavra no AFD:
palavra = ''
while palavra != "sair":
  print("\nPara terminar, digite 'sair'")
  palavra = input('palavra que se deseja processar: ')
  if palavra != 'sair':
    print(afd(func_trans, q0, F, palavra))
