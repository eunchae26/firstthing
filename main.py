import pygame, sys
pygame.init()
s = pygame.display.set_mode((800,600))
p = pygame.Rect(375, 275, 50, 50)
b = []
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: pygame.quit(); sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            b.append(pygame.Rect(p.centerx, p.top, 10, 5))
    k = pygame.key.get_pressed()
    if k[pygame.K_LEFT]: p.x -= 5
    if k[pygame.K_RIGHT]: p.x += 5
    if k[pygame.K_UP]: p.y -= 5
    if k[pygame.K_DOWN]: p.y += 5
    for bullet in b[:]:
        bullet.x += 10
        if bullet.x > 800: b.remove(bullet)
    s.fill((0,0,0))
    pygame.draw.rect(s, (255,255,255), p)
    for bullet in b: pygame.draw.rect(s, (255,255,255), bullet)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
