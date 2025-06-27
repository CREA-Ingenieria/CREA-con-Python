import pygame

NEGRO = (0,0,0)

class BloqueBase(pygame.sprite.Sprite):
    def __init__(self, color, puntos, nombre_imagen=None):
        super().__init__()
        
        # OPCIÓN 1: Usar imagen
        #if nombre_imagen:
        #    try:
        #        self.image = pygame.image.load(f'imagenes/{nombre_imagen}')
        #        self.image = pygame.transform.scale(self.image, (100, 20))
        #    except pygame.error:
        #        print(f"No se pudo cargar {nombre_imagen}. Usando color sólido.")
        #        self.image = pygame.Surface([100,20])
        #        pygame.draw.rect(self.image, color, [0,0,100,20])
        #        pygame.draw.rect(self.image, NEGRO, [0,0,100,20], 2)
        #else:
        #    self.image = pygame.Surface([100,20])
        #    pygame.draw.rect(self.image, color, [0,0,100,20])
        #    pygame.draw.rect(self.image, NEGRO, [0,0,100,20], 2)
        
        # OPCIÓN 2: Usar figuras geométricas
        self.image = pygame.Surface([100,20])
        pygame.draw.rect(self.image, color, [0,0,100,20])
        pygame.draw.rect(self.image, NEGRO, [0,0,100,20], 1)
        
        self.rect = self.image.get_rect()
        self.puntos = puntos

class BloqueA(BloqueBase):
    def __init__(self):
        NARANJA = (252, 111, 49)
        super().__init__(NARANJA, 4, 'Oro.png')

class BloqueB(BloqueBase):
    def __init__(self):
        ROSADO = (255, 102, 186)
        super().__init__(ROSADO, 3, 'Ladrillo.png')

class BloqueC(BloqueBase):
    def __init__(self):
        TURQUESA = (92, 225, 230)
        super().__init__(TURQUESA, 2, 'Piedra.png')

class BloqueD(BloqueBase):
    def __init__(self):
        MORADO = (203, 108, 230)
        super().__init__(MORADO, 1, 'Madera.png')