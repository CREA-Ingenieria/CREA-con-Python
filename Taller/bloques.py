import pygame

# ========== PASO 5: CREAR LOS BLOQUES ==========
# TODO: Define NEGRO = (0, 0, 0)
NEGRO = (0, 0, 0)

# ========== CLASE BASE PARA LOS BLOQUES ==========
class BloqueBase(pygame.sprite.Sprite):
    def __init__(self, color, puntos, nombre_imagen):
        """Inicializa un bloque con color, puntos y posición"""
        super().__init__()
        
        # OPCIÓN 1: Usar figuras geométricas
        self.image = pygame.Surface([100,20])
        pygame.draw.rect(self.image, color, [0,0,100,20])
        pygame.draw.rect(self.image, NEGRO, [0,0,100,20], 1)
        
        # OPCIÓN 2: Usar imagen
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
        
        self.rect = self.image.get_rect()
        self.puntos = puntos

# ========== CLASES DE BLOQUES ESPECÍFICOS ==========
# TODO: Crea la clase BloqueA (naranja, 4 puntos)

class BloqueA(BloqueBase):
    def __init__(self):
        NARANJA = (252, 111, 49)
        super().__init__(NARANJA, 4, 'Oro.png')

# TODO: Crea la clase BloqueB (rosado, 3 puntos)


# TODO: Crea la clase BloqueC (turquesa, 2 puntos)


# TODO: Crea la clase BloqueD (morado, 1 punto)

