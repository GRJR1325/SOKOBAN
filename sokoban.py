
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
    
    mapa = [3,1,1,1,0,1,1,2,1,1,4,3] 
    posicion_x = 4 #Posicion Inicial

    def __init__(self):
        pass

    def imprimirMapa(self):
        for i in self.mapa:
            if i == 0: #Muñeco
                print(chr(254), end = "")
            elif i == 1: #Espacio
                print (" ",end = "")
            elif i == 2: #Cajas
                print(chr(164),end = "")
            elif i == 3:  #Paredes
                print (chr(220),end = "")
            elif i == 4:  #Meta
                print (chr(109),end = "")
            elif i == 5:  #Muñeco_Meta
                print (chr(80),end = "")
            elif i == 6:  #Caja_Meta
                print (chr(100),end = "")
            else:
                print(i, end = "")
        print()

#CONFIGURACION DE MOVIMIENTOS
        
    #MOVIMIENTOS A LA DERECHA 
    def moverDerecha(self):
        self.posicion_x += 1 #Calcula la nueva posicion del muñeco 
        self.mapa[self.posicion_x] = 0 #Coloca el muñeco en la nueva posicion 
        self.mapa[self.posicion_x - 1] = 1 #Coloca el espacio donde va el muñeco

        #CONDICIONES--->
        # 0 Muñeco, espacio
        self.mapa[self.posicion_x+1]==1
        self.mapa[self.posicion_x]=1
        self.mapa[self.posicion_x+1]=0
        self.posicion_x += 1
        
        # 1 Muñeco, meta
        self.mapa[self.posicion_x+1]==1
        self.mapa[self.posicion_x]=1
        self.mapa[self.posicion_x+1]=5
        self.posicion_x += 1

    #MOVIMIENTOS A LA IZQUIERDA
    def moverIzquierda(self):
        self.posicion_x -= 1
        self.mapa[self.posicion_x] = 0 
        self.mapa[self.posicion_x + 1] = 1

        
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
        
#2 Muñeco, caja ,espacio
        self.mapa[self.posicion_fila] [self.posicion_columna]=1
        self.mapa[self.posicion_fila] [self.posicion_columna+1]=0
        self.posicion.columna += 1




#3 Muneco,caja,meta
if self.mapa[self.posicion_x]==0 and self.mapa[self.posicion_x+1]==2 and self.mapa[self.posicion_x+2]==4:
    self.mapa[self.posicion_x]=1
    self.mapa[self.posicion_x+1]=0
    self.mapa[self.posicion_x+2]=6
    self.posicion_x += 1

#6 Muñeco meta, caja, espacio
if self.mapa[self.posicion_x]==5 and self.mapa[self.posicion_x+1]==2 and self.mapa[self.posicion_x+2]==1:
    self.mapa[self.posicion_x]=4
    self.mapa[self.posicion_x+1]=0
    self.mapa[self.posicion_x+2]=2
    self.posicion_x += 1








    
