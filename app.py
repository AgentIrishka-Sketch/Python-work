from p5 import *

particles = []

class Particle:
    def __init__(self):
        self.x = random_uniform(0, width)
        self.y = random_uniform(0, height)
        self.vx = 0
        self.vy = 0

    def update(self):
        dx = mouse_x - self.x
        dy = mouse_y - self.y
        
        self.vx += dx * 0.001
        self.vy += dy * 0.001
        
        self.vx *= 0.95
        self.vy *= 0.95
        
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        circle((self.x, self.y), 5)

def setup():
    size(600, 600)
    for _ in range(200):
        particles.append(Particle())

def draw():
    background(10, 10, 30)
    
    fill(0, 200, 255)
    no_stroke()
    
    for p in particles:
        p.update()
        p.draw()

run()
