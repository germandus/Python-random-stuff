PYTHONDONTWRITEBYTECODE='dont whrite pychache'

#import Diccionario1
'''
n=int(input('ingrese un numero: '))
i = 2
primo = True
while(primo and i < n//2):
    if (n%i == 0):
       primo = False
    i+=1
print(bool(primo))
'''
#test de sorted
'''
l=[]
for i in range(6):
    n=input()
    l.append(n)
print(sorted(l))
'''
#test de filter
'''
l=[100,3,20]
def div(x):
    x%10==0
    return True

l=list(filter(div,l))
print(l)
'''
#programita corto para quitar doble espacio
'''
txt=input('texto a quitar doble espacio: ')
for i in range (len(txt)):
    while (txt.count('  '))>0:
        txt=txt.replace('  ',' ')
print(txt)
'''
#ej 1 hackerrank.net
'''
def fizzBuzz(n):
    # Write your code here
    n=int(input('give a number: '))
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0 and i%5!=0:
            print('Fizz')
        elif i%5==0 and i%3!=0:
            print('Buzz')
        else:
            print(i)
if __name__ == '__main__':
'''
#ej 2 hackerrank.net
'''
def triangleOrNot(a, b, c):
     
    a1=[]
    b1=[]
    c1=[]
    d=[]
    for n in range(3): 
        a1.append(a)      
        b1.append(b)
        c1.append()
        for i in range(3):
         if a1[i]>b1[i]>b1[i]:
            if b1[i]+c1[i]>a1[i]:
                d[i]='yes'
            else:
                d1[i]='no'
         elif c1[i]>b1[i]>a1[i]:
            if b1[i]+a1[i]>c1[i]:
                d[i]='yes'
            else:
                d[i]='no'           
         elif b1[i]>c1[i]>a1[c]:
            if a1[i]+c1[i]>b1[i]:
                d[i]='yes'
            else:
                d[i]='no'  

if __name__ == "__main__":
'''
#random code-snippet with switcher
'''
def switch_demo(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
        20: 'Ginobili'
    }
    print (switcher.get(argument, "Invalid month"))
    return

a=int(input('ingrese un mes: '))
switch_demo(a)
'''
#(prueba random) imprime carita llorando print('\U0001F62D')
'''
HOLA=5
CONSTANTT=4
CONSTANTT=5
print(CONSTANT)
'''
'''
jazmín;gerez;formosa;95/n
roberto;luna;corrientes;68/n
antonio peñate río negro 83
marcelo villate santa cruz 99
joaquín;ortiz;alba;entre;ríos;88/n
mariano;villafáñez;santa;cruz;98/n
nicolás;luzuriaga;santa;cruz;97/n
agustín;méndez;formosa;77/n
'''
'''
txt=input('tx: ')
txt=txt.strip()
txt=txt.replace(' ',';')
txt=txt+'/'+'n'
print(txt)
'''
'''
dat=open('datos3.csv','r')
a=dat.readlines()
dat.close()
dat=open('datos3.csv','w')
for i in range (len(a)):
    a[i]=a[i].replace(' ',';')
    #a[i].split(';')
    dat.write(a[i])
dat.close()
'''
'''
dat=open('datos3.csv','r')
a=dat.readlines()
dat.close()
dat=open('datos3.csv','w')
dat.write(str(a))
dat.close()
'''
#saca ultima letra
'''
txt = input('ingrese texto: ')
txt=txt[:len(txt)-1] #saca ultima letra
print(txt)
'''
'''
t=[]
tabla=[1,2,3]
tabla2=[4,5,6]
#t3=t.append(tabla)
#t.append(tabla2)
t=t+tabla+tabla2
print(t)
'''
'''
#test isnumeric()
a='0'
if a.isnumeric():
    print(a)
# isnumeric() -> true if int #false 4 the rest (float or letters )
'''
#function ex
'''
num_1 = int(input('ingrese un numero: '))
num_2 = int(input('ingrese un numero: '))

def suma (n_1:int,n_2:int) -> str:
    sum = n_1 + n_2
    return sum
print(suma(num_1,num_2))
'''
'''
#old
def llorar2(msj):
    msj=msj.split()
    AlguienLlora=False
    for palabra in msj:
        if palabra.lower() in datos.quejas.values(): 
            AlguienLlora=True
            break
    return AlguienLlora
'''
#update
'''
def llorar2(msj):
    msj=msj.split()
    AlguienLlora = False
    i=0
    while AlguienLlora == False and i < (len(msj)):
        if msj[i].lower() in Diccionario1.quejas.values(): 
            AlguienLlora=True
        
        i += 1
    return AlguienLlora

msj = input('ingrese mensaje: ')
print(bool(llorar2(msj)))
'''
#prueba con enumem
'''
enum ='', '1', '2', 4, 5

for i in range (1,6):
    print(str(i),enum[i])
'''
#Casteos varios en python y practica de types - tipos (mini resumen) (list, tuple, set)
'''
conjunto_vacio = set()
conjunto_con_elementos = {1,2}
tupla = (1,2)
lista = [4,5]

#casteo lista a tupla
tupla_nueva = tuple(lista) #devuelve una lista con 4 y 5
print(tupla_nueva)

#casteo str a lista
lista_nueva = list('hola')

#casteo tupla a lista
lista_nueva_de_tupla = list(tupla)

print(lista_nueva)
print(lista_nueva_de_tupla)

#print(conjunto_con_elementos[0]) #tira error set no no es subciptable
print(tupla[0])  #devuelve 1
print(lista[1])  #devuelve 2

print(type(conjunto_vacio))
print(type(conjunto_con_elementos))
print(type(tupla))
print(type(list))
'''
#ejemplo numerico
'''
n=10
xKMenosUno = []
for i in range(n):
    xKMenosUno.append(0)
print(xKMenosUno)
'''
#ejemplos de busqueda
'''
def llorar2(msj):
    llorar = False
    for queja in Diccionario1.quejas.values():
        if msj.find(str(queja)) >-1 and llorar == False:
            llorar = True
            print(bool(llorar))
    return llorar

msj = input()
if llorar2(msj) == True:
    print('lloro')
'''
'''
def llorar2(msj):
    llorar = False
    for queja in Diccionario1.quejas.values():
        if queja in msj and llorar == False:
            llorar = True
    return llorar

msj = input()
if llorar2(msj) == True:
    print('lloro')
'''
#ejemplo de pasaje x referencia
'''
def modifica_lista_1(l):
    l[0] = 'modif'
l = [1,2,3]

modifica_lista_1(l)
print(l)

#ejemplo de pasaje x valor
def modifica_lista_2(l):
    l ='modif'
    return l

l = [1,2,3]
l_modif = modifica_lista_2(l)
print(l_modif)
'''

