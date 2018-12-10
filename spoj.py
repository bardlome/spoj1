import random
#https://pl.spoj.com/problems/TROJEDNO/

try:
	n=input("ile punktow? ")
except NameError:
	print "taaaak. dla wygody uznam, ze miales/as na mysli 5"
	n=5

wezly=[]
czerwone=0
def taknie():
	y=random.sample(range(2),1)
	if y==[1]:
		return "czerwo"
	else:
		return "czarna"
iloscx=0
for i in range(n):
	j=i+1
	while j<n:
		b=[i,j,taknie()]
		print b
		if b[2]=="czerwo":
			czerwone+=1
		wezly.append(b)
		iloscx+=1
		j+=1
print "czeronwe linie: " , czerwone


licznik=0
czerwonytrojkat=0
carnytrojkat=0
for i in range(n):
	j=i+1
	while j<n:
		if (wezly[licznik])[2]=="czerwo":
			pierwsza = (wezly[licznik])[1]
			druga= (wezly[licznik])[0]
			for s in range(iloscx):
				if (wezly[s])[0]==pierwsza and (wezly[s])[2] == "czerwo":
					trzecia=(wezly[s])[1]
					for z in range(iloscx):
						if (wezly[z])[0]==druga and (wezly[z])[1]==trzecia and (wezly[z])[2]== "czerwo":	
							czerwonytrojkat+=1
							print "znaleziony red: ", pierwsza, " ", druga, " ",trzecia			
		elif (wezly[licznik])[2]=="czarna":
			pierwsza2 = (wezly[licznik])[1]
			druga2= (wezly[licznik])[0]
			for s in range(iloscx):
				if (wezly[s])[0]==pierwsza2 and (wezly[s])[2] == "czarna":
					trzecia2=(wezly[s])[1]
					for z in range(iloscx):
						if (wezly[z])[0]==druga2 and (wezly[z])[1]==trzecia2 and (wezly[z])[2]== "czarna":
							carnytrojkat+=1			
							print "znaleziony black: ", pierwsza2, " ", druga2, " ",trzecia2			

		licznik+=1
		j+=1

print "redy: ", czerwonytrojkat
print "czarne: ", carnytrojkat

