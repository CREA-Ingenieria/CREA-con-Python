import pygame

# ========== PASO 5: CREAR LOS BLOQUES ==========
# TODO: Define NEGRO = (0, 0, 0)
# NEGRO = (0, 0, 0)

# ========== CLASE BASE PARA LOS BLOQUES ==========
class BloqueBase(pygame.sprite.Sprite):
    def __init__(self, color, puntos, nombre_imagen):
        """Inicializa un bloque con color, puntos y posición"""
        super().__init__()
        
        # TODO: Opción 1 - Usar rectángulo de color (descomenta para usar)
        # self.image = pygame.Surface([100, 20])
        # pygame.draw.rect(self.image, color, [0, 0, 100, 20])
        # pygame.draw.rect(self.image, NEGRO, [0, 0, 100, 20], 1)
        
        # TODO: Opción 2 - Usar imagen personalizada (descomenta para usar)
        # Parámetro nombre_imagen contiene el archivo (ej: 'Oro.png', 'Ladrillo.png')
        # if nombre_imagen:
        #     try:
        #         self.image = pygame.image.load(f'imagenes/{nombre_imagen}')
        #         self.image = pygame.transform.scale(self.image, (100, 20))
        #     except pygame.error:
        #         print(f"No se pudo cargar {nombre_imagen}. Usando color.")
        #         self.image = pygame.Surface([100, 20])
        #         pygame.draw.rect(self.image, color, [0, 0, 100, 20])
        #         pygame.draw.rect(self.image, NEGRO, [0, 0, 100, 20], 1)
        # else:
        #     self.image = pygame.Surface([100, 20])
        #     pygame.draw.rect(self.image, color, [0, 0, 100, 20])
        #     pygame.draw.rect(self.image, NEGRO, [0, 0, 100, 20], 1)
        
        # VERSIÓN INICIAL: rectángulo de color
        self.image = pygame.Surface([100, 20])
        pygame.draw.rect(self.image, color, [0, 0, 100, 20])
        pygame.draw.rect(self.image, NEGRO, [0, 0, 100, 20], 1)
        
        # TODO: Crea el rectángulo de colisión
        self.rect = self.image.get_rect()
        
        # TODO: Guarda los puntos del bloque
        self.puntos = puntos

# ========== CLASES DE BLOQUES ESPECÍFICOS ==========
# TODO: Crea la clase BloqueA (naranja, 4 puntos)
# Debe heredar de BloqueBase
# color = (252, 111, 49)
# class BloqueA(BloqueBase):
#     def __init__(self):
#         super().__init__((252, 111, 49), 4, 'Oro.png')

# TODO: Crea la clase BloqueB (rosado, 3 puntos)
# class BloqueB(BloqueBase):
#     def __init__(self):
#         super().__init__((255, 102, 186), 3, 'Ladrillo.png')

# TODO: Crea la clase BloqueC (turquesa, 2 puntos)
# class BloqueC(BloqueBase):
#     def __init__(self):
#         super().__init__((92, 225, 230), 2, 'Piedra.png')

# TODO: Crea la clase BloqueD (morado, 1 punto)
# class BloqueD(BloqueBase):
#     def __init__(self):
#         super().__init__((203, 108, 230), 1, 'Madera.png')