#creacion de tablero
'''
tablero_1=[]
for columna in range(4):
    tablero_1.append([])
    for fila in range(4):
        tablero_1[columna]=[' ']*4
for columna in tablero_1:
    print(columna)

print()
'''
'''
l=[]
for i in range(4):
  l.append([])
for i in range(4):
  l[i]=[' ']*4
for i in range(4):
    print (l[i])
'''
'''
tablero_1=[]
for fila in range(4):
    tablero_1.append([])
    for columna in range(4):
        tablero_1[fila].append('  1  ')   
''' 
'''
for fila in tablero_1:
    print(fila)
print(tablero_1)
print(tablero_1[fila])
'''
'''
for i in range(4):
    for j in range(4):
        print(tablero_1[i][j], end =' ')
    print()
'''
'''
tam_matriz = int(input('ingrese tamano: '))

matriz_identidad_1 = []
for i in range(tam_matriz):
    fila = []
    for j in range(tam_matriz):
        if i == j:
            fila.append('1')
        else:
            fila.append('0')
    matriz_identidad_1.append(fila)
#tam_matriz = int(input('ingrese tamano: '))

matriz_identidad = []
for fila in range(tam_matriz):
    matriz_identidad.append([])
    for columna in range(tam_matriz):
        if fila == columna:
            matriz_identidad[fila].append('1')
        else:
            matriz_identidad[fila].append('0')

for i in range(tam_matriz):
    print(matriz_identidad_1[i],)
    print("\n")

print('la otra')

for i in range(tam_matriz):
    for j in range(tam_matriz):
        print(matriz_identidad[i][j],end="   ")
    print("\n")
'''
'''
for i in range(n): 
    for j in range (n): 
        print(matriz[i][j]) # seteale el end a tab acá
    print(salto de línea)
'''
'''
for i in range(tam_matriz):
    for j in range(tam_matriz):
        print(matriz_identidad[i][j], end=",")
    print("\n")
'''
'''
for i in range(tam_matriz):
    for j in range(tam_matriz):
        nuevo_elemento = input('ingrese numero: ')
        matriz_identidad[i][j] = nuevo_elemento
'''

