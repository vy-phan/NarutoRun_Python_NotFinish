import pygame

pygame.init()
running = True
screenWidth = 564*2
screenHeigth = 317*2
pygame.display.set_caption("Naruto Run MoCoi")
clock = pygame.time.Clock()
movement_speed = 15
gravity = 1
jump_height = 20 
velocity = 0
isJumpping = False

screen = pygame.display.set_mode((screenWidth,screenHeigth))

bg = pygame.transform.scale2x(pygame.image.load('./IMG/back.jpg').convert())

char = pygame.image.load('./IMG/naruto.jpg').convert()
char_pos_x = 100 
char_pos_y = 550
char_rect = char.get_rect(center = (char_pos_x,char_pos_y))

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False 
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			running = False 	
		if event.type == pygame.KEYDOWN:
			# if event.key == pygame.K_a:
			# 	char_pos_x -= movement_speed	
			# if event.key == pygame.K_d:
			# 	char_pos_x += movement_speed
			# if event.key == pygame.K_w:
			# 	char_pos_y -= movement_speed
			# if event.key == pygame.K_s:
			# 	if char_pos_y + movement_speed <= 550: 
			# 		char_pos_y += movement_speed

			if event.key == pygame.K_LEFT:
				if char_pos_x + movement_speed > 10:
					char_pos_x -= movement_speed	
			if event.key == pygame.K_RIGHT:
				if char_pos_x + movement_speed < screenWidth - 35: 
					char_pos_x += movement_speed
			if event.key == pygame.K_UP:
				if char_pos_y + movement_speed > 10:
					char_pos_y -= movement_speed
			if event.key == pygame.K_DOWN:
				if char_pos_y + movement_speed <= 550: 
					char_pos_y += movement_speed
		# if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not isJumpping:
		# 	isJumpping = True
		# 	velocity = jump_height				

		# if isJumpping:
		# 	char_pos_y -= velocity
		# 	velocity -= gravity
		# 	if velocity < - jump_height:
		# 		isJumpping = False
		# 		velocity = 0
		# else:
		# 	char_pos_y -= velocity 
		# 	velocity -= gravity

	char_rect.center = (char_pos_x, char_pos_y)
	screen.fill((0, 0, 0))
	screen.blit(bg,(0,0))
	screen.blit(char,(char_pos_x,char_pos_y))
	
	pygame.display.update()
	clock.tick(60)
pygame.quit()