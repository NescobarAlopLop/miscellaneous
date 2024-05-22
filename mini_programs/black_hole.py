import pygame
import random
import math

pygame.init()


WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Massive Black Hole Simulation")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 140, 0)
RED = (255, 0, 0)
GRAY = (169, 169, 169)
BLUE = (0, 0, 255)


black_hole_pos = (WIDTH // 6, HEIGHT // 2)
black_hole_mass = 10**8  # Increased mass for stronger gravitational pull
G = 6.67430e-11  # Gravitational constant


class Particle:
    def __init__(self, x, y, mass, color):
        self.x = x
        self.y = y
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.mass = mass
        self.color = color

    def update(self):
        dx = black_hole_pos[0] - self.x
        dy = black_hole_pos[1] - self.y
        dist = math.sqrt(dx**2 + dy**2)
        if dist < 5:  # Avoid particles getting stuck in the center
            dist = 5
        force = G * self.mass * black_hole_mass / (dist**2 if dist > 1 else 1)

        force_x = force * (dx / dist)
        force_y = force * (dy / dist)

        self.vx += force_x
        self.vy += force_y

        self.x += self.vx
        self.y += self.vy

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 2)


def generate_particles(num_particles):
    particles = []
    center_x, center_y = WIDTH * 4 // 5, HEIGHT // 2
    for _ in range(num_particles):
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(0, 200)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        mass = random.uniform(1, 10)
        color = (
            random.randint(100, 255),
            random.randint(0, 150),
            random.randint(0, 150),
        )
        particles.append(Particle(x, y, mass, color))
    return particles


particles = generate_particles(3000)


class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.action = action

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, self.hover_color, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if self.action:
                self.action()


def play():
    global paused
    paused = False


def pause():
    global paused
    paused = True


def restart():
    global particles
    particles = generate_particles(3000)


play_button = Button("Play", 50, 550, 100, 40, GRAY, YELLOW, play)
pause_button = Button("Pause", 200, 550, 100, 40, GRAY, YELLOW, pause)
restart_button = Button("Restart", 350, 550, 100, 40, GRAY, YELLOW, restart)

buttons = [play_button, pause_button, restart_button]

running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for button in buttons:
            if button.is_clicked(event):
                button.action()

    screen.fill(BLACK)

    pygame.draw.circle(screen, YELLOW, black_hole_pos, 20)

    if not paused:
        for particle in particles:
            particle.update()
    for particle in particles:
        particle.draw()

    for button in buttons:
        button.draw(screen)

    pygame.display.flip()

pygame.quit()
