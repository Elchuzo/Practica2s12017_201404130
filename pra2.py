from flask import Flask, request, Response
from graphviz import Digraph
app = Flask("Practica2")


  
class Nodo(object):

    def __init__(self, dato=None,siguiente=None):
        self.dato = dato
        self.siguiente = siguiente
    
    def get_dato(self):
        return self.dato
    
    def get_siguiente(self):
        return self.siguiente
        
    def set_siguiente(self,nuevo):
        self.siguiente = nuevo

class NodoDoble(object):

    def __init__(self, dato, derecha = None, izquierda=None, arriba=None, abajo=None,posx=None,posy=None):
        self.dato = dato
        self.derecha = derecha
        self.izquierda = izquierda
        self.arriba = arriba
        self.abajo = abajo
        self.posx = posx
        self.posy = posy
		
class ListaDoble(object):
    
    def __init__(self, cabeza =None):
        self.cabeza = None
    
    def insertar_inicio(self,entrada):
        nuevo = NodoDoble(entrada)
        nuevo.derecha = cabeza
        if(self.cabeza is not None):
            cabeza.izquierda = nuevo
        cabeza = nuevo
    
    def eliminar(self,entrada):
        actual = self.cabeza
        encontrado = False
        while((actual is not None) and (not encontrado)):
            if (actual.dato == entrada):
               encontrado = True
            else:
                actual = actual.derecha
        if(actual is not None):
            if(actual==self.cabeza):
                self.cabeza = actual.derecha
                if(actual.derecha is not None):
                    actual.derecha.izquierda = None
            elif(actual.derecha is not None):
                actual.izquierda.derecha = actual.derecha
                actual.derecha.izquierda = actual.izquierda
            else:
                actual.izquierda.derecha = None
            actual = None

class Lista(object):
    
    def __init__(self,cabeza=None):
        self.cabeza = cabeza
    
    def insertar(self, dato):
        nuevo = Nodo(dato)
        nuevo.set_siguiente(self.cabeza)
        self.cabeza = nuevo
    
    def tamanio(self):
        actual = self.cabeza
        contador = 0
        while actual:
            contador += 1
            actual = actual.get_siguiente()
        return count
        
    def buscar(self,dato):
        contador = 0
        actual = self.cabeza
        encontrado = False
        while actual and encontrado is False:
            if actual.get_dato() == dato:
                encontrado = True
                "valor encontrado en" + str(contador)
            else:
                actual = actual.get_siguiente()
        i+=1
        if actual is None:
            raise ValueError("Dato no encontrado")
        return "valor no encontrado"
    
    def eliminar(self, dato):
        actual = self.cabeza
        previo = None
        encontrado = False
        while actual is not None and encontrado is False:
            
            if actual.get_dato() == dato:
                encontrado = True
            else:
                previo = actual
                actual = actual.get_siguiente()
        if actual is not None:
            if(actual==self.cabeza):
                self.cabeza = actual.siguiente
            else:
                previo.siguiente = actual.siguiente
            actual = None
            return "valor eliminado"
        else:
             return "valor no encontrado"

class Pila(object):
    
    def __init__(self, top=None):
        self.top=top
    
    def vacia(self):
        if self.top is None:
            return True
        else:
            return False
    
    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.top
        self.top = nuevo;
    def pop(self):
        a = self.top.dato
        self.top = self.top.siguiente;
        return a
    def top(self):
        return top.dato;
    def limpiar(self):
        while(not vacia()):
            pop()
        return "pila vaciada"

class cola(object):
    def __init__(self, inicio=None, fin=None):
        self.inicio = inicio
        self.fin = fin
    
    def vacia(self):
        if self.inicio is None:
            return True
        else:
            return False
    def insertar(self, dato):
        nuevo = Nodo(dato)
        if(self.vacia()):
            self.inicio = nuevo
        else:
            self.fin.siguiente = nuevo
        self.fin = nuevo
    def extraer(self):
        a = self.inicio.dato
        self.inicio = self.inicio.siguiente
        return a
    def inicio(self):
        return self.inicio.dato
    def fin():
        return self.fin.dato
    def limpiar():
        while(not self.vacia()):
    	     extraer()

def graficarlista():
    dot = Digraph(comment='Prueba')
    i = 0
    actual = list.cabeza
    if (list.tamanio==0):
        pass
    else:
        print(actual.dato)
        dot.node(str(i),actual.dato)
        while(actual != None):           
            if(actual.siguiente is not None):
                temp = Nodo()
                temp = actual.siguiente
                dot.node(str(i+1),temp.dato)
                sta = str(i)
                stb = str(i+1)
                dot.edge(sta,stb,constraint='false')
            actual = actual.siguiente
            i+=1
    print(dot.source)
    dot.render('prueba3.gv',cleanup=True)
    dot.save('prueba3.gv',"C:\\Users\\Oscar\\Desktop")
 
def graficarcola():
    dot = Digraph(comment='Prueba')
    i = 0
    actual = queue.inicio
    if (queue.vacia()==True):
        pass
    else:
        print(actual.dato)
        dot.node(str(i),actual.dato)
        while(actual != None):           
            if(actual.siguiente is not None):
                temp = Nodo()
                temp = actual.siguiente
                dot.node(str(i+1),temp.dato)
                sta = str(i)
                stb = str(i+1)
                dot.edge(stb,sta,constraint='false')
            actual = actual.siguiente
            i+=1
    print(dot.source)
    dot.render('prueba2.gv',cleanup=True)
    dot.save('prueba2.gv',"C:\\Users\\Oscar\\Desktop")
			
def graficar():
    dot = Digraph(comment='Prueba')
    i = 0
    actual = stack.top
    if (stack.vacia()==True):
        pass
    else:
        print(actual.dato)
        dot.node(str(i),actual.dato)
        while(actual != None):           
            if(actual.siguiente is not None):
                temp = Nodo()
                temp = actual.siguiente
                dot.node(str(i+1),temp.dato)
                sta = str(i)
                stb = str(i+1)
                dot.edge(sta,stb)
            actual = actual.siguiente
            i+=1
    print(dot.source)
    dot.render('prueba.gv',cleanup=True)
    dot.save('prueba.gv',"C:\\Users\\Oscar\\Desktop")
    
stack = Pila()
queue = cola()
list = Lista()

@app.route('/pila',methods=['POST']) 
def push():
    parametro = str(request.form['dato'])
    operacion = str(request.form['operacion'])
    if(operacion=="push"):         
        stack.push(parametro)
        graficar()
        return "Elemento Ingresado"
    else:
        res = stack.pop()
        graficar()
        return res
@app.route('/cola',methods=['POST']) 
def encolar():
    parametro = str(request.form['dato'])
    operacion = str(request.form['operacion'])
    if(operacion=="insertar"):         
        queue.insertar(parametro)
        graficarcola()
        return "Elemento Ingresado"
    else:
        res = queue.extraer()
        graficarcola()
        return res
@app.route('/lista',methods=['POST']) 		
def insertar():
    parametro = str(request.form['dato'])
    operacion = str(request.form['operacion'])
    if(operacion=="insertar"):         
        list.insertar(parametro)
        graficarlista()
        return "Elemento Ingresado"
    elif(operacion=="buscar"):
        return list.buscar(parametro)		
    else:
        res = list.eliminar(parametro)
        graficarlista()
        return res
    

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
  