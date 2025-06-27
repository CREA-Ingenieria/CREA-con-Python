import pygame

NEGRO = (0,0,0)
ANCHO = 800
ALTO = 700

class Barra(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # OPCIÓN 1: Usar imagen 
        #try:
        #    self.image = pygame.image.load('imagenes/BarraLadrillos.png')
        #    self.image = pygame.transform.scale(self.image, (120, 20))
        #except pygame.error:
        #    print("No se pudo cargar barra.png. Usando figura geométrica.")
        #    self.image = pygame.Surface([120,20])
        #    pygame.draw.rect(self.image, NEGRO,[0,0,120,20])
        
        # OPCIÓN 2: Usar figura geométrica (comentar si usas OPCIÓN 1)
        self.image = pygame.Surface([120,20])
        pygame.draw.rect(self.image, NEGRO,[0,0,120,20])
        
        self.rect = self.image.get_rect()

    def moverDerecha(self):
        self.rect.x += 10
        if self.rect.x >= (ANCHO - 120):
            self.rect.x = ANCHO - 120

    def moverIzquierda(self):
        self.rect.x -= 10
        if self.rect.x <= 0:
            self.rect.x = 0