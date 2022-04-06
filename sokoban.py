import numpy as op
...
archivo_nivel = op.genfromtxt(fname='Nvl1.txt')

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
    mapa = op.loadtxt('Nvl1.txt',dtype=int)

    posicion_fila = 0
    posicion_columna = 0
    
    def __init__(self):
        pass
          
    def leermapa(self):
        self.mapa = op.loadtxt('Nvl1.txt',dtype=int)

    def imprimirmapa(self):
        for fila in self.mapa: 
            for columna in fila: # For each row in map
                if columna == 0: #Muñeco
                    print(chr(64), end = "")
                elif columna == 1: #Espacio
                    print (" ",end = "")
                elif columna == 2: #Cajas
                    print(chr(67),end = "")
                elif columna == 3:  #Paredes
                    print (chr(79),end = "")
                elif columna == 4:  #Meta = m
                    print (chr(109),end = "")
                elif columna == 5:  #Muñeco_Meta = N
                    print (chr(110),end = "")
                elif columna == 6:  #Caja_Meta
                    print (chr(43),end = "")
                else:
                    print(columna, end = "")
            print()

#ENCONTRAR LA POSICION DEL PERSONAJE
    def EncontrarPosicion(self):
        for fila in range(len(self.mapa)):  # Get rows number on the map
            for columna in range(len(self.mapa[fila])):  # Get columns number on the map
                if self.mapa[fila][columna] == 0:  # If the character is found
                   self.posicion_fila = fila  # Update the character row position
                   self.posicion_columna = columna  # Update the character col position

#NIVEL COMPLETADO
    def completado(self):
        for columna in self.mapa:
            for cell in columna:
                if cell == '+':
                    return False
        return True                      


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
  
