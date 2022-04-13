from os import system, name
class Sokoban:
 # REPRESENTACIÓN DEL COMPONENTE DEL JUEGO
 # 0 = Muñeco
 # 1 = Espacio
 # 2 = Cajas
 # 3 = Paredes
 # 4 = Metas
 # 5 = Muñeco_meta
 # 6 = Caja_meta
    
#CREACION DEL MAPA DE JUEGO     
    mapa = []
    posicion_fila = 0
    posicion_columna = 0
    inicia = True
    nivel = open ("nivel3.txt", "r")

    def __init__(self):
        pass 
        
    def leermapa(self): 
        for rug in self.nivel:
            columna = []
            for digito in rug:
                if digito == "\n":
                    continue
                columna.append(int(digito))
            self.mapa.append(columna)
            
    def imprimirmapa(self): 
        for fila in self.mapa: 
            for columna in fila: 
                if columna == 0: #Muñeco
                    print(chr(128515), end = "")
                elif columna == 1: #Espacio
                    print ("  ",end = "")                   
                elif columna == 2: #Cajas
                    print(chr(128230),end = "")                    
                elif columna == 3:  #Paredes
                    print (chr(129521),end = "")                    
                elif columna == 4:  #Meta 
                    print (chr(128681),end = "")                    
                elif columna == 5:  #Muñeco_Meta 
                    print (chr(128522),end = "")                    
                elif columna == 6:  #Caja_Meta
                    print (chr(127873),end = "")
                else:
                    print(columna, end = "")
            print()

    def EncontrarPosicion(self):
        for fila in range(len(self.mapa)):
            for columna in range(len(self.mapa[fila])):  
                if self.mapa[fila][columna] == 0:  
                    self.posicion_fila = fila  
                    self.posicion_columna = columna   

    def borrarpantalla(self):
        if name == "poo":
            system ("cls")
        else: 
            system("clear")
                            
#NIVEL COMPLETADO
    def terminado(self):
        cell=0
        for columna in self.mapa:
            for fila in columna:
                if fila == 2:
                    cell += 1
        return cell


            
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
            self.mapa[self.posicion_fila][self.posicion_columna + 2] = 6
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
        elif (self.mapa[self.posicion_fila][self.posicion_columna] == 5   
        and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 4):
            self.mapa[self.posicion_fila][self.posicion_columna] = 4
            self.mapa[self.posicion_fila][self.posicion_columna - 1] = 5 
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
        self.leermapa() # LEE EL .TXT
        self.EncontrarPosicion() # ENCUENTRA EL PERSONAJE
        
        nombre = input("¿Cual es tu nombre viajero?:")
        
        print(chr(129521),chr(129521),chr(129521),chr(129521),chr(129521),chr(129521),chr(129521),chr(129521),chr(129521),chr(129521),chr(129521),chr(129521))
        print("                                        ")
        print(f"     Bienvenido a sokoban {nombre}     ")
        print("                                        ")     
        print(chr(129521),chr(129521),chr(129521),chr(129521),chr(129521),chr(129521),chr(129521),chr(129521),chr(129521),chr(129521),chr(129521),chr(129521))

        print(f"Tu objetivo es muy simple {nombre} coloca todas las cajas dentro de las metas")
        input ()
        
        print(f"Para moverte {nombre} usa las siguientes teclas:\nd-Derecha\na-Izquierda\nw-Arriba\ns-Abajo\nq-Cerrar Juego")
        input()

        print(f"Te deseo suerte {nombre}  ")
        input ()
        
        print("Usa tu inteligencia para superar los retos que te esperan ;)")



        tecla = input("*Dos veces ENTER para iniciar tu aventura*:")
        if tecla == " ":
            self.borrarpantalla()
        
        input()
        self.borrarpantalla()
    
        while self.inicia == True:
            self.imprimirmapa()  
            print(
                "Personaje posicion: [{},{}]".format(  #MUESTRA PERSONAJE
                    self.posicion_fila, self.posicion_columna
                )
            )
            movimiento = input("Mover hacia:")
            if movimiento == "d":
                self.moverDerecha()
                self.borrarpantalla()
            elif movimiento == "a":
                self.moverIzquierda()
                self.borrarpantalla()
            elif movimiento == "w":
                self.moverArriba()
                self.borrarpantalla()
            elif movimiento == "s":
                self.moverAbajo()
                self.borrarpantalla()      
            elif movimiento == "wwssadad":
                print(chr(128142),chr(128142),chr(128142),chr(128142),chr(128142),chr(128142),chr(128142),chr(128142),chr(128142))
                print("                                        ")
                print(f"Juego Terminado\n created by José Rolando \nGRACIAS POR JUGAR {nombre} ")
                print("                                        ")
                print(chr(128142),chr(128142),chr(128142),chr(128142),chr(128142),chr(128142),chr(128142),chr(128142),chr(128142))
                break
            elif movimiento == "q":
                print("Juego Cerrado")
                break
            else:
                self.borrarpantalla()
                print("Tecla equivocada")

            if self.terminado() == 0:
                self.inicia = False
                self.borrarpantalla
                print(chr(127873),chr(127873),chr(127873),chr(127873),chr(127873),chr(127873),chr(127873),chr(127873),chr(127873),chr(127873),chr(127873),chr(127873),chr(127873))
                print("                                        ")
                print("JUEGO TERMINADO GRACIAS POR JUGAR :) ")
                print("                                        ")
                print(chr(127873),chr(127873),chr(127873),chr(127873),chr(127873),chr(127873),chr(127873),chr(127873),chr(127873),chr(127873),chr(127873),chr(127873),chr(127873))
                break

juego = Sokoban()
juego.jugar()