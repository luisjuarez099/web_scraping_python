import requests#libreria para hacer una peticion
from bs4 import BeautifulSoup
import csv

labels=['lic','sem','mat']#licenciatura, semestre y materias
smt=[]#lista de semestres
mats=[]#lista de materias
rows=[] #lista que contiene diccionarios de la carrera.
def scrap():
	page =  0  #contador de paginas.
	pags=[1,2,3,4,5,6,7,8,9,10,11,15,16,30,34,35,36,39,40] #numero de paginas que voy a scrapyar ID's
	#X=len(pags) #largo del numero de paginas
	while(page < 3):
		markup= requests.get(f'https://www.unedl.edu.mx/carreras/carreras.php?univ=unedl&idCarrera={pags[page]}').text
		#hacer un parseo
		soup=BeautifulSoup(markup,'html.parser') # lo convierta a html. TODO EXTRACTO DE LA PAGINA
		cars={}#Aqui se guarda carreras. licis, semes y materias.
		#nombre de las licenciatura
		for lic in soup.find(class_ = 'color-til-carrera'):
			cars['lic']=lic.get_text().upper()
			#print(lic.get_text())
		
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
								for j in semst:
									smt.append(f"{j}")
									#cars['sem']=smt #[[primer,segundo,tercero]]
							for mat in n.find_all("a",{"href":"#"}):#materias
								#print(mat.get_text())
								maat=[mat.get_text() for m in n.select_one("a",{"href":"#"})]
								for i in maat:
									mats.append(f"{i}")
		print(mats)
		#rows.append(cars)
		print(f'Numero de paginas: {page}')#Imprime NUmero de paginas
		page+=1
		'''for i in rows:
			#print(f'AAAAA: {rows}')
			#generador de csv'''
		try:
			with open(f'{lic.replace(" ","")}.csv','w') as f1:
				writer = csv.DictWriter(f1,fieldnames=labels)
				writer.writeheader() #labels en cabeceras, columnas.
				for elem in rows:
					writer.writerow(elem)
			#limpiamos cada arreglo una vez ya escrito en el csv
			smt.clear()
			mats.clear()
			rows.clear()
		except IOError:
			print("IO/ERROR")

	return rows


row=scrap()


#recorremos list de carreras

#print(row)

#print(soup)

#extraccion de licenciaturas en una lista
'''lic=[lics for lics in soup.find(class_ = 'color-til-carrera')]
print(lic)'''

'''
titulos de la carrera
for title in soup.select('.row'): #row es padre
			#print(title) #se trae todo el html en titulo
			for j in title.select('.col-md-4'):
				t=j.select_one('.color-til-carrera').get_text()
				print(t)
				break
'''

'''
hay que empezar a dividir por secciones.
objetivo: que no se repitan los semestres
1.- recorres los semestres
2.- guardarlos como diccionarios.
3.- pasar despues como conjunto solo la llave no el valor
4.- 


'''

'''
for item in soup.select('.row'): #selecciona todas las clases row
			#print(item) #Imprime todo el html de cada licenciatura
			for i in item.select('.col-md-6 ' '.col-sm-6'):
				#print(i) #te imprime todo el div del .col-md-6
				y = i.select_one('.description').get_text() #le digo que solo me traiga el texto
				print(y)
				

		
		leer plan de estudios
		for plan in soup.select('.description'):
			#print(plan)
			for j in plan.find("h3"):
				print(j)
			
		#accedemos a los semestres
		
		for mat in soup.select('.row'):
			#print(mat)
			for j in mat.find_all("div",{"class":"col-md-6 col-sm-6"}):
				#print(j)
				for x in j.find_all("div",{"class":"description"}):
					#print(x)
					for l in x.find("h3"):
						print(l)
'''