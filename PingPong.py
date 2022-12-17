import pygame

timer = pygame.time.Clock()
window = pygame.display.set_mode((500, 500))
window_hitbox = window.get_rect()

class GameObject():
    def __init__ (self, x, y, w, h, speed_x, speed_y, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color
        self.image = pygame.Surface((w, h))
        self.image.fill(color)

class Ball(GameObject):
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.right > window_hitbox.right:
            self.speed_x = -self.speed_x
        if self.rect.x < window_hitbox.left:
            self.speed_x = -self.speed_x
        if self.rect.bottom > window_hitbox.bottom:
            self.speed_y = -self.speed_y
        if self.rect.y < window_hitbox.top:
            self.speed_y = -self.speed_y
        #if player.rect.colliderect(self.rect):
            #self.speed_y = -self.speed_y

class Player(GameObject):
    def keyboard(self):
        buttons = pygame.key.get_pressed()
        if buttons[pygame.K_w] == True:
            self.rect.y -= self.speed_y
        if buttons[pygame.K_s] == True:
            self.rect.y += self.speed_y

ball = Ball(0, 0, 30, 30, 2, 1, (255, 0, 0))
player = Player(0, 0, 10, 100, 0, 3, (255, 0, 0))

while True:
    window.fill((0, 255, 0))
    events_list = pygame.event.get()
    for event in events_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    window.blit(ball.image, ball.rect)
    window.blit(player.image, player.rect)
    ball.move()
    player.keyboard()
    timer.tick(60)
    pygame.display.update()