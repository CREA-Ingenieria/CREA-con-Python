import pygame
import random

# ========== PASO 4: CREAR LA BOLA ==========
# TODO: Define ROJO = (255, 0, 0)
# ROJO = (255, 0, 0)

# TODO: Define ANCHO = 800
# ANCHO = 800

# TODO: Define ALTO = 600 (o el valor que uses en RompeBloques.py)
# ALTO = 600

# ========== CLASE BOLA ==========
class Bola(pygame.sprite.Sprite):
    def __init__(self):
        """Inicializa la bola con imagen, velocidad y posición"""
        super().__init__()

        # TODO: Crea la imagen de la bola (cuadrado de 30x30 píxeles rojo)
        self.image = pygame.Surface([30, 30])
        pygame.draw.rect(self.image, ROJO, [0, 0, 30, 30])
        
        # TODO: Crea el rectángulo de colisión
        self.rect = self.image.get_rect()
        
        # TODO: Define la velocidad de la bola
        # Puede ser aleatoria: [random.randint(3, 7), random.randint(4, 8)]
        # O fija: [5, 5]
        # self.velocidad = [5, 5]
    
    # TODO: Crea la función posicionInicial()
    # Debe posicionar la bola en el centro horizontal y más arriba
    # Usa self.rect.x = (ANCHO / 2) - 10
    # y self.rect.y = ALTO - 300
    # def posicionInicial(self):
    #     pass

    # TODO: Crea la función update()
    # Debe mover la bola sumando su velocidad a su posición
    # self.rect.x += self.velocidad[0]
    # self.rect.y += self.velocidad[1]
    # def update(self):
    #     pass

    # TODO: Crea la función rebotarX()
    # Debe invertir la velocidad horizontal
    # self.velocidad[0] = -self.velocidad[0]
    # def rebotarX(self):
    #     pass

    # TODO: Crea la función rebotarY()
    # Debe invertir la velocidad vertical
    # self.velocidad[1] = -self.velocidad[1]
    # def rebotarY(self):
    #     pass
