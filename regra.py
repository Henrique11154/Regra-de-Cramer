#Regra de Cramer
import numpy as np
#Cria uma função que devolve os resultados
def regra_de_cramer(i,j): #i = numero de equações; j = numero de incognitas
   eq = np.random.randint(1,size=(i,i))   #matiz de equações
   Ti = np.random.randint(1,size=(i,1))   #Termo independente
   inc = []                               #incognitas
   Dx = Dy = 1
   if j > 3 or j < 2 and i > 3 or i < 2:
      print("Infelizmente isso não sera possivel")
   if j > i:
      print("Não é possivel aplicar a regra pois o sistema não possui solução")
   for d in range(i):      #pedindo os números da equação
      for o in range(i):  
         eq[d,o] = int(input("digite os números que multiplicam as icognitas: "))
         print("")
   for d in range(j):
      inc.append(input("Digite as incognitas: "))
      print("")
   for d in range(i):
      Ti[d,0] = int(input("digite os termos independentes: "))
   Det =[]   #Determinante
   d = 0
   #o resto da determinate
   if i == 3:
      Det2 = []
      for l in range(i):
         if l <i-1:
            Det2.append(int(eq[l,l+1]))
         else:
            l = 0
            Det2.append(int(eq[i-1,l]))

      Det3 = []
      for d in range(i-1):
         if d <i-2:
            Det3.append(int(eq[d,d+2]))
         else:
            d = 2
            for r in range(d):
               Det3.append(int(eq[i-d,r]))
               d-=1
   DetInv = []   #Determinante contraria
   if i == 3:
      DetInv2 = []
      for d in range(i):
         if d == 0:
            DetInv2.append(int(eq[d,d]))
         else:
            DetInv2.append(int(eq[d,i-d]))

      DetInv3 = []
      for d in range(i):
         if d == 0:
            DetInv3.append(int(eq[d,d+1]))
         elif d == 1:
            DetInv3.append(int(eq[d,d-1]))
         else:
            DetInv3.append(int(eq[d,d]))
   
   cont = 0       #contador
   u = 0          #Termo aleatorio que eu criei
   k= 0           #Termo aleatorio que eu criei
   
   #três primeiros números da diagonal
   for d in range(i):         
      Det.append(int(eq[d,d]))
   
   #pegando os números da determinante contraria
   for d in range(i):
      if d < 1:
         DetInv.append(int(eq[d,i-1]))
      else:
         DetInv.append(int(eq[d,i-d-1]))

   if i == 2:
      for m in range(1):
         Dx = (int(Ti[m,0])*int(eq[m+1,m+1])) - (int(eq[m,m+1])*int(Ti[m+1,0]))
         Dy = (int(Ti[m+1,0])*int(eq[m,m])) - (int(Ti[m,0])*int(eq[m+1,m]))
   elif i == 3:
      Detx = []
      Detx2 = []
      Detx3 = []
      Dety = []
      Dety2 = []
      Dety3 = []
      Detz = []
      Detz2 = []
      Detz3 = []
      for l in range(i):
         if l < 1:
            Detx.append(int(Ti[l,l]))
            Detx2.append(int(eq[l,l+1]))
            Detx3.append(int(eq[l,l+2]))

            Dety.append(int(eq[l,l]))
            Dety2.append(int(Ti[l,l]))
            Dety3.append(int(eq[l,l+2]))

            Detz.append(int(eq[l,l]))
            Detz2.append(int(eq[l,l+1]))
            Detz3.append(int(Ti[l,l]))
         elif l == 1:
            Detx.append(int(eq[l,l]))
            Detx2.append(int(eq[l,l+1]))
            Detx3.append(int(Ti[l,0]))

            Dety.append(int(Ti[l,0]))
            Dety2.append(int(eq[l,l+1]))
            Dety3.append(int(eq[l,l-1]))
            
            Detz.append(int(eq[l,l]))
            Detz2.append(int(Ti[l,0]))
            Detz3.append(int(eq[l,l-l]))
         else:
            Detx.append(int(eq[l,l]))
            Detx2.append(int(Ti[l,0]))
            Detx3.append(int(eq[l,l-1]))

            Dety.append(int(eq[l,l]))
            Dety2.append(int(eq[l,l-l]))
            Dety3.append(int(Ti[l,0]))

            Detz.append(int(Ti[l,0]))
            Detz2.append(int(eq[l,l-l]))
            Detz3.append(int(eq[l,l-1]))
   
   d=0
   if i == 3:
      DetInvx = []
      DetInvx2 = []
      DetInvx3 = []
      DetInvy = []
      DetInvy2 = []
      DetInvy3 = []
      DetInvz = []
      DetInvz2 = []
      DetInvz3 = []
      for d in range(i):
         if d < 1:
            DetInvx.append(int(eq[d,d+2]))
            DetInvx2.append(int(Ti[d,d]))
            DetInvx3.append(int(eq[d,d+1]))

            DetInvy.append(int(eq[d,d+2]))
            DetInvy2.append(int(eq[d,d]))
            DetInvy3.append(int(Ti[d,d]))

            DetInvz.append(int(Ti[d,d]))
            DetInvz2.append(int(eq[d,d]))
            DetInvz3.append(int(eq[d+2,d]))
         elif d == 1:
            DetInvx.append(int(eq[d,d]))
            DetInvx2.append(int(eq[d,d+1]))
            DetInvx3.append(int(Ti[d,0]))

            DetInvy.append(int(Ti[d,0]))
            DetInvy2.append(int(eq[d,d+1]))
            DetInvy3.append(int(eq[d,d-1]))

            DetInvz.append(int(eq[d,d]))
            DetInvz2.append(int(Ti[d,0]))
            DetInvz3.append(int(eq[d,d-1]))
         else:
            DetInvx.append(int(Ti[d,0]))
            DetInvx2.append(int(eq[d,d-1]))
            DetInvx3.append(int(eq[d,d]))

            DetInvy.append(int(eq[d,d-d]))
            DetInvy2.append(int(Ti[d,0]))
            DetInvy3.append(int(eq[d,d]))

            DetInvz.append(int(eq[d,d-d]))
            DetInvz2.append(int(eq[d,d]))
            DetInvz3.append(int(Ti[d,0]))

   #calcular a os valores das variaveis
   if i == 2:
      while cont < 1:  
         u = Det[cont]*Det[cont+1]
         k = DetInv[cont]*DetInv[cont+1]
         cont+=1
      DetTotal = u-k
      print("{}:{}\n{}:{}".format(inc[0],Dx/DetTotal,inc[1],Dy/DetTotal))
   if i == 3:
      while cont < 1:
         u = (Det[cont]*Det[cont+1]*Det[cont+2])+(Det2[cont]*Det2[cont+1]*Det2[cont+2])+(Det3[cont]*Det3[cont+1]*Det3[cont+2])
         k = (DetInv[cont]*DetInv[cont+1]*DetInv[cont+2])+(DetInv2[cont]*DetInv2[cont+1]*DetInv2[cont+2])+(DetInv3[cont]*DetInv3[cont+1]*DetInv3[cont+2])
         Dx = (Detx[cont]*Detx[cont+1]*Detx[cont+2])+(Detx2[cont]*Detx2[cont+1]*Detx2[cont+2])+(Detx3[cont]*Detx3[cont+1]*Detx3[cont+2])-((DetInvx[cont]*DetInvx[cont+1]*DetInvx[cont+2])+(DetInvx2[cont]*DetInvx2[cont+1]*DetInvx2[cont+2])+(DetInvx3[cont]*DetInvx3[cont+1]*DetInvx3[cont+2]))
         Dy = (Dety[cont]*Dety[cont+1]*Dety[cont+2])+(Dety2[cont]*Dety2[cont+1]*Dety2[cont+2])+(Dety3[cont]*Dety3[cont+1]*Dety3[cont+2])-((DetInvy[cont]*DetInvy[cont+1]*DetInvy[cont+2])+(DetInvy2[cont]*DetInvy2[cont+1]*DetInvy2[cont+2])+(DetInvy3[cont]*DetInvy3[cont+1]*DetInvy3[cont+2]))
         Dz = (Detz[cont]*Detz[cont+1]*Detz[cont+2])+(Detz2[cont]*Detz2[cont+1]*Detz2[cont+2])+(Detz3[cont]*Detz3[cont+1]*Detz3[cont+2])-((DetInvz[cont]*DetInvz[cont+1]*DetInvz[cont+2])+(DetInvz2[cont]*DetInvz2[cont+1]*DetInvz2[cont+2])+(DetInvz3[cont]*DetInvz3[cont+1]*DetInvz3[cont+2]))
         cont+=1
      DetTotal = u-k
      print("{}:{}\n{}:{}\n{}:{}".format(inc[0],Dx/DetTotal,inc[1],Dy/DetTotal,inc[2],Dz/DetTotal))


print("--------------- REGRA DE CRAMER --------------------\n")
print("Por favor apenas digite uma matriz 2x2 ou 3x3")
i = int(input("Digite o número de equações: "))
print("")
j = int(input("Agora o número de icognitas: "))
regra_de_cramer(i,j)
