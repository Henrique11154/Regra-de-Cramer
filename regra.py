#Regra de Cramer
import numpy as np
#Cria uma função que devolve os resultados
def regra_de_cramer(i,j): #i = numero de equações; j = numero de incognitas
   eq = np.random.randint(1,size=(i,i))
   Ti = np.random.randint(1,size=(i,1)) 
   if j > i:
    print("Não é possivel aplicar a regra pois o sistema não possui solução")