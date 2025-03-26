import random

class ColorGenerator:
    def get_random_color():
        return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))