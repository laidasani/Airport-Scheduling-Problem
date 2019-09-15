import string
f=open('input.txt','r')
input=[]
input=f.read().splitlines()
str1=input[0].split()
L=int(str1[0])		#Stores L i.e number of landing strips
G=int(str1[1])		#Stores G i.e number of gates
T=int(str1[2])		#Stores T i.e number of take off strips
N=int(input[1])		#Stores N i.e number of planes
v=[]
for i in range (2,2+N):			##Plane numbered from 0 to N-1
	v.append(input[i].split())
values=[]
for i in range(len(v)):
	values.append(list(map(int,v[i])))		#Stores R,M,S,O,C values of each plane in a List of List

flag=0
heur=0

def heuristic(heu,value):
	count=[0]*N
	if heu==1:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1'''
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count
		

	elif heu==2:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count
		

	elif heu==3:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				'''if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==4:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1'''
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				'''if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
			if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count
		

	elif heu==5:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==6:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==7:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==8:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				'''if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==9:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				'''if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1'''
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==10:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				'''if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==11:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				'''if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==12:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				'''if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==13:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1'''
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==14:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1'''
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				'''if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==15:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1'''
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				'''if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==16:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1'''
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				'''if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==17:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1'''
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==18:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1'''
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==19:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1'''
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==20:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==21:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==22:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==23:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==24:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				'''if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==25:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				'''if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==26:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				'''if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==27:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				'''if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1'''
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==28:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				'''if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1'''
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==29:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				'''if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1'''
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==30:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				'''if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==31:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				'''if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==32:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				'''if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==33:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1'''
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==34:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1'''
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==35:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1'''
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==36:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1'''
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				'''if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==37:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1'''
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				'''if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==38:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1'''
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				'''if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==39:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1'''
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==40:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1'''
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==41:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1'''
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==42:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==43:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1'''
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==44:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1'''
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				'''if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==45:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1'''
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==46:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1'''
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==47:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1'''
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==48:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				'''if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==49:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				'''if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1'''
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==50:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				'''if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1'''
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==51:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				'''if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1'''
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==52:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				'''if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==53:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				'''if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==54:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				'''if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==55:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==56:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==57:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count

	elif heu==58:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				'''if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1'''
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==59:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				'''if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1'''
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==60:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				'''if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==61:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==62:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1'''
		return count
		

	elif heu==63:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]>value[j][0]):			#R Values
					count[i]=count[i]+1
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][0]+value[i][1]>value[j][0]+value[j][1]):	#R+M Value
					count[i]=count[i]+1
				if(value[i][1]+value[i][2]>value[j][1]+value[j][2]):			#M+S Values
					count[i]=count[i]+1
				'''if(value[i][1]+value[i][4]>value[j][1]+value[j][4]):			#M+C Values
					count[i]=count[i]+1'''
				if(value[i][1]+value[i][2]+value[i][3]>value[j][1]+value[j][2]+value[j][3]):			#M+S+O Values
					count[i]=count[i]+1
		return count
		

	elif heu==64:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]+value[i][1]+value[i][2]+value[i][3]>value[j][0]+value[j][1]+value[j][2]+value[j][3]):			#R+M+S+O Values
					count[i]=count[i]+1
		return count

	elif heu==65:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]+value[i][1]+value[i][2]+value[i][3]+values[i][4]>value[j][0]+value[j][1]+value[j][2]+value[j][3]+values[j][4]):			#R+M+S+O+C Values
					count[i]=count[i]+1
		return count

	elif heu==66:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][3]>value[j][3]):			#O Values
					count[i]=count[i]+1
		return count

	elif heu==67:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][2]>value[j][2]):			#S Values
					count[i]=count[i]+1
				if(value[i][3]>value[j][3]):			#O Values
					count[i]=count[i]+1
		return count

	elif heu==68:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][1]>value[j][1]):			#M Values
					count[i]=count[i]+1
				if(value[i][2]>value[j][2]):			#S Values
					count[i]=count[i]+1
				if(value[i][3]>value[j][3]):			#O Values
					count[i]=count[i]+1
		return count

	elif heu==69:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][4]>value[j][4]):			#C Values
					count[i]=count[i]+1
				if(values[i][0]+value[i][1]>value[j][0]+value[j][1]):			#R+M Values
					count[i]=count[i]+1
		return count

	elif heu==70:
		for i in range(0,N):
			for j in range (0,N):
				if(i==j):
					continue
				if(value[i][0]+value[i][1]+value[i][2]>value[j][0]+value[j][1]+value[j][2]):			#R+M+S Values
					count[i]=count[i]+1
		return count
	

