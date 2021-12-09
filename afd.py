# Programa que lê um AFD com o alfabeto {a, b}
#Autor: Lais de Fátima Sousa Gomes

#recebe uma lista e uma string e retorna TRUE caso esse valor não exista na lista
def naoExiste(lista, str_value):
  saida = True
  for i in lista:
    if i == str_value:
      saida = False
  return saida


#ler todos os estados e retorna uma lista contendo-os
def le_estados(Q):
  est_temp = ''
  while est_temp != 'vazio':
    est_temp = input('digite o nome do estado - para finalizar, escreva o estado vazio como "vazio": ')
    if naoExiste(Q, est_temp):
      Q.append(est_temp)
    else:
      print("Estado já presente na lista. Digite outro!")
  return Q



# Dentre o conjunto de estados Q, essa função define qual é o estado inicial
def estado_inicial(Q):
  q0 = ''
  while (q0 in Q)==False:
    q0 = input("dos estados em Q, qual é o estado inicial? ")
  return q0



def estados_finais(Q):
  F = []
  val = ''
     
  while val != 'fim':
    val = input('digite o nome do estado final - para finalizar, escreva "fim": ')
    if val != 'fim':
      F.append(val)
  return F




def Delta(Q):
  #um dicionário
  func_trans = {}
  for i in Q:
    if i != 'vazio':
      concA = 'valor para o estado '+ i + ' em a'
      valA = input(concA)
      concB = 'valor para o estado '+ i + ' em b'
      valB = input(concB)
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

Q = le_estados([])
qtd_estados  = len(Q)
print(Q)

q0 = estado_inicial(Q)
print(q0)

F = estados_finais(Q)
print(F)

func_trans = Delta(Q)
palavra = input('palavra que se deseja processar: ')

print(afd(func_trans, q0, F, palavra))
