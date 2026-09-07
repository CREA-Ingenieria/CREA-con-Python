import pygame
# from barra import Barra
# from bola import Bola
# from bloques import BloqueA, BloqueB, BloqueC, BloqueD

# ========== PASO 1: VENTANA VACÍA ==========
pygame.init()

# TODO: Define ANCHO = 800
ANCHO = 200

# TODO: Define ALTO = 600
ALTO = 100

# TODO: Define Velocidad (FPS) = 60
FPS = 20

# TODO: Crea la ventana con pygame.display.set_mode((ANCHO, ALTO))
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# TODO: Agrega el título con pygame.display.set_caption('Rompe Bloques')
pygame.display.set_caption('Rompe Bloques')

# ========== PASO 2: CAMBIAR COLOR DE FONDO ==========
# TODO: Define NEGRO = (0, 0, 0)
COLOR = (220, 220, 220)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# ========== PASO 2b: CARGAR IMAGEN DE FONDO (OPCIONAL) ==========
# TODO: Descomenta estas líneas para cargar una imagen de fondo
# Reemplaza 'imagenes/fondo.png' con la ruta de tu imagen

fondo = None
#try:
#    fondo = pygame.image.load('imagenes/CREA_AMARILLO.png')
    # Escalar la imagen para que se ajuste al tamaño de la pantalla
#    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
#except pygame.error:
#    print("No se pudo cargar la imagen de fondo. Usando color sólido.")
#    fondo = None
    


reloj = pygame.time.Clock()

# ========== PASO 3: CREAR LA BARRA ==========
# TODO: Descomenta la importación de Barra
#from barra import Barra

# TODO: Instancia la barra
#barra = Barra()
#barra.rect.x = (ANCHO/2) - 60
#barra.rect.y = ALTO - 60

# Grupo de sprites
todosLosSprites = pygame.sprite.Group()
#todosLosSprites.add(barra)

# Grupo de bloques
todosLosBloques = pygame.sprite.Group()

# ========== PASO 4: CREAR LA BOLA ==========
# TODO: Descomenta la importación de Bola
# from bola import Bola

# TODO: Instancia la bola
# bola = Bola()
# bola.posicionInicial()
#todosLosSprites.add(bola)

# ========== PASO 5: CREAR LOS BLOQUES ==========
# TODO: Descomenta las importaciones de bloques
#from bloques import BloqueA, BloqueB, BloqueC, BloqueD


# ========== PASO 6: INSTANCIAR BLOQUES ==========
# Instanciar Bloques

#def instanciarBloques(c, r):
#    for i in range(c):
#        for j in range(r):
#            # Determinar el tipo de bloque según la fila
#            if j == 0 or j == 1:  # Filas 1 y 2
#                bloque = BloqueA()
#            elif j == 2 or j == 3:  # Filas 3 y 4
#                bloque = BloqueB()
#            elif j == 4 or j == 5:  # Filas 5 y 6
#                bloque = BloqueC()
#            else:  # Filas 7 y 8
#                bloque = BloqueD()
            
#            bloque.rect.x = 20 + i*110
#            bloque.rect.y = 20 + j*30
#            todosLosBloques.add(bloque)
#            todosLosSprites.add(bloque)

#instanciarBloques(7, 8)

#def eliminarBloques():
#    for bloque in todosLosBloques:
#        bloque.kill()


# TODO: Llama la función para crear 7 columnas y 8 filas
#instanciarBloques(7, 8)

# ========== PASO 7: VIDAS Y PUNTUACIÓN ==========
# TODO: Define puntuacion = 0
#puntuacion = 0

# TODO: Define vidas = 3
#vidas = 3

# TODO: Define iniciar = False (controla si la bola se mueve)
#iniciar = False

# Agregar efectos de sonido (opcional)
sonidoBloque = None
sonidoPerder = None
"""
try:
    sonidoBloque = pygame.mixer.Sound('sonidos/Brick.wav')
    sonidoPerder = pygame.mixer.Sound('sonidos/Downer01.wav')
except pygame.error:
    print("No se pudieron cargar los archivos de sonido.")
    sonidoBloque = None
    sonidoPerder = None
    """
# ========== BUCLE PRINCIPAL ==========
ejecutando = True
while ejecutando:
    # TODO: Maneja el evento QUIT para cerrar la ventana
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False


    if fondo:
        pantalla.blit(fondo, (0, 0))
    else:
        pantalla.fill(COLOR)

    # ========== PASO 3-7: DIBUJAR SPRITES Y LÓGICA ==========
    # TODO: Descomenta para dibujar la barra y bola
    todosLosSprites.draw(pantalla)

    """
    # TODO: Descomenta para manejar el movimiento de la barra
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_SPACE]:
            iniciar = True
    if teclas[pygame.K_RIGHT]:
        barra.moverDerecha()
    if teclas[pygame.K_LEFT]:
        COMPLETAR...

    # ========== PASO 7: MOSTRAR VIDAS Y PUNTUACIÓN ==========
    # Puntuación
    
    fuente = pygame.font.Font(None, 40)
    texto = fuente.render(f'Puntuación: {puntuacion}', 1, NEGRO)
    pantalla.blit(texto, (20, ALTO-30))
    # Vidas
    fuente = pygame.font.Font(None, 40)
    texto = fuente.render(f'Vidas: {vidas}', 1, NEGRO)
    pantalla.blit(texto, (ANCHO-120, ALTO-30))

    if vidas == 0:
        fuente = pygame.font.Font(None, 40)
        texto = fuente.render(f'JUEGO TERMINADO', 1, NEGRO)
        pantalla.blit(texto, (ANCHO/3, 350))
        fuente = pygame.font.Font(None, 40)
        texto = fuente.render(f'PRESIONA ESPACIO PARA JUGAR', 1, NEGRO)
        pantalla.blit(texto, (ANCHO/5, 450))
    if len(todosLosBloques) == 0:
        fuente = pygame.font.Font(None, 40)
        texto = fuente.render(f'¡GANASTE!', 1, NEGRO)
        pantalla.blit(texto, (ANCHO-480, 350))
        bola.posicionInicial()
        iniciar = False

    if iniciar:
        # Actualizar los Sprites
        todosLosSprites.update()
        if vidas == 0:
            vidas = 3
            puntuacion = 0
            eliminarBloques()
            instanciarBloques(7, 8)
        if bola.rect.right >= ANCHO or bola.rect.left <= 0:
            bola.rebotarX()
        if bola.rect.top <= 0:
            bola.rebotarY()
        if bola.rect.y >= ALTO - 40:
            if sonidoPerder:
                sonidoPerder.play()
            bola.posicionInicial()
            vidas -= 1
            iniciar = False

        # Colisión con la barra
        if bola.rect.colliderect(barra.rect):
            if abs(barra.rect.top - bola.rect.bottom) < 8:
                bola.rebotarY()
            if abs(barra.rect.left - bola.rect.right) < 8 or abs(barra.rect.right - bola.rect.left) < 8:
                bola.rebotarX()
        
        # Colisión con los bloques
        bolaImpactoLista = pygame.sprite.spritecollide(bola, todosLosBloques, False)
        for bloque in bolaImpactoLista:
            if sonidoBloque:
                sonidoBloque.play()
            bola.rebotarY()
            # Sumar puntos según el tipo de bloque
            puntuacion += bloque.puntos
            bloque.kill()
    """
    pygame.display.update()
    
    reloj.tick(FPS)
    

# Cerrar el juego
pygame.quit()