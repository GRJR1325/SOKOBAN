
class Sokoban:
 # REPRESENTACIÓN DEL COMPONENTE DEL JUEGO
 # 0 = Muñeco
 # 1 = Espacio
 # 2 = Cajas
 # 3 = Paredes
 # 4 = Metas
 # 5 = Muñeco_meta
 # 6 = Caja_meta
    
 # Controles:
 # a = Izquierda
 # d = Derecha
 # w = Arriba
 # s = Abajo
 # q = Cerrar juego

#CREACION DEL MAPA DE JUEGO
    
    mapa =[
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 0, 1, 2, 1, 4, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        ]
          
    
    posicion_columna= 4 #Posicion Inicial
    posicion_fila= 4

    
    def imprimirMapa(self):
        for i in self.mapa:  # For each row in map
            print(i)
       # for i in self.mapa:
            #if i == 0: #Muñeco
              #  print(chr(64), end = "")
            #elif i == 1: #Espacio
              #  print (" ",end = "")
            #elif i == 2: #Cajas
               # print(chr(164),end = "")
            #elif i == 3:  #Paredes
               # print (chr(220),end = "")
            #elif i == 4:  #Meta = m
               # print (chr(109),end = "")
            #elif i == 5:  #Muñeco_Meta = N
              #  print (chr(78),end = "")
            #elif i == 6:  #Caja_Meta
               # print (chr(100),end = "")
            #else:
                #print(i, end = "")
        #print()

     def actualizamapa (self):
        for i in range(len(self.mapa)):  # Get rows number on the map
            for columna in range(len(self.mapa[i])):  # Get columns number on the map
                if self.mapa[fila][columna] == 0:  # If the character is found
                    self.posicion_fila = fila # Update the character row position
                    self.posicion_columna = columna           

#CONFIGURACION DE MOVIMIENTOS

#MOVIMIENTOS A LA DERECHA --->
    def moverDerecha(self):
        if (self.mapa[self.posicion_fila][self.posicion_columna] == 0 
        and self.mapa[self.posicion_fila][self.posicion_columna+1] == 1): #Calcula la nueva posicion del muñeco
  
        #CONDICIONES--->
            self.mapa[self.posicion_fila][self.posicion_columna] = 1     
            self.mapa[self.posicion_fila][self.posicion_columna+1] = 0
            self.posicion.columna += 1
            

#MOVIMIENTOS A LA IZQUIERDA <---
    def moverIzquierda(self):
        if self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 1: #Calcula la nueva posicion del muñeco

            #CONDICIONES--->
            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila][self.posicion_columna -1 ] = 0
            
            self.posicion.columna -= 1


        
#EJECUCIÓN DEL JUEGO
juego = Sokoban()

juego.imprimirMapa()

while True:
    instrucciones = "d-Derecha\na-Izquierda\nq-Cerrar Juego"
    print(instrucciones)
    movimientos = input("mover a: ")
    if movimientos == "d": 
        juego.moverDerecha()
        juego.imprimirMapa()
    elif movimientos == "a":
        juego.moverIzquierda()
        juego.imprimirMapa()
    elif movimientos == "q":
        print("Game Over")
        break
        
#PRUEBAS 
        
#class Sokoban
"""

#mapa = {}


    def __init__(self):
        pass

    def leerMapa(self):
        self.mapa [
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 0, 1, 2, 1, 4, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        ]
        self.personaje_fila = 4
        self.personaje_coluna = 4 

    def imprimirMapa(self):
        for fila in self.mapa:
            print(fila)

    def moverDerecha(self)
        print("Moverderecha")

        if self.mapa [personaje_fila][personaje_columna] == 0 and
            self.mapa [personaje_fila][personaje_columna+1]==1):

si eso es cierto ejecuta :


#donde estaba el personaje  
    


def moverIzquierda(self)

        print("Moverizquierda")




    def jugar (self):
        instruccioness= "A=izquierda"
        print(INSTRUCCIONES)
        self.leerMapa()
            while TRUE:
                self.imprimirMapa()
                movimiento = input("Mover hacia")
                if movimiento =="d";
                    moverderecha()
                elif movimiento =="a";
                    moverizquierda()
                elif movimiento =="w";
                    moverdizquierda()
                elif movimiento =="a";
                    moverdizquierda()
juego = Sokoban


personaje meta
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0 
        and self.mapa[self.posicion_fila][self.posicion_columna+1] == 4): #Calcula la nueva posicion del muñeco
  
        #CONDICIONES--->
            self.mapa[self.posicion_fila][self.posicion_columna] = 1     donde estba queda
            self.mapa[self.posicion_fila][self.posicion_columna+1] = 5    queda el personaje meta
            self.posicion.columna += 1





        if (self.mapa[self.posicion_fila][self.posicion_columna] == self.personaje   otra forma de hacerlo
        and self.mapa[self.posicion_fila][self.posicion_columna+1] == self.espacio): #Calcula la nueva posicion del muñeco
  
        #CONDICIONES--->
            self.mapa[self.posicion_fila][self.posicion_columna] = self.espacio 
            self.mapa[self.posicion_fila][self.posicion_columna+1] = self.personaje
            self.posicion.columna += 1

juego = SOKOBAN