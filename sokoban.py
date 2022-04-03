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

    posicion = 0
    espacio = 1
    caja = 2
    paredes = 3
    meta = 4
    
    posicion_meta = 5
    caja_meta = 6
    
    mapa = []
    
    posicion_fila = 0
    posicion_columna = 0
    
    def __init__(self):
        pass
          
    def leermapa(self):
        self.mapa = [
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 4, 1, 0, 1, 2, 4, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        ]
        self.posicion_fila = 3     #Posicion Inicial
        self.posicion_columna = 5

    
    def imprimirmapa(self):
        for fila in self.mapa:  # For each row in map
            print(fila)
            
       #for i in self.mapa:
           # if i == 0: #Muñeco
                #print(chr(64), end = "")
           # elif i == 1: #Espacio
                #print (" ",end = "")
           # elif i == 2: #Cajas
               #print(chr(164),end = "")
           # elif i == 3:  #Paredes
               # print (chr(220),end = "")
           # elif i == 4:  #Meta = m
              #  print (chr(109),end = "")
            #elif i == 5:  #Muñeco_Meta = N
                #print (chr(78),end = "")
           # elif i == 6:  #Caja_Meta
                #print (chr(100),end = "")
           # else:
               # print(i, end = "")
       # print()



#CONFIGURACION DE MOVIMIENTOS

#MOVIMIENTOS A LA DERECHA --->
    def moverDerecha(self):
        print("Mover derecha")

        #CONDICIONES--->
        # 0 Personaje, espacio  0,1 -> 1,0
        if (self.mapa[self.posicion_fila][self.posicion_columna] == 0 
        and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 1): #Calcula la nueva posicion del muñeco
  
            self.mapa[self.posicion_fila][self.posicion_columna] = 1     
            self.mapa[self.posicion_fila][self.posicion_columna + 1] = 0
            self.posicion_columna += 1

        # 1 Personaje, meta  0,4 -> 1,5
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0   
        and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 4):

            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila][self.posicion_columna + 1] = 5
            self.posicion_columna += 1
            
         # 2 Personaje, caja, espacio  0,2,1 -> 1,0,2
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0
        and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 2 
        and self.mapa[self.posicion_fila][self.posicion_columna + 2] == 1):
            
            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila][self.posicion_columna + 1] = 0
            self.mapa[self.posicion_fila][self.posicion_columna + 2] = 2
            self.posicion_columna += 1

        # 3 Personaje, caja, meta  0,2,4 -> 1,0,6
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0 
        and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 2 
        and self.mapa[self.posicion_fila][self.posicion_columna + 2] == 4):

            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila][self.posicion_columna + 1] = 0
            self.mapa[self.posicion_fila][self.posicion_columna + 2] = 6
            self.posicion_columna += 1

        # 4 Personaje, caja-meta, espacio 0,6,1 -> 1,5,2
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0
        and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 6
        and self.mapa[self.posicion_fila][self.posicion_columna + 2] == 1):

            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila][self.posicion_columna + 1] = 5
            self.mapa[self.posicion_fila][self.posicion_columna + 2] = 2
            self.posicion_columna += 1

        # 5 Personaja, caja_meta, meta 0,6,4 -> 1,5,6
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0
        and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 6
        and self.mapa[self.posicion_fila][self.posicion_columna + 2] == 4):

            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila][self.posicion_columna + 1] = 5
            self.mapa[self.posicion_fila][self.posicion_columna + 2] = 6
            self.posicion_columna += 1

        # 6 Personaje_meta,espacio 5,1 -> 4,0
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 1):

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila][self.posicion_columna + 1] = 0
            self.posicion_columna += 1

        # 7 Personaje_meta, meta 5,4 -> 4,5
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 4):

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila][self.posicion_columna + 1] = 5
            self.posicion_columna += 1

        # 8 Personaje_meta, caja, espacio 5,2,1 -> 4,0,2
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 2
        and self.mapa[self.posicion_fila][self.posicion_columna + 2] == 1):

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila][self.posicion_columna + 1] = 0
            self.mapa[self.posicion_fila][self.posicion_columna + 2] = 2
            self.posicion_columna += 1

        # 9 Muñeco_meta, Caja, meta 5,2,4 -> 4,0,6
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 2
        and self.mapa[self.posicion_fila][self.posicion_columna + 2] == 4):

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila][self.posicion_columna + 1] = 0
            self.mapa[self.posicion_fila][self.posicion_columna + 1] = 6
            self.posicion_columna += 1

        # 10 Personaje_meta, caja, meta,espacio 5,6,4 -> 4,5,6
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 6
        and self.mapa[self.posicion_fila][self.posicion_columna + 2] == 4):

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila][self.posicion_columna + 1] = 5
            self.mapa[self.posicion_fila][self.posicion_columna + 2] = 6
            self.posicion_columna += 1   

        # 11 Personaje_meta, caja, meta 5,6,1 -> 4,5,2
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 6
        and self.mapa[self.posicion_fila][self.posicion_columna + 2] == 1):

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila][self.posicion_columna + 1] = 5
            self.mapa[self.posicion_fila][self.posicion_columna + 2] = 2
            self.posicion_columna += 1

