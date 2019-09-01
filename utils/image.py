import pygame
pygame.font.init()
	
def draw_image(text, img_file_name, font_size=20):
	texts = text.split('\n')
	rtexts = []
	font = pygame.font.Font("Monaco.ttf", font_size)
	#font = pygame.font.Font("MSYHMONO.ttf", font_size)
	max_width, total_height = 0, 0
	for text in texts:
		surf = font.render(text, True, (0, 0, 0), (255 ,255 ,255))
		max_width = max(max_width, surf.get_width())
		total_height = total_height + surf.get_height()
		rtexts.append(surf)
	surf = pygame.Surface((max_width, total_height))
	surf.fill((255,255,255))
	total_height = 0
	for rtext in rtexts:
		surf.blit(rtext, (0, total_height))
		total_height += rtext.get_height()
	pygame.image.save(surf, img_file_name)