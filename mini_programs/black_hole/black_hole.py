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
GRAY = (169, 169, 169)

black_hole_pos = (WIDTH // 6, HEIGHT // 2)
black_hole_mass = 10**8
G = 6.67430e-11 * 1000  # Gravitational constant increased
zoom_level = 1.0
zoom_increment = 0.1


class Particle:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.mass = mass

    def update(self):
        dx = black_hole_pos[0] - self.x
        dy = black_hole_pos[1] - self.y
        dist = math.sqrt(dx**2 + dy**2)
        if dist < 5:
            dist = 5
        force = G * self.mass * black_hole_mass / (dist**2)
        force_x = force * (dx / dist)
        force_y = force * (dy / dist)
        self.vx += force_x
        self.vy += force_y
        self.x += self.vx
        self.y += self.vy
        if dist < 10:
            self.vx = self.vy = 0
            self.x, self.y = black_hole_pos

    def draw(self, surface, zoom_level):
        scaled_x = black_hole_pos[0] + (self.x - black_hole_pos[0]) * zoom_level
        scaled_y = black_hole_pos[1] + (self.y - black_hole_pos[1]) * zoom_level
        pygame.draw.circle(surface, WHITE, (int(scaled_x), int(scaled_y)), int(2 * zoom_level))


def generate_particles(num_particles):
    particles = []
    center_x, center_y = WIDTH * 4 // 5, HEIGHT // 2
    for _ in range(num_particles):
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(0, 200)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        mass = random.uniform(1, 10)
        particles.append(Particle(x, y, mass))
    return particles


particles = generate_particles(3000)


class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.active = False

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


def toggle_play_pause():
    global paused
    paused = not paused
    play_pause_button.text = "Pause" if not paused else "Play"


def restart():
    global particles
    particles = generate_particles(3000)


def handle_zoom(event):
    global zoom_level
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 4:  # Scroll up
            zoom_level += zoom_increment
        elif event.button == 5:  # Scroll down
            zoom_level -= zoom_increment
            if zoom_level < 0.1:
                zoom_level = 0.1


play_pause_button = Button("Pause", 50, 550, 100, 40, GRAY, YELLOW, toggle_play_pause)
restart_button = Button("Restart", 200, 550, 100, 40, GRAY, YELLOW, restart)

buttons = [play_pause_button, restart_button]

running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        handle_zoom(event)
        for button in buttons:
            if button.is_clicked(event):
                button.action()

    screen.fill(BLACK)

    scaled_black_hole_pos = (
        int(black_hole_pos[0] * zoom_level),
        int(black_hole_pos[1] * zoom_level)
    )
    pygame.draw.circle(screen, YELLOW, scaled_black_hole_pos, int(20 * zoom_level))

    if not paused:
        for particle in particles:
            particle.update()
    for particle in particles:
        particle.draw(screen, zoom_level)

    for button in buttons:
        button.draw(screen)

    pygame.display.flip()

pygame.quit()
