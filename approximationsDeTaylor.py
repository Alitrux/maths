#vraiment ce code est pourri

from matplotlib.pyplot import plot, show, pause, rcParams
from math import exp, cos, sin, factorial
import time

#Cette ligne sert à éviter de calculer plusieurs fois les factorielles (on pourrait d'ailleurs 
#l'améliorer en utilisant le caractère récursif de la factorielle.)
tabFact = [factorial(k) for k in range(50)]

def tracerFonction(f, a, b, points, width, couleur):
	abcisses = []
	ordonnees = []
	for i in range(int((b-a)*points)):
		if abs(f(a+i/points))>1.5:
			continue
		abcisses.append(f(a + i/points))
		ordonnees.append(a+i/points)
	plot(ordonnees, abcisses, linewidth = width, color = couleur)

#Et oui, j'ai vraiment créer une fonction juste pour ça, j'avais prévenu que ce code était déguelasse
def tracerFonctionExp(f, a, b, points, width, couleur):
	abcisses = []
	ordonnees = []
	for i in range(int((b-a)*points)):
		if not(-2 < f(a+i/points) < 10):
			continue
		abcisses.append(f(a + i/points))
		ordonnees.append(a+i/points)
	plot(ordonnees, abcisses, linewidth = width, color = couleur)

#les 3 prochaines fonctions donnent la gerbe attention
def Tcos(n, x):
	somme = 0
	for n in range(0, n):
		if n%2 != 0:
			continue
		if n%4 == 0:
			somme += x**n/tabFact[n]
		else:
			somme -= x**n/tabFact[n]
	return somme

def Tsin(n, x):
	somme = 0
	for n in range(0, n):
		if n%2 != 1:
			continue
		if n%4 == 1:
			somme += x**n/tabFact[n]
		else:
			somme -= x**n/tabFact[n]
	return somme

def Texp(n, x):
	somme = 0
	for n in range(0, n):
		somme += x**n/tabFact[n]
	return somme

def animationCosinus():
	rcParams['axes.facecolor'] = 'black' #pour mettre le fond en noir
	tracerFonction(cos, -15, 15, 10000, 2, (1, 1, 1))
	pause(5)
	for k in range(2, 40, 2):
		tracerFonction(lambda x : Tcos(k, x), -15, 15, 1000, 1, (1-1/k,1-1/k,1-1/k))
		pause(2)
	show()

def animationSinus():
	rcParams['axes.facecolor'] = 'black' #pour mettre le fond en noir
	tracerFonction(sin, -15, 15, 10000, 2, (1, 1, 1))
	pause(5)
	for k in range(1, 40, 2):
		tracerFonction(lambda x : Tsin(k, x), -15, 15, 1000, 1, (1-1/k,1-1/k,1-1/k))
		pause(2)
	show()

def animationExp():
	rcParams['axes.facecolor'] = 'black' #pour mettre le fond en noir
	tracerFonctionExp(exp, -15, 15, 10000, 2, (1, 1, 1))
	pause(5)
	for k in range(2, 40):
		tracerFonctionExp(lambda x : Texp(k, x), -15, 15, 1000, 1, (1-1/(k+1),1-1/(k+1),1-1/(k+1))) #le k+1 est juste là pour éviter les divisions par 0
		pause(1)
	show()

animationCosinus()
animationSinus()
animationExp()
