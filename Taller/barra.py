import pygame

# ========== PASO 3: CREAR LA BARRA ==========
# TODO: Define NEGRO = (0, 0, 0)
NEGRO = (0, 0, 0)

# TODO: Define ANCHO = 800
ANCHO = 800

# TODO: Define ALTO = 600 (o el valor que uses en RompeBloques.py)
ALTO = 600

# ========== CLASE BARRA ==========
class Barra(pygame.sprite.Sprite):
    def __init__(self):
        """Inicializa la barra (su imagen y posición en pantalla)"""
        super().__init__()

        # TODO: Opción 1 - Usar rectángulo de color (descomenta para usar)
        self.image = pygame.Surface([120, 20])
        pygame.draw.rect(self.image, NEGRO, [0, 0, 120, 20])
        
        # TODO: Opción 2 - Usar imagen personalizada (descomenta para usar)
        # Reemplaza 'imagenes/barra.png' con la ruta de tu imagen
        
        #try:
        #    self.image = pygame.image.load('imagenes/barra.png')
        #    self.image = pygame.transform.scale(self.image, (120, 20))
        #except pygame.error:
        #    print("No se pudo cargar barra.png. Usando rectángulo.")
        #    self.image = pygame.Surface([120, 20])
        #    pygame.draw.rect(self.image, NEGRO, [0, 0, 120, 20])
        
        self.rect = self.image.get_rect()

    def moverDerecha(self):
        self.rect.x += 10
        if self.rect.x >= (ANCHO - 120):
            self.rect.x = ANCHO - 120

    def moverIzquierda(self):
        self.rect.x -= 10
        if self.rect.x <= 0:
            self.rect.x = 0