#metto  5 alla variabile x e John alla variabile y
x = 5
y = "John"
print(x)
print(y)
print("#############")
#attribuisco alla variabile x il valore 4 e il nome Sally
x = 4    
print(x)  
x = "Sally" 
print(x)

print("#############")
#definisco il tipo di variabile
x = str(3)    
x = '3'
y = int(3)   
z = float(3)
z = 3.0
print(x)
print(y)
print(z)


x = 3
y = str(x)

print("#############")
# assegno alla variabile x il valore intero 5 e alla variabile y John che è una stringa, stampo il tipo di variabile con il loro valore
x = 5
y = "John"
print(int(x))
print(str(y))

print("#############")
x = "John"
x = 'John'

print("#############")
#nomino la prima variabile "a " di tipo intero e la seconda variabile "A" di tipo str
a = 4
A = "Sally"
print("#############")
#attribuiusco ad ogni variabile un nome che non inizi con un numero e non contenga spazi
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print("#############")
#nomino le 3 variabili: la prima con due lettere maiuscole, la seconda con 3 lettere maiuscole, la terza con il trattino basso
myVariableName = "John"
MyVariableName = "John"
my_variable_name = "John"

print("#############")
#definisco 3 variabili contenenti i seguenti nomi,stampo le variabili
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print("#############")
#definisco 3 variabili diverse che contengono tutte la stessa cosa,stampo le variabili
x = y = z = "Orange"
print(x)
print(y)
print(z)

print("#############")
#definisco una variabile unica contenente 3 valori str, dichiaro che la variabile definita e' corrisponde a tre variabili diverse che contengono 3 valori uguali.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print("#############")
#definisco una variabile x contenente una frase, stampo la variabile con la frase
x = "Python is awesome"
print(x)


print("#############")
#divido una frase all'interno di tre variabili diverse e stampo le variabili
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

print("#############")
#eseguo la somma di tre variabili
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

print("#############")
x = 5
y = 10
print(x + y)

print("#############")
#l'esercizio è errato perchè non posso eseguiore la smma di due variabili che contengono valori di tipo differente
x = 5
y = "John"
#print(x + y)
print(x,y)
#correggo l'esercizio stampando i valori senza effettuare somma


print("#############")
#creo una variabile fuori da una funzione e la inserisco all'interno di una funzione
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

print("#############")
 #definisco una sola variabile, una fuori dalla funzione e una all'interno. assegno alla stessa variabile due valori diversi
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

print("#############")
#definisco una variabile all'interno di una funzione, la definisco come variabile globale 
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

print("#############")
#definisco una variabile globale e una funzione con una variabile locale
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

