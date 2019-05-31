import math
import copy

def DistEuclidiana(p1 ,p2):
	return math.sqrt ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)


def kmeans (X, K, centroides):
	b = 0
	dcen=[]# distancia entre todos los pares de puntos para un centroide
	#matriz auxiliar
	mAux = [-1] * K
	for j in range(K):
		mAux[j] = [-1] * 4
	
	#matriz para almacenar las coordenadas de los centroides
	mCentroides = [0] * K
	for j in range(K):
		dcen.append(0)		#creamos tantas posiciones como centroides tenemos
		mCentroides[j] = [0] * 4

	for j in range(K):
		for jj in range(3):
			mCentroides[j][jj]=centroides[j][jj] 


	while ((cmp(mCentroides,mAux))!=0):   #si los centroides son diferente a los nuevos	
		b=b+1
		for j in range(K):
			for z in range(len(mAux[j])):
				mAux[j][z] = round(mCentroides[j][z],2)
		matriz = [0] * K
		for i in range(K):
			matriz[i] = [0] * 4    			

		for n in range(len(X)):
			aux = [[10**10],[0]]
			cCurrent = -1
			punto = X[n]			
			for f in range(K):				
				dist = DistEuclidiana(punto,mCentroides[f])
				if aux[0] > dist:				
					aux[0] = dist
					aux[1] = punto
					cCurrent = f
					dcen[f]+= dist					
			#almacenar valores RGB y numero de puntos en la fila (K) correspondiente en la matriz
			matriz[cCurrent][0] += aux[1][0]	#R
			matriz[cCurrent][1] += aux[1][1]	#G
			matriz[cCurrent][2] += aux[1][2]	#B	
			matriz[cCurrent][3] += 1 			#numero de puntos 

		#y a continuacion calcular nueva coordenada de centroide
		for o in range(K):
			if matriz[o][3] > 0:
				mCentroides[o][0] = round(matriz[o][0]/matriz[o][3],2)
				mCentroides[o][1] = round(matriz[o][1]/matriz[o][3],2)
				mCentroides[o][2] = round(matriz[o][2]/matriz[o][3],2)
				mCentroides[o][3] = matriz[o][3]
	return mCentroides, K, dcen