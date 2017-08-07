import random
class Gameplay:
	def __init__(self,k):
		self._score=k
	def checkRowfull(self,arr,i):
		for j in range(1,33):
		    if(arr[i][j]==' '):
			return -1
		return 1
	def checkRowempty(self,arr,i):
		for j in range(1,33):
		    if(arr[i][j]!=' '):
			return -1
		return 1
	def getscore(self):
		return self._score


	def updatescore(self,k):
		self._score+=k
		return self._score



	def selectpiece(self):	
		k=random.random()
		k=k*10000
		k=int(k)
		return k%6
