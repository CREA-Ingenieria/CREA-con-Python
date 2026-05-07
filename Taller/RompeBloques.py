import pygame
# from barra import Barra
# from bola import Bola
# from bloques import BloqueA, BloqueB, BloqueC, BloqueD

# ========== PASO 1: VENTANA VACÍA ==========
pygame.init()

# TODO: Define ANCHO = 800
ANCHO = 800

# TODO: Define ALTO = 600
ALTO = 600

# TODO: Crea la ventana con pygame.display.set_mode((ANCHO, ALTO))
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# TODO: Agrega el título con pygame.display.set_caption('Rompe Bloques')
pygame.display.set_caption('Rompe Bloques')

# ========== PASO 2: CAMBIAR COLOR DE FONDO ==========
# TODO: Define NEGRO = (0, 0, 0)
COLOR = (220, 220, 220)

# TODO: Define un color personalizado para el fondo
# color_fondo = (220, 220, 220)

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
    
FPS = 60


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
#todosLosSprites.add(bola)

# Grupo de bloques
todosLosBloques = pygame.sprite.Group()

# ========== PASO 4: CREAR LA BOLA ==========
# TODO: Descomenta la importación de Bola
# from bola import Bola

# TODO: Instancia la bola
# bola = Bola()
# bola.posicionInicial()

# ========== PASO 5: CREAR LOS BLOQUES ==========
# TODO: Descomenta las importaciones de bloques
# from bloques import BloqueA, BloqueB, BloqueC, BloqueD


# ========== PASO 6: INSTANCIAR BLOQUES ==========
# TODO: Crea una función instanciarBloques(columnas, filas)
# Debe crear bloques en una cuadrícula con ciclos for anidados
# def instanciarBloques(columnas, filas):
#     pass

# TODO: Llama la función para crear 7 columnas y 8 filas
# instanciarBloques(7, 8)

# ========== PASO 7: VIDAS Y PUNTUACIÓN ==========
# TODO: Define puntuacion = 0
# puntuacion = 0

# TODO: Define vidas = 3
# vidas = 3

# TODO: Define iniciar = False (controla si la bola se mueve)
# iniciar = False
# ========== BUCLE PRINCIPAL ==========
ejecutando = True
while ejecutando:
    # TODO: Maneja el evento QUIT para cerrar la ventana
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # ========== PASO 2: CAMBIAR COLOR DE FONDO ==========
    # TODO: Rellena la pantalla de negro con pantalla.fill(NEGRO)
    # O descomenta la siguiente línea para usar imagen de fondo:
    if fondo:
        pantalla.blit(fondo, (0, 0))
    else:
        pantalla.fill(COLOR)

    # ========== PASO 3-7: DIBUJAR SPRITES Y LÓGICA ==========
    # TODO: Descomenta para dibujar la barra y bola
    todosLosSprites.draw(pantalla)

    # TODO: Descomenta para manejar el movimiento de la barra
    # teclas = pygame.key.get_pressed()
    # if teclas[pygame.K_RIGHT]:
    #     barra.moverDerecha()
    # if teclas[pygame.K_LEFT]:
    #     COMPLETAR...

    # ========== PASO 7: MOSTRAR VIDAS Y PUNTUACIÓN ==========
    # TODO: Crea una fuente y muestra la puntuación
    # fuente = pygame.font.Font(None, 40)
    # texto = fuente.render(f'Puntuación: {puntuacion}', 1, NEGRO)
    # pantalla.blit(texto, (20, ALTO-30))

    # TODO: Muestra las vidas
    # texto = fuente.render(f'Vidas: {vidas}', 1, NEGRO)
    # pantalla.blit(texto, (ANCHO-120, ALTO-30))

    # ========== PASO 8: COLISIONES ==========
    # TODO: Implementa lógica de movimiento de bola (si iniciar == True)
    # TODO: Implementa rebotes en paredes
    # TODO: Implementa colisión bola-barra
    # TODO: Implementa colisión bola-bloques
    # TODO: Descomenta cuando tengas todas las piezas
    # if iniciar:
    #     todosLosSprites.update()
    #     # Rebotes en paredes...
    #     # Colisiones...


    pygame.display.update()
    
    reloj.tick(FPS)
    

# Cerrar el juego
pygame.quit()