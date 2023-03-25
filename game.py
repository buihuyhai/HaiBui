import pygame

pygame.init()

screen = pygame.display.set_mode((700,700))

GREY = (128,128,128)
WHILE = (255,255,255)
BLACK = (0,0,0)
while():
	screen.fill(GREY)
	mouse_x, mouse_y = pygame.mouse.get_pos()
	print(mouse_x)

	pygame.draw.rect(screen,WHITE,(100,50,50,50))
	pygame.draw.rect(screen,WHITE,(100,200,50,50))
	pygame.draw.rect(screen,WHITE,(200,50,50,50))
	pygame.draw.rect(screen,WHITE,(200,200,50,50))
	pygame.draw.rect(screen,WHITE,(300,50,150,50))
	pygame.draw.rect(screen,WHITE,(300,50,150,50))
	pygame.draw.rect(screen,WHITE,(300,1505,150,50))

	screen.blit(text_1,(100,50))
	screen.blit(text_2,(100,200))
	screen.blit(text_3,(200,50))
	screen.blit(text_4,(200,200))
	screen.blit(text_5,(300,50))
	screen.blit(text_6,(300,150))

	pygame.draw.rect(screen,BLACK,(50,520,400,50))
	pygame.draw.rect(screen,WHITE,(60,530,380,30))

	pygame.draw.circle(screen, BLACK,(250,400),100)
	pygame.draw.circle(screen, WHITE,(250,400),95)
	pygame.draw.circle(screen, BLACK,(250,400),5)

	pygame.draw.line(screen, BLACK, (250,400),(250,310))



	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				print()
	pygame.display.flip()
pygame.quit()