import pygame
import random

ROJO = (255,0,0)
ANCHO = 800
ALTO = 700

class Bola(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # OPCIÓN 1: Usar imagen 
        #try:
        #    self.image = pygame.image.load('imagenes/Moneda.png')
        #    self.image = pygame.transform.scale(self.image, (30, 30))
        #except pygame.error:
        #    print("No se pudo cargar bola.png. Usando figura geométrica.")
        #    self.image = pygame.Surface([30,30])
        #    pygame.draw.rect(self.image, ROJO, [0,0,30,30])
        
        # OPCIÓN 2: Usar figura geométrica
        self.image = pygame.Surface([30,30])
        pygame.draw.rect(self.image, ROJO, [0,0,30,30])
        
        self.rect = self.image.get_rect()
        self.velocidad = [random.randint(3,7),random.randint(4,8)]
    
    def posicionInicial(self):
        self.rect.x = (ANCHO/2) - 10
        self.rect.y = ALTO - 300

    def update(self):
        self.rect.x += self.velocidad[0]
        self.rect.y += self.velocidad[1]

    def rebotarX(self):
        self.velocidad[0] = -self.velocidad[0]

    def rebotarY(self):
        self.velocidad[1] = -self.velocidad[1]