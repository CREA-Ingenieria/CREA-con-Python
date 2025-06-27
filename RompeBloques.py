import pygame
from barra import Barra
from bola import Bola
from bloques import BloqueA, BloqueB, BloqueC, BloqueD

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
ANCHO = 800
ALTO = 700
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Rompe Bloques')

puntuacion = 0
vidas = 3

# Definir los colores
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (50,100,200)
TURQUESA = (92, 225, 230)
GRIS = (220,220,220)
ROSADO = (255, 102, 186)
AMARILLO = (255, 222, 88)
MORADO = (203, 108, 230)

# Cargar imagen de fondo
try:
    fondo = pygame.image.load('imagenes/CREA_AMARILLO.png')
    # Escalar la imagen para que se ajuste al tamaño de la pantalla
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
except pygame.error:
    print("No se pudo cargar la imagen de fondo. Usando color sólido.")
    fondo = None

# Configurar el reloj
FPS = 60
reloj = pygame.time.Clock()

# Instanciar la barra
barra = Barra()
barra.rect.x = (ANCHO/2) - 60
barra.rect.y = ALTO - 60

# Instanciar la bola
bola = Bola()
bola.posicionInicial()

# Grupo de sprites
todosLosSprites = pygame.sprite.Group()
todosLosSprites.add(barra)
todosLosSprites.add(bola)

# Grupo de bloques
todosLosBloques = pygame.sprite.Group()

# Instanciar Bloques
def instanciarBloques(c, r):
    for i in range(c):
        for j in range(r):
            # Determinar el tipo de bloque según la fila
            if j == 0 or j == 1:  # Filas 1 y 2
                bloque = BloqueA()
            elif j == 2 or j == 3:  # Filas 3 y 4
                bloque = BloqueB()
            elif j == 4 or j == 5:  # Filas 5 y 6
                bloque = BloqueC()
            else:  # Filas 7 y 8
                bloque = BloqueD()
            
            bloque.rect.x = 20 + i*110
            bloque.rect.y = 20 + j*30
            todosLosBloques.add(bloque)
            todosLosSprites.add(bloque)

instanciarBloques(7, 8)

def eliminarBloques():
    for bloque in todosLosBloques:
        bloque.kill()

# Agregar efectos de sonido
try:
    sonidoBloque = pygame.mixer.Sound('sonidos/Brick.wav')
    sonidoPerder = pygame.mixer.Sound('sonidos/Downer01.wav')
except pygame.error:
    print("No se pudieron cargar los archivos de sonido.")
    sonidoBloque = None
    sonidoPerder = None

# Bucle principal
iniciar = False
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Dibujar fondo
    if fondo:
        pantalla.blit(fondo, (0, 0))
    else:
        pantalla.fill(GRIS)

    # Dibujar los sprites
    todosLosSprites.draw(pantalla)

    # Manejar eventos de teclado
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_SPACE]:
        iniciar = True
    if teclas[pygame.K_RIGHT]:
        barra.moverDerecha()
    if teclas[pygame.K_LEFT]:
        barra.moverIzquierda()

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
        pantalla.blit(texto, (ANCHO/4, 350))
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

    # Dibujar una línea
    pygame.draw.line(pantalla, NEGRO, [0, ALTO-35], [ANCHO, ALTO-35], 5)

    # Actualizar la pantalla
    pygame.display.update()

    # Controlar el reloj
    reloj.tick(FPS)

# Cerrar el juego
pygame.quit()