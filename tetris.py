import curses
import random
import time
import os
from Gameplay import *
from Block import *
i=0
arr=[]
dup=[]
for i in range(0,32):
	arr.append([])
for i in range(0,32):
	for j in range(0,34):
		arr[i].append(' ') 
for i in range(0,32):
	dup.append([])
for i in range(0,32):
	for j in range(0,34):
		dup[i].append(' ') 
for i in range(1,33,2):
    arr[0][i]='-'
    arr[0][i+1]='-'
    arr[31][i+1]='-'
    arr[31][i]='-'

for i in range(1,31,2):
    arr[i][0]='|'
    arr[i+1][0]='|'
    arr[i][33]='|'
    arr[i+1][33]='|'
arr[0][33]='+'
arr[31][33]='+'
arr[0][0]='+'
arr[31][0]='+'
pos=[[[1,14],[1,15],[2,15],[2,16]],[[1,14],[1,15],[1,16],[1,17]],[[1,14],[1,15],[1,16],[2,16]],[[1,14],[1,15],[2,14],[2,15]],[[1,14],[1,15],[1,16],[2,15]],[[1,14],[2,14],[2,15],[3,15]],[[1,14],[1,15],[2,13],[2,14]],[[1,14],[2,14],[3,14],[4,14]],[[1,14],[2,14],[2,15],[2,16]],[[1,14],[1,15],[2,14],[2,15]],[[1,14],[2,13],[2,14],[2,15]],[[1,14],[2,13],[2,14],[3,13]]]
def dupprint(dup):
	for j in range(0,32):
		for i in range(0,34):
    			screen.addch(j,i,dup[j][i])
			screen.refresh()
def dupprint1():
	for j in range(0,32):
		for i in range(0,34):
    			screen.addch(j,i,' ')
			screen.refresh()
class Board(Gameplay,Block):
	def checkPiecepos(self,i,j,ss,arr,rc):
		if(rc==0):
		    rtc=0
		else:
		    rtc=6
		if((arr[pos[ss+rtc][0][0]+i-1][pos[ss+rtc][0][1]+j]==' ' and arr[pos[ss+rtc][1][0]+i-1][pos[ss+rtc][1][1]+j]==' ' )and (arr[pos[ss+rtc][2][0]+i-1][pos[ss+rtc][2][1]+j]==' ' and arr[pos[ss+rtc][3][0]+i-1][pos[ss+rtc][3][1]+j]==' ')):
		    return 1
		else:
		    return -1



	def fillPiecePos(self,i,j,ss,dup,rc):
		if(rc==0):
		    rtc=0
		else:
		    rtc=6
		if(i!=1):
			dup[pos[ss+rtc][0][0]+i-2][pos[ss+rtc][0][1]+j]=' '
			dup[pos[ss+rtc][1][0]+i-2][pos[ss+rtc][1][1]+j]=' '
			dup[pos[ss+rtc][2][0]+i-2][pos[ss+rtc][2][1]+j]=' '
			dup[pos[ss+rtc][3][0]+i-2][pos[ss+rtc][3][1]+j]=' '
		dup[pos[ss+rtc][0][0]+i-1][pos[ss+rtc][0][1]+j]='x'
		dup[pos[ss+rtc][1][0]+i-1][pos[ss+rtc][1][1]+j]='x'
		dup[pos[ss+rtc][2][0]+i-1][pos[ss+rtc][2][1]+j]='x'
		dup[pos[ss+rtc][3][0]+i-1][pos[ss+rtc][3][1]+j]='x'
		return 1
for i in range(0,32):
    for j in range(0,34):
	dup[i][j]=arr[i][j]
def merge(arr,dup):	
	for i in range(0,32):
    		for j in range(0,34):
		    if(dup[i][j]=='x'):
			arr[i][j]=dup[i][j]
x=Board(0)
def clear(arr,k,dup):
	    for aw in range(1,k):
		for aw1 in range(1,32):
		    arr[k+1-aw][aw1]=arr[k-aw][aw1]
	    for aw in range(1,32):
		arr[1][aw]=' '
	    for aw in range(1,k):
		for aw1 in range(1,32):
		    dup[k+1-aw][aw1]=dup[k-aw][aw1]
	    for aw in range(1,32):
		dup[1][aw]=' '
screen=curses.initscr()
screen.border()
curses.noecho()
screen.nodelay(1)
curses.curs_set(0)
screen.addstr(35,5,"Enjoy the game")
screen.refresh()
screen.addstr(36,6,"Instructions for playing the game are")
screen.refresh()
screen.addstr(37,6,"'a' for left move and 'd' for right move")
screen.refresh()
screen.addstr(38,6,"'s' for rotate in clockwise and 'SPACE' for complete fall")
screen.refresh()
while(1):
	re=x.checkRowempty(arr,1)
	for aw2 in range(1,31):
	    re1=x.checkRowfull(arr,aw2)
	    if(re1==1):
		clear(arr,aw2,dup)
		x.updatescore(100)
	if(re!=1):
	    screen.addstr(40,5,"GAME OVER'''''''  GAME OVER 'SORRY THIS IS CHILDREN'S GAME'")
	    screen.refresh()
	    time.sleep(5)
	    curses.endwin()
	    break;
	x.updatescore(10)
	ss=x.selectpiece()
	z=0
	count=1
	rc=0
    	while(1):
		q=screen.getch()
		if(q==ord('a')):
			#os.system('clear')
			temp=x.moveLeft(count-1,z-1,arr,1,dup,rc,pos,ss)
			if(temp==1):
			    z=z-1
			dupprint1()
			dupprint(dup)
		elif(q==ord('s')):
			#os.system('clear')
			temp=x.rotate(count-1,z,arr,rc,dup,pos,ss)
			if(rc==1 and temp==1):
			    rc=0
			elif(rc==0 and temp==1):
			    rc=1
			else:
			    hiy=0
			dupprint1()
			dupprint(dup)
		elif(q==ord('d')):
		 	#os.system('clear')
			temp=x.moveRight(count-1,z+1,arr,-1,dup,rc,pos,ss)
			if(temp==1):
			    z=z+1
			dupprint1()
			dupprint(dup)
		elif(q==ord(' ')):
			var=count
			for tr in range(var,31):
				#os.system('clear')
				ss1=x.checkPiecepos(count,z,ss,arr,rc)
				#print "asfgasdfasd"
				if(ss1==1):
			    		x.fillPiecePos(count,z,ss,dup,rc)
					count=count+1
				else:
		    			break
			dupprint1()
		    	dupprint(dup)
			break
		#os.system('clear')
		ss1=x.checkPiecepos(count,z,ss,arr,rc)
		if(ss1==1):
		    	x.fillPiecePos(count,z,ss,dup,rc)
			dupprint1()
			dupprint(dup)
			count=count+1
		else:
		    	dupprint1()
		    	dupprint(dup)
	    		break
		time.sleep(.6)
	merge(arr,dup)
	screen.addstr(39,6,"Your score is")
	screen.refresh()
	sepas=x.getscore()
	screen.addstr(39,21,str(sepas))
	screen.refresh()
	time.sleep(2)
	
#os.system('clear')
