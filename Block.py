
class Block():
	def rotate(self,i,j,arr,label,dup,pos,ss):
		if(label==0):
		    rty=6
		else:
		    rty=0
	 	if((arr[pos[ss+rty][0][0]+i-1][pos[ss+rty][0][1]+j]==' ' and arr[pos[ss+rty][1][0]+i-1][pos[ss+rty][1][1]+j]==' ' )and (arr[pos[ss+rty][2][0]+i-1][pos[ss+rty][2][1]+j]==' ' and arr[pos[ss+rty][3][0]+i-1][pos[ss+rty][3][1]+j]==' ')):
			if(rty==6):	
				dup[pos[ss][0][0]+i-1][pos[ss][0][1]+j]=' '
				dup[pos[ss][1][0]+i-1][pos[ss][1][1]+j]=' '
				dup[pos[ss][2][0]+i-1][pos[ss][2][1]+j]=' '
				dup[pos[ss][3][0]+i-1][pos[ss][3][1]+j]=' '	
				dup[pos[ss+rty][0][0]+i-1][pos[ss+rty][0][1]+j]='x' 
				dup[pos[ss+rty][1][0]+i-1][pos[ss+rty][1][1]+j]='x' 
				dup[pos[ss+rty][2][0]+i-1][pos[ss+rty][2][1]+j]='x'
				dup[pos[ss+rty][3][0]+i-1][pos[ss+rty][3][1]+j]='x'
			else:
				dup[pos[ss+6][0][0]+i-1][pos[ss+6][0][1]+j]=' '
				dup[pos[ss+6][1][0]+i-1][pos[ss+6][1][1]+j]=' '
				dup[pos[ss+6][2][0]+i-1][pos[ss+6][2][1]+j]=' '
				dup[pos[ss+6][3][0]+i-1][pos[ss+6][3][1]+j]=' '	
				dup[pos[ss][0][0]+i-1][pos[ss][0][1]+j]='x' 
				dup[pos[ss][1][0]+i-1][pos[ss][1][1]+j]='x' 
				dup[pos[ss][2][0]+i-1][pos[ss][2][1]+j]='x'
				dup[pos[ss][3][0]+i-1][pos[ss][3][1]+j]='x'
			return 1
		return -1
	def moveLeft(self,i,j,arr,label,dup,rc,pos,ss):
		if(rc==0):
		    rtc=0
		else:
		    rtc=6
	 	if((arr[pos[ss+rtc][0][0]+i-1][pos[ss+rtc][0][1]+j]==' ' and arr[pos[ss+rtc][1][0]+i-1][pos[ss+rtc][1][1]+j]==' ' )and (arr[pos[ss+rtc][2][0]+i-1][pos[ss+rtc][2][1]+j]==' ' and arr[pos[ss+rtc][3][0]+i-1][pos[ss+rtc][3][1]+j]==' ')):
			dup[pos[ss+rtc][0][0]+i-1][pos[ss+rtc][0][1]+j+label]=' '
			dup[pos[ss+rtc][1][0]+i-1][pos[ss+rtc][1][1]+j+label]=' '
			dup[pos[ss+rtc][2][0]+i-1][pos[ss+rtc][2][1]+j+label]=' '
			dup[pos[ss+rtc][3][0]+i-1][pos[ss+rtc][3][1]+j+label]=' '	
			dup[pos[ss+rtc][0][0]+i-1][pos[ss+rtc][0][1]+j]='x' 
			dup[pos[ss+rtc][1][0]+i-1][pos[ss+rtc][1][1]+j]='x' 
			dup[pos[ss+rtc][2][0]+i-1][pos[ss+rtc][2][1]+j]='x'
			dup[pos[ss+rtc][3][0]+i-1][pos[ss+rtc][3][1]+j]='x'
			return 1
		return -1
	def moveRight(self,i,j,arr,label,dup,rc,pos,ss):
		if(rc==0):
		    rtc=0
		else:
		    rtc=6
	 	if((arr[pos[ss+rtc][0][0]+i-1][pos[ss+rtc][0][1]+j]==' ' and arr[pos[ss+rtc][1][0]+i-1][pos[ss+rtc][1][1]+j]==' ' )and (arr[pos[ss+rtc][2][0]+i-1][pos[ss+rtc][2][1]+j]==' ' and arr[pos[ss+rtc][3][0]+i-1][pos[ss+rtc][3][1]+j]==' ')):
			dup[pos[ss+rtc][0][0]+i-1][pos[ss+rtc][0][1]+j+label]=' '
			dup[pos[ss+rtc][1][0]+i-1][pos[ss+rtc][1][1]+j+label]=' '
			dup[pos[ss+rtc][2][0]+i-1][pos[ss+rtc][2][1]+j+label]=' '
			dup[pos[ss+rtc][3][0]+i-1][pos[ss+rtc][3][1]+j+label]=' '	
			dup[pos[ss+rtc][0][0]+i-1][pos[ss+rtc][0][1]+j]='x' 
			dup[pos[ss+rtc][1][0]+i-1][pos[ss+rtc][1][1]+j]='x' 
			dup[pos[ss+rtc][2][0]+i-1][pos[ss+rtc][2][1]+j]='x'
			dup[pos[ss+rtc][3][0]+i-1][pos[ss+rtc][3][1]+j]='x'
			return 1
		return -1
	def draw(self):
		print self.selectpiece()
		return 1
