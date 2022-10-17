import random
import pygame
from sys import exit
test_words = []
width,height = 800,600
with open("wordlist.txt","r") as file:
	for line in file:
		test_words.append(str(line.strip()))
pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Helvetica",50)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			screen.fill((255,255,255))
			word_choice = random.randint(0,len(test_words)/2-1)*2
			screen.blit(font.render(test_words[word_choice],1,(0,0,0)),(width/2-font.render(test_words[word_choice],1,(0,0,0)).get_width()/2,height/2-font.render(test_words[word_choice],1,(0,0,0)).get_height()/2))
		if event.type == pygame.KEYDOWN :
			if event.key == pygame.K_s:
				screen.fill((255,255,255))
				if word_choice %2 == 0:
					word_choice += 1
				screen.blit(font.render(test_words[word_choice],1,(0,0,0)),(width/2-font.render(test_words[word_choice],1,(0,0,0)).get_width()/2,height/2-font.render(test_words[word_choice],1,(0,0,0)).get_height()/2))
		if event.type == pygame.KEYDOWN :
			if event.key == pygame.K_a:
				screen.fill((255,255,255))
				if word_choice %2 != 0:
					word_choice -= 1
				screen.blit(font.render(test_words[word_choice],1,(0,0,0)),(width/2-font.render(test_words[word_choice],1,(0,0,0)).get_width()/2,height/2-font.render(test_words[word_choice],1,(0,0,0)).get_height()/2))


		pygame.display.update()
		clock.tick(60)