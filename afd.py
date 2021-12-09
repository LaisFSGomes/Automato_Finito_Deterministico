qtd_estados = input('quantidade de estados: ')

#Estados
Q = []
for i in range(int(qtd_estados)): 
  a = input('digite o estado: ')
  Q.append(a)


#estado inicial e final
q0 = input("dos estados em Q, qual é o estado inicial? ")
a = input("digite a quantidade de estados finais: ")
F = []
for i in range(int(a)):
  b = input("estado final: ")
  F.append(b)

print("estados")
print(Q)
print('estado inicial: ')
print(q0)
print('estado final: ')
print(F)

#função de transição
func_trans = {}
for i in Q:
  conca = 'valor para o estado '+ i + ' em a'
  valA = input(conca)
  concb = 'valor para o estado '+ i + ' em b'
  valB = input(concb)
  func_trans[(i, 'a')] = valA
  func_trans[(i, 'b')] = valB

print(func_trans)

def afd(delta, q0, F, cadeia):
  qA = q0
  for s in cadeia:
    qA = delta[(qA, s)]
  return qA in F

resp = afd(func_trans, q0, F, 'abab')
print(resp)

  
  
