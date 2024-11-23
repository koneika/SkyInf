import pygame

pygame.init()

# Инициализация экрана
screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)

# Настройки текста
font = pygame.font.Font(None, 36)  # Шрифт и размер текста
text = font.render("Hello, Pygame!", True, (255, 255, 255))  # Создание текста (белого цвета)
text_rect = text.get_rect(center=(400, 300))  # Позиционируем текст по центру экрана

# Основной цикл программы
running = True
while running:
    screen.fill((0, 0, 0))  # Заполняем экран черным цветом

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отрисовка текста на экране
    screen.blit(text, text_rect)

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
