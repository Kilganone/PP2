import pygame
import sys
import os
from player import MusicPlayer

pygame.init()

WIDTH, HEIGHT = 640, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Keyboard Music Player")

clock = pygame.time.Clock()

font_title = pygame.font.SysFont("arial", 36, bold=True)
font_text = pygame.font.SysFont("arial", 24)
font_small = pygame.font.SysFont("arial", 18)

music_dir = os.path.join(os.path.dirname(__file__), "music")
player = MusicPlayer(music_dir)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.prev_track()
            elif event.key == pygame.K_SPACE:
                player.toggle_pause()
            elif event.key == pygame.K_q:
                running = False

    player.update()
    info = player.get_info()

    screen.fill((25, 25, 30))

    # TITLE
    screen.blit(font_title.render("Music Player", True, (255, 255, 255)), (20, 20))

    # STATUS COLOR
    if info["status"] == "Playing":
        status_color = (50, 255, 50)
    elif info["status"] == "Paused":
        status_color = (255, 200, 50)
    else:
        status_color = (200, 200, 200)

    # TEXT INFO
    screen.blit(font_text.render(f"Track: {info['name']}", True, (200, 200, 200)), (20, 80))
    screen.blit(font_text.render(f"Status: {info['status']}", True, status_color), (20, 110))
    screen.blit(font_text.render(f"Time: {info['pos']:.1f}s", True, (200, 200, 200)), (20, 140))
    screen.blit(font_text.render(f"Playlist: {info['idx']} / {info['total']}", True, (200, 200, 200)), (20, 170))

    # PROGRESS BAR
    bar_x, bar_y, bar_w, bar_h = 20, 220, 400, 16

    pygame.draw.rect(screen, (60, 60, 60), (bar_x, bar_y, bar_w, bar_h), border_radius=8)

    progress = 0
    if info["total"] > 0:
        progress = min(info["pos"] / 240.0, 1.0)

    pygame.draw.rect(
        screen,
        (50, 200, 100),
        (bar_x, bar_y, bar_w * progress, bar_h),
        border_radius=8
    )

    # HINTS
    screen.blit(font_small.render(
        "P=Play | S=Stop | N=Next | B=Back | Space=Pause | Q=Quit",
        True,
        (150, 150, 150)
    ), (20, 320))

    screen.blit(font_small.render(
        "Add tracks to music/ folder",
        True,
        (100, 100, 100)
    ), (20, 350))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()