#MOVIMIENTOS A LA IZQUIERDA <---
    def moverIzquierda(self):
        print("Mover Izquierda")

        #CONDICIONES <---
        # 0 Personaje, espacio  1,0 -> 0,1
        if (self.mapa[self.posicion_fila][self.posicion_columna] == 0 
        and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 1): #Calcula la nueva posicion del muñeco

            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila][self.posicion_columna -1 ] = 0
            self.posicion_columna -= 1

        # 1 Personaje, meta  4,0 --> 5,1
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0   
        and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 4):

            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila][self.posicion_columna - 1] = 5
            self.posicion_columna -= 1               

         # 2 Personaje, caja, espacio  1,2,0 -> 2,0,1
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0
        and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 2 
        and self.mapa[self.posicion_fila][self.posicion_columna - 2] == 1):
            
            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila][self.posicion_columna - 1] = 0
            self.mapa[self.posicion_fila][self.posicion_columna - 2] = 2
            self.posicion_columna -= 1
 
         # 3 Personaje ,caja, meta 4,2,0 -> 6,0,1
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0
        and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 2 
        and self.mapa[self.posicion_fila][self.posicion_columna - 2] == 4):
            
            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila][self.posicion_columna - 1] = 0
            self.mapa[self.posicion_fila][self.posicion_columna - 2] = 6
            self.posicion_columna -= 1

         # 4 Personaje, caja_meta, espacio 1,6,0 -> 2,5,1
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0
        and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 6
        and self.mapa[self.posicion_fila][self.posicion_columna - 2] == 1):
            
            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila][self.posicion_columna - 1] = 5
            self.mapa[self.posicion_fila][self.posicion_columna - 2] = 2
            self.posicion_columna -= 1

         # 5 Personaje, caja_meta, meta 4,6,0 -> 6,5,1
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0
        and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 6 
        and self.mapa[self.posicion_fila][self.posicion_columna - 2] == 4):
            
            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila][self.posicion_columna - 1] = 5
            self.mapa[self.posicion_fila][self.posicion_columna - 2] = 6
            self.posicion_columna -= 1

        # 6 Personaje_meta, espacio 1,5 -> 0.4
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5 
        and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 1 ):

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila][self.posicion_columna - 1] = 0
            self.posicion_columna -= 1   

        # 7 Personaje_meta, meta 4,5 -> 5,4 
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 4   
        and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 5):

            self.mapa[self.posicion_fila][self.posicion_columna] = 5
            self.mapa[self.posicion_fila][self.posicion_columna - 1] = 4 
            self.posicion_columna -= 1 

         # 8 Personaje_meta, caja, espacio 1,2,5 -> 2,0,4
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 2
        and self.mapa[self.posicion_fila][self.posicion_columna - 2] == 1):
            
            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila][self.posicion_columna - 1] = 0
            self.mapa[self.posicion_fila][self.posicion_columna - 2] = 2
            self.posicion_columna -= 1

        # 9 Personaje_meta, caja, meta 4,2,5 -> 6,0,4
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 2 
        and self.mapa[self.posicion_fila][self.posicion_columna - 2] == 4):
            
            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila][self.posicion_columna - 1] = 0
            self.mapa[self.posicion_fila][self.posicion_columna - 2] = 6
            self.posicion_columna -= 1
            
         # 10 Personaje_meta, caja_meta, espacio 4,6,5 -> 6,5,4
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 6
        and self.mapa[self.posicion_fila][self.posicion_columna - 2] == 4):
            
            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila][self.posicion_columna - 1] = 5
            self.mapa[self.posicion_fila][self.posicion_columna - 2] = 6
            self.posicion_columna -= 1

         # 11 Personaje_meta, caja_meta, meta 1,6,5 -> 2,5,4
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 6 
        and self.mapa[self.posicion_fila][self.posicion_columna - 2] == 1):
            
            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila][self.posicion_columna - 1] = 5
            self.mapa[self.posicion_fila][self.posicion_columna - 2] = 2
            self.posicion_columna -= 1
  
                
#EJECUCIÓN DEL JUEGO

    def jugar(self):
        instrucciones = "d-Derecha\na-Izquierda\nq-Cerrar Juego"
        print(instrucciones)
        self.leermapa()
        while True:
            self.imprimirmapa()
            movimiento = input("Mover hacia:")
            
            if movimiento == "d":
                self.moverDerecha()
                
            elif movimiento == "a":
                self.moverIzquierda()
                
            elif movimiento == "q":
                print("Salir del juego")
                break
                    
juego = Sokoban()
juego.jugar()