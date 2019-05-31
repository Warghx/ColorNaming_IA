#el número de pares de puntos que puedes unir con una línea, dependiendo de los centroides (K). ##
##k: numero de cluster, matriz[Scurent][3]: numero de puntos en el cluster, cen:centro del cluster, puntos : array con los puntos y su localizacion,
## 	mCentroides:array con los centroides y su posicion

from scipy.spatial import distance

def  Fisher(k,matriz,puntos,mCentroides):
##Calculamos normalizador para contrarestar el crecimiento del denominador
Normalizador = (k-1)/2

Numerador = Numerador(k,matriz,puntos)
Denominador = Denominador(mCentroides,k)

Fisher = Numerador/Denominador
return Fisher
##Funcion para calcular la distancia media entre todos los puntos de un cluster, necesitamos posicion de los clusters y que puntos estan en cada cluster

def sumatDistMed(k,puntos,matriz)
i=0
##calculamos distancia de todos los puntos de un cluster, hacemos la media con los puntos del cluster y finalmente sumatorio para todos los clusters
for i in range(k)
	for ii in range(puntos)
		dist = distance.euclidean(puntos[ii],centroide[i]])+ dist ##calculamos distancia entre los puntos de un cluster al centroide
	
	Distmedia[i]= dist/matriz[i][3]
	
for b in range(k)
	sumadistmed= Distmedia[b]+sumadistmed

return sumadistmed
##Funcion que calcula el numerador 
def Numerador(k,matriz,puntos)
i=1
dist = sumatDistMed(k,puntos,matriz)
for i in range k
	num=(1/m)* dist+num
numerador= Normalizador* num
return numerador

##la suma de todas las distancias entre pares de centroides que puedes obtener con K centroides.
def Denominador(mCentroides,k)
i=0
z=0
for i in range(mCentroides)
	for z in range(mCentroides)
		dist = distance.euclidean(mCentroides[i],mCentroides[z+1]])+ dist
		
DistClusterMedia= dist/k
return DistClusterMedia
	
	
	




		
		
		