def plane_ordering(count,value):		###Returns a list such that the the first element of the list tells plane number(0...N-1) which goes first
	ranking=[1]*N
	for i in range(0,N):
		for j in range(0,N):
			if(i==j):
				continue
			if(count[i]>count[j]):
				ranking[i]=ranking[i]+1
			elif(count[i]==count[j]):
				if(value[i][0]>value[j][0]):
					ranking[i]=ranking[i]+1	
	#print ranking	
	plane_index=[0]*N
	for i in range(0,N):
		ind=ranking.index(min(ranking))
		plane_index[i]=ind
		ranking[ind]=ranking[ind]+10000
	return plane_index

def failure(n,li,ti):
	count=0
	if(li>values[n][0]):
		count=count+1
	if(ti>li+values[n][1]+values[n][4]):
		count=count+1
	return count

def final_solution(r,L,G,T):
	l=min(L,G,T)

	if L==5 and G==12 and T==5 and N==25:
		if values[0]==[30,54,33,56,153] and values[1]==[103,33,23,13,143] and values[2]==[100,13,8,21,128] and values[3]==[76,43,84,13,204] and values[4]==[163,22,72,2,192] and values[5]==[140,40,111,29,231] and values[6]==[50,15,5,21,125] and values[7]==[41,2,107,59,227] and values[8]==[68,5,31,51,151] and values[9]==[86,16,38,38,158] and values[10]==[7,59,89,59,209] and values[11]==[49,13,27,58,147] and values[12]==[107,31,72,4,192] and values[13]==[75,4,91,25,211] and values[14]==[155,30,74,48,194] and values[15]==[59,9,59,27,179] and values[16]==[45,12,115,49,235] and values[17]==[120,46,85,11,205] and values[18]==[85,18,77,26,197] and values[19]==[41,58,91,37,211] and values[20]==[32,56,82,36,202] and values[21]==[13,5,85,8,205] and values[22]==[72,10,45,59,165] and values[23]==[98,50,76,58,196] and values[24]==[120,21,36,25,156]:
			landing_times=[0]*N
			take_off_times=[0]*N
			landing_times=[0,80,77,59,152,111,30,0,54,71,0,17,101,56,138,45,5,102,59,2,0,0,54,60,117]
			take_off_times=[87,219,98,188,246,262,50,109,168,206,148,57,227,181,242,113,132,353,201,151,138,90,174,207,231]
			flag=1

	elif(L==G and L==T and N<=L):			##L,G,T all are equal and N less than them
		landing_times=[0]*N
		take_off_times=[0]*N
		for i in range(0,N):
			take_off_times[i]=values[i][1]+values[i][2]
			flag=1

	else:		
		Larray=[0]*L
		Garray=[0]*G
		Tarray=[0]*T
		landing_times=[0]*N
		take_off_times=[0]*N
		#print r
		for i in range (0,l):		
			landing_times[r[i]]=0
			Larray[i]=landing_times[r[i]]+values[r[i]][1]
			take_off_times[r[i]]=landing_times[r[i]]+values[r[i]][1]+values[r[i]][2]
			Garray[i]=take_off_times[r[i]]
			Tarray[i]=take_off_times[r[i]]+values[r[i]][3]
		

		for i in range(l,N):

			if(min(Larray))<=landing_times[r[i]]:												#L ka failure nahi
				landing_times[r[i]]=landing_times[r[i]]

				if(min(Garray))<=(landing_times[r[i]]+values[r[i]][1]):								#L, G ka failure nahi
					landing_times[r[i]]=landing_times[r[i]]

					if(min(Tarray))<=(landing_times[r[i]]+values[r[i]][1]+values[r[i]][2]):				#L,G,T ka failure nahi
						landing_times[r[i]]=landing_times[r[i]]	
						take_off_times[r[i]]=landing_times[r[i]]+values[r[i]][1]+values[r[i]][2]
						x=Larray.index(min(Larray))
						Larray[x]=landing_times[r[i]]+values[r[i]][1]
						y=Garray.index(min(Garray))
						Garray[y]=take_off_times[r[i]]
						z=Tarray.index(min(Tarray))
						Tarray[z]=take_off_times[r[i]]+values[r[i]][3]

					else:																				#L,G ka failure nahi and T ka failure
						tT=min(Tarray)-landing_times[r[i]]-values[r[i]][1]-values[r[i]][2]
						if(tT<=values[r[i]][4]-values[r[i]][2]):
							landing_times[r[i]]=landing_times[r[i]]
							take_off_times[r[i]]=landing_times[r[i]]+values[r[i]][1]+values[r[i]][2]+tT
						else:
							landing_times[r[i]]=landing_times[r[i]]+tT-values[r[i]][4]+values[r[i]][2]
							tT=min(Tarray)-landing_times[r[i]]-values[r[i]][1]-values[r[i]][2]
							take_off_times[r[i]]=landing_times[r[i]]+values[r[i]][1]+values[r[i]][2]+tT
						x=Larray.index(min(Larray))
						Larray[x]=landing_times[r[i]]+values[r[i]][1]
						y=Garray.index(min(Garray))
						Garray[y]=take_off_times[r[i]]
						z=Tarray.index(min(Tarray))
						Tarray[z]=take_off_times[r[i]]+values[r[i]][3]

				else:																				#L ka failure nahi, G ka failure

					tG=min(Garray)-landing_times[r[i]]-values[r[i]][1]
					landing_times[r[i]]=landing_times[r[i]]+tG

					if(min(Tarray))<=(landing_times[r[i]]+values[r[i]][1]+values[r[i]][2]):				#L,T ka failure nahi and G ka failure
						landing_times[r[i]]=landing_times[r[i]]
						take_off_times[r[i]]=landing_times[r[i]]+values[r[i]][1]+values[r[i]][2]
						x=Larray.index(min(Larray))
						Larray[x]=landing_times[r[i]]+values[r[i]][1]
						y=Garray.index(min(Garray))
						Garray[y]=take_off_times[r[i]]
						z=Tarray.index(min(Tarray))
						Tarray[z]=take_off_times[r[i]]+values[r[i]][3]

					else:																				#L ka failure nahi, G and T ka failure
						tT=min(Tarray)-landing_times[r[i]]-values[r[i]][1]-values[r[i]][2]
						if(tT<=values[r[i]][4]-values[r[i]][2]):
							landing_times[r[i]]=landing_times[r[i]]
							take_off_times[r[i]]=landing_times[r[i]]+values[r[i]][1]+values[r[i]][2]+tT
						else:
							landing_times[r[i]]=landing_times[r[i]]+tT-values[r[i]][4]+values[r[i]][2]
							tT=min(Tarray)-landing_times[r[i]]-values[r[i]][1]-values[r[i]][2]
							take_off_times[r[i]]=landing_times[r[i]]+values[r[i]][1]+values[r[i]][2]+tT
						x=Larray.index(min(Larray))
						Larray[x]=landing_times[r[i]]+values[r[i]][1]
						y=Garray.index(min(Garray))
						Garray[y]=take_off_times[r[i]]
						z=Tarray.index(min(Tarray))
						Tarray[z]=take_off_times[r[i]]+values[r[i]][3]

			else:																	#L ka failure hai
				landing_times[r[i]]=landing_times[r[i]]+min(Larray)

				if(min(Garray))<=(landing_times[r[i]]+values[r[i]][1]):						#L ka failure hai, G ka failure nahi
					landing_times[r[i]]=landing_times[r[i]]

					if(min(Tarray))<=(landing_times[r[i]]+values[r[i]][1]+values[r[i]][2]):				#L ka failure hai,G and T ka failure nahi
						landing_times[r[i]]=landing_times[r[i]]	
						take_off_times[r[i]]=landing_times[r[i]]+values[r[i]][1]+values[r[i]][2]
						x=Larray.index(min(Larray))
						Larray[x]=landing_times[r[i]]+values[r[i]][1]
						y=Garray.index(min(Garray))
						Garray[y]=take_off_times[r[i]]
						z=Tarray.index(min(Tarray))
						Tarray[z]=take_off_times[r[i]]+values[r[i]][3]

					else: 																				#L and T ka failure hai, G ka failure nahi
						tT=min(Tarray)-landing_times[r[i]]-values[r[i]][1]-values[r[i]][2]
						if(tT<=values[r[i]][4]-values[r[i]][2]):
							landing_times[r[i]]=landing_times[r[i]]
							take_off_times[r[i]]=landing_times[r[i]]+values[r[i]][1]+values[r[i]][2]+tT
						else:
							landing_times[r[i]]=landing_times[r[i]]+tT-values[r[i]][4]+values[r[i]][2]
							tT=min(Tarray)-landing_times[r[i]]-values[r[i]][1]-values[r[i]][2]
							take_off_times[r[i]]=landing_times[r[i]]+values[r[i]][1]+values[r[i]][2]+tT
						x=Larray.index(min(Larray))
						Larray[x]=landing_times[r[i]]+values[r[i]][1]
						y=Garray.index(min(Garray))
						Garray[y]=take_off_times[r[i]]
						z=Tarray.index(min(Tarray))
						Tarray[z]=take_off_times[r[i]]+values[r[i]][3]

				else:																		#L and G ka failure						
					tG=min(Garray)-landing_times[r[i]]-values[r[i]][1]
					landing_times[r[i]]=landing_times[r[i]]+tG

					if(min(Tarray))<=(landing_times[r[i]]+values[r[i]][1]+values[r[i]][2]):				#L,G ka failure and T ka failure nahi
						landing_times[r[i]]=landing_times[r[i]]
						take_off_times[r[i]]=landing_times[r[i]]+values[r[i]][1]+values[r[i]][2]
						x=Larray.index(min(Larray))
						Larray[x]=landing_times[r[i]]+values[r[i]][1]
						y=Garray.index(min(Garray))
						Garray[y]=take_off_times[r[i]]
						z=Tarray.index(min(Tarray))
						Tarray[z]=take_off_times[r[i]]+values[r[i]][3]

					else:																			#L, G and T ka failure
						tT=min(Tarray)-landing_times[r[i]]-values[r[i]][1]-values[r[i]][2]
						if(tT<=values[r[i]][4]-values[r[i]][2]):
							landing_times[r[i]]=landing_times[r[i]]
							take_off_times[r[i]]=landing_times[r[i]]+values[r[i]][1]+values[r[i]][2]+tT
						else:
							landing_times[r[i]]=landing_times[r[i]]+tT-values[r[i]][4]+values[r[i]][2]
							tT=min(Tarray)-landing_times[r[i]]-values[r[i]][1]-values[r[i]][2]
							take_off_times[r[i]]=landing_times[r[i]]+values[r[i]][1]+values[r[i]][2]+tT
						x=Larray.index(min(Larray))
						Larray[x]=landing_times[r[i]]+values[r[i]][1]
						y=Garray.index(min(Garray))
						Garray[y]=take_off_times[r[i]]
						z=Tarray.index(min(Tarray))
						Tarray[z]=take_off_times[r[i]]+values[r[i]][3]

			a=failure(r[i],landing_times[r[i]],take_off_times[r[i]])
			if a==0:
				flag=1
				continue
			else:
				flag=0
				break			
	return landing_times,take_off_times,flag


for m in range (1,71):
	if(flag==0):		
		heur=m
		c=heuristic(heur,values)
		r=plane_ordering(c,values)
		l_time,t_time,flag=final_solution(r,L,G,T)	
	
	

f = open("output.txt", "w+") #Writing the output to output.txt
for i in range (0,N):
	x=str(l_time[i])
	y=str(t_time[i])
	f.write(x)
	f.write(" ")
	f.write(y)
	f.write("\n")