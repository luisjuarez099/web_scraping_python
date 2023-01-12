import requests#libreria para hacer una peticion
from bs4 import BeautifulSoup
import csv
labels=['sem','mat']#licenciatura, semestre y materias
smt=[]#lista de semestres
mats=[]#lista de materias
rows=[] #lista que contiene diccionarios de la carrera.
def scrap():
	page =  0  #contador de paginas.
	pags=[1,2,3,4,5,6,7,8,9,10,11,15,16,30,34,35,36,39,40] #numero de paginas que voy a scrapyar ID's
	#X=len(pags) #largo del numero de paginas
	while(page < 1):
		markup= requests.get(f'https://www.unedl.edu.mx/carreras/carreras.php?univ=unedl&idCarrera={pags[page]}').text
		#hacer un parseo
		soup=BeautifulSoup(markup,'html.parser') # lo convierta a html. TODO EXTRACTO DE LA PAGINA
		#Aqui se guarda carreras. licis, semes y materias.
		cars={}
		#nombre de las licenciatura
		for lic in soup.find(class_ = 'color-til-carrera'):
			#LO agrego como titulo del csv, y lo  quito del diccionario
			#cars['lic']=lic.get_text().upper()
			#IMprimo mis licenciaturas
			lics=lic.get_text().replace(". ","")

		#sacar las materias
		for item in soup.select('.row'): #selecciona todas las clases row
			#print(item) #Imprime todo el html de cada licenciatura
			for i in item.find_all("div",{"id":"page-main"}):
				#print(i)
				for x in i.select(".row"):
					#print(x)
					for p in x.select('.course-thumbnail'):
						#print(p)
						for n in p.select(".description"):
							#print(n)
							for sem in n.select_one("h3"):#semestres.
								#print(f'\t {sem.get_text().upper()}')
								semst=[sem.get_text() for s in n.select_one("h3")]
								#print(semst) #obtengo mi listas
								for j in semst:
									smt.append(j)
									
									#cars[f'{semst}']=smt#[[primer,segundo,tercero]]'''
							for mat in n.find_all("a",{"href":"#"}):#materias
								#print(mat.get_text())
								maat=[mat.get_text() for m in n.select_one("a",{"href":"#"})]
								#print(maat) #se imprime las materias .
								for i in maat:
									smt.append(i)
		#print(smt) #IMprime todo el semestre
		#print(lics)
		cars["semestre"]=lics
		v="" #mi variable string
		for s in smt:
			if "semestre" in s:
				c=s 
				v="" #limpia las variables repetidas
				#print(c.upper())
			else:
				v=v+s+"," #se agrga comas a la concatenacion de cada materia
				#print(v)
				cars[c]=v

		#rows.append(cars)#se agrega mi diccionario a un lista (por ahora no lo usamos)

		#print(f'Numero de paginas: {page}')#Imprime NUmero de paginas
		page+=1

		try:
			with open(f'{lic}.csv','w') as f:
				writer=csv.writer(f)
				#lectura de un diccionario para agregarlo al csv
				for k,v in cars.items():
					writer.writerow([k,v])

		except IOError:
			print("IO/ERROR")
	return rows

row=scrap()