#cargar tablero

#from random import randint
#import random

from random import choice, shuffle
from random import randint
'''
tam_matriz = int(input('tamaño: '))

tablero_1=[]
for fila in range(tam_matriz):
    tablero_1.append([])
    for columna in range(tam_matriz):
        tablero_1[fila].append('')

print('tablero vacio\n')
for i in range(4):
    for j in range(4):
        print(tablero_1[i][j], end ='   ')
    print()


elementos =['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S',
'Cl', 'Zr', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V','Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga',  'Ge',
'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Ru', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te',
'I', 'Xe', 'Cs', 'Ba', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Lu', 'Pt', 'Au', 'Hg', 
'Pb', 'Bi', 'Po', 'Rn', 'Fr', 'Ra', 'U', 'Np','Es', 'Rf']

elementos_xa_tablero =[]

for i in range(int((tam_matriz**2)/2)):
    elegido = choice(elementos)
    elementos_xa_tablero.append(elegido)
    elementos_xa_tablero.append(elegido)
    elementos.pop(elementos.index(elegido))

print(int((tam_matriz**2)/2))
shuffle(elementos_xa_tablero)
print(elementos_xa_tablero)

indice = 0
for fila in range(tam_matriz):
    for columna in range(tam_matriz):
        tablero_1[fila][columna] = elementos_xa_tablero[indice]
        indice += 1 

print('tablero cargado\n')
for i in range(tam_matriz):
        for j in range(tam_matriz):
            print(tablero_1[i][j], end ='  ')
        print()

'''
#xa copiar elementos mas facil
'''
dat=open('elementos.txt')
a=dat.readlines()
dat.close()
for ele in a:
    ele=ele[:2]
    print(f" '{ele}', ",end ='')
'''

#no sirve
'''
elementos = ['a','b','c','d','e','f','g','h']
indice = [1,2,3,4,5,6,7,8,]
ya_elegidos = []
for indice in range(indice):
    ya_elegidos.append(elementos[indice])
    
for fila in range(4):
    for columna in range(4):
        tablero_1[fila][columna] = 5

'''
#chequeo eles repes
'''
elementos =['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 
    'S', 'Cl', 'Zr', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V','Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 
    'Ga',  'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Ru', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 
    'I', 'Xe', 'Cs', 'Ba', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Lu', 'Pt', 'Au', 'Hg', 'Pb', 
    'Bi', 'Po', 'Rn', 'Fr', 'Ra', 'U', 'Np','Es', 'Rf']

for ele in elementos:
    if elementos.count(ele)>1:
        print('cuidad0',ele, 'duplicado!')
    
print('Todo OK!, No hay duplicados')
'''
'''
#ejemplo de uso de pass
def prueba (a):
    pass

b=4
prueba(b)
print('hola')
'''
#recomendacion guido xa convertir letras a indices

#Version ingenieri

'''
print(ord("a"))
print(ord("b"))
coord = input("Ingrese primer coordenada (a-z)")
print(ord(coord)-97)

#Version rudimentaria
dicconver = {"a":0,"b":1}
print(dicconver["a"])
'''