#MOVIMIENTOS ARRIBA ^
    def moverArriba(self):
        print("Mover Arriba")

        #CONDICIONES ^
        # 0 Espacio, personaje  1,0 -> 0,1
        if (self.mapa[self.posicion_fila][self.posicion_columna] == 0 
        and self.mapa[self.posicion_fila - 1] [self.posicion_columna] == 1): 

            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila - 1][self.posicion_columna] = 0
            self.posicion_fila -= 1

        # 1 Meta, personaje 4,0 -> 5,1
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0
        and self.mapa[self.posicion_fila - 1] [self.posicion_columna] == 4): 

            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila - 1][self.posicion_columna] = 5
            self.posicion_fila -= 1

        # 2 Espacio, caja, personaje 1,2,0 -> 2,0,1
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0
        and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 2
        and self.mapa[self.posicion_fila - 2][self.posicion_columna] == 1):

            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila - 1][self.posicion_columna] = 0
            self.mapa[self.posicion_fila - 2][self.posicion_columna] = 2
            self.posicion_fila -= 1           

        # 3 Meta, caja, personaje 4,2,0 -> 6,0,1
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0
        and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 2
        and self.mapa[self.posicion_fila - 2][self.posicion_columna] == 4):

            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila - 1][self.posicion_columna] = 0
            self.mapa[self.posicion_fila - 2][self.posicion_columna] = 6
            self.posicion_fila -= 1    

        # 4 Espacio, caja_meta 1,6,0 -> 2,5,1

        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0
        and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 6
        and self.mapa[self.posicion_fila - 2][self.posicion_columna] == 1):

            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila - 1][self.posicion_columna] = 5
            self.mapa[self.posicion_fila - 2][self.posicion_columna] = 2
            self.posicion_fila -= 1   

        # 5 Meta, caja_meta, personaje 4,6,0 -> 6,5,1
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0
        and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 6
        and self.mapa[self.posicion_fila - 2][self.posicion_columna] == 4):

            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila - 1][self.posicion_columna] = 5
            self.mapa[self.posicion_fila - 2][self.posicion_columna] = 6
            self.posicion_fila -= 1   

        # 6 Espacio, personaje_meta 1,5 -> 0,4
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 1): 

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila - 1][self.posicion_columna] = 0
            self.posicion_fila -= 1

        # 7 Meta, personaje_meta 4,5 -> 5,4
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila - 1] [self.posicion_columna] == 4): 

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila - 1][self.posicion_columna] = 5
            self.posicion_fila -= 1            

        # 8 Espacio, caja , personaje_meta 1,2,5 -> 2,0,4
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 2
        and self.mapa[self.posicion_fila - 2][self.posicion_columna] == 1):

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila - 1][self.posicion_columna] = 0
            self.mapa[self.posicion_fila - 2][self.posicion_columna] = 2
            self.posicion_fila -= 1    

        # 9 Meta, caja, personaje_meta 4,2,5 -> 6,0,4
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 2
        and self.mapa[self.posicion_fila - 2][self.posicion_columna] == 4):

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila - 1][self.posicion_columna] = 0
            self.mapa[self.posicion_fila - 2][self.posicion_columna] = 6
            self.posicion_fila -= 1    

        # 10 Espacio, caja_meta, personaje_meta 4,6,5 -> 6,5,4 
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 6
        and self.mapa[self.posicion_fila - 2][self.posicion_columna] == 4):

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila - 1][self.posicion_columna] = 5
            self.mapa[self.posicion_fila - 2][self.posicion_columna] = 6
            self.posicion_fila -= 1    

        # 11 Meta, caja_meta, personaje_meta 1,6,5 -> 2,5,4
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 6
        and self.mapa[self.posicion_fila - 2][self.posicion_columna] == 1):

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila - 1][self.posicion_columna] = 5
            self.mapa[self.posicion_fila - 2][self.posicion_columna] = 2
            self.posicion_fila -= 1       

    def moverAbajo(self):
        print("Mover Abajo")

        #CONDICIONES ^
        
        # 0 Personaje, espacio 0,1 -> 1,0
        if (self.mapa[self.posicion_fila][self.posicion_columna] == 0
        and self.mapa[self.posicion_fila + 1] [self.posicion_columna] == 1 ): 

            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila + 1][self.posicion_columna] = 0
            self.posicion_fila += 1        

        # 1 Personaje, meta 0,4 -> 1,5
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0
        and self.mapa[self.posicion_fila + 1] [self.posicion_columna] == 4 ): 

            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila + 1][self.posicion_columna] = 5
            self.posicion_fila += 1       

        # 2 Personaje, caja, espacio 0,2,1 -> 1,0,2
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0
        and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 2
        and self.mapa[self.posicion_fila + 2][self.posicion_columna] == 1):

            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila + 1][self.posicion_columna] = 0
            self.mapa[self.posicion_fila + 2][self.posicion_columna] = 2
            self.posicion_fila += 1    

        # 3 Personaje, caja, meta 0,2,4 -> 1,0,6
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0
        and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 2
        and self.mapa[self.posicion_fila + 2][self.posicion_columna] == 4):

            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila + 1][self.posicion_columna] = 0
            self.mapa[self.posicion_fila + 2][self.posicion_columna] = 6
            self.posicion_fila += 1   

        # 4 Personaje, caja_meta, meta 0,6,1 -> 1,5,2
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0
        and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 6
        and self.mapa[self.posicion_fila + 2][self.posicion_columna] == 1):

            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila + 1][self.posicion_columna] = 5
            self.mapa[self.posicion_fila + 2][self.posicion_columna] = 2
            self.posicion_fila += 1                   

        # 5 Personaje, caja_meta, meta 0,6,4 -> 1,5,6
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 0
        and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 6 
        and self.mapa[self.posicion_fila + 2][self.posicion_columna] == 4):

            self.mapa[self.posicion_fila][self.posicion_columna] = 1
            self.mapa[self.posicion_fila + 1][self.posicion_columna] = 5 
            self.mapa[self.posicion_fila + 2][self.posicion_columna] = 6
            self.posicion_fila += 1                   

        # 6 Personaje_meta, espacio 5,1 -> 4,0
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila + 1] [self.posicion_columna] == 1 ): 

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila + 1][self.posicion_columna] = 0
            self.posicion_fila += 1

        # 7 Personaje_meta Personaje_meta, meta 5,4 -> 4,5
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila + 1] [self.posicion_columna] == 4 ): 

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila + 1][self.posicion_columna] = 5
            self.posicion_fila += 1        
      
        # 8 Personaje_meta, caja, espacio 5,2,1 -> 4,0,2
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 2
        and self.mapa[self.posicion_fila + 2][self.posicion_columna] == 1):

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila + 1][self.posicion_columna] = 0 
            self.mapa[self.posicion_fila + 2][self.posicion_columna] = 2
            self.posicion_fila += 1  

        # 9 Personaje_meta, caja, meta 5,2,4 -> 4,0,6
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 2 
        and self.mapa[self.posicion_fila + 2][self.posicion_columna] == 4):

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila + 1][self.posicion_columna] = 0
            self.mapa[self.posicion_fila + 2][self.posicion_columna] = 6
            self.posicion_fila += 1      

        # 10 Personaje_meta,caja_meta,espacio 5,6,4 -> 4,5,6
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5
        and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 6
        and self.mapa[self.posicion_fila + 2][self.posicion_columna] == 4):

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila + 1][self.posicion_columna] = 5
            self.mapa[self.posicion_fila + 2][self.posicion_columna] = 6
            self.posicion_fila += 1     

        # 11 Personaje_meta, caja_meta, meta 5,6,1 -> 4,5,2 
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5 
        and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 6
        and self.mapa[self.posicion_fila + 2][self.posicion_columna] == 1):

            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila + 1][self.posicion_columna] = 5
            self.mapa[self.posicion_fila + 2][self.posicion_columna] = 2
            self.posicion_fila += 1                  
#EJECUCIÓN DEL JUEGO    
   
    def jugar(self):

#ENCONTRAR LA POSICION
        self.leermapa()
        self.EncontrarPosicion() 
        
        instrucciones = "d-Derecha\na-Izquierda\nq-Cerrar Juego"
        print(instrucciones)
        
        while True:
            if juego.completado():
                print("acabado")
    
            self.EncontrarPosicion()  # Update the character position for new map  
            self.imprimirmapa()   
            print(
                "Personaje posicion: [{},{}]".format(
                    self.posicion_fila, self.posicion_columna
                )
            )
            movimiento = input("Mover hacia:")
            if movimiento == "d":
                self.moverDerecha()
                
            elif movimiento == "a":
                self.moverIzquierda()

            elif movimiento == "w":
                self.moverArriba()

            elif movimiento == "s":
                self.moverAbajo()
            
            elif movimiento == "q":
                print("Salir del juego")
                break
                    
juego = Sokoban()
juego.jugar()


