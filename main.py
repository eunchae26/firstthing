import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple FPS")
clock = pygame.time.Clock()

# 플레이어 사각형
player = pygame.Rect(375, 275, 50, 50)
bullets = []

# 메인 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 마우스 클릭 -> 총알 추가
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            bullet = pygame.Rect(player.centerx, player.top, 10, 5)
            bullets.append(bullet)

    # 키보드 입력
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= 5
    if keys[pygame.K_RIGHT]: player.x += 5
    if keys[pygame.K_UP]: player.y -= 5
    if keys[pygame.K_DOWN]: player.y += 5

    # 총알 이동
    for bullet in bullets[:]:
        bullet.x += 10
        if bullet.x > 800:
            bullets.remove(bullet)

    # 화면 그리기
    screen.fill((0, 0, 0))  # 배경색
    pygame.draw.rect(screen, (255, 255, 255), player)  # 플레이어
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 255), bullet)  # 총알

    pygame.display.flip()
    clock.tick(60)
