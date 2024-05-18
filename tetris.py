#coding : utf-8
# code by satt105 alias Thomas Bouret
# Date : 18/05/2024
# Prototyping of a Tetris game in Python with Pygame

import pygame
import random

pygame.init()

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
JAUNE = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)

taille_case = 30
grille = [[NOIR] * 10 for _ in range(20)]
largeur_grille = 10
hauteur_grille = 20

largeur_fenetre = largeur_grille * taille_case
hauteur_fenetre = hauteur_grille * taille_case
pieces = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]

# Classe pour représenter une pièce
class Piece:
    def __init__(self):
        self.x = 4
        self.y = 0
        self.forme = random.choice(pieces)
        self.couleur = random.choice([ROUGE, VERT, BLEU, JAUNE, CYAN, MAGENTA, ORANGE])

    def tourner(self):
        self.forme = list(zip(*self.forme[::-1]))

    def descendre(self):
        self.y += 1

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def afficher(self):
        for i in range(len(self.forme)):
            for j in range(len(self.forme[i])):
                if self.forme[i][j] == 1:
                    pygame.draw.rect(fenetre, self.couleur, (self.x * taille_case + j * taille_case, self.y * taille_case + i * taille_case, taille_case, taille_case))

    def est_collision(self):
        for i in range(len(self.forme)):
            for j in range(len(self.forme[i])):
                if self.forme[i][j] == 1:
                    if self.y + i >= 20 or self.x + j < 0 or self.x + j >= 10 or grille[self.y + i][self.x + j] != NOIR:
                        return True
        return False

    def fixer(self):
        for i in range(len(self.forme)):
            for j in range(len(self.forme[i])):
                if self.forme[i][j] == 1:
                    grille[self.y + i][self.x + j] = self.couleur

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Tetris")

def jeu():
    piece = Piece()
    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    piece.gauche()
                    if piece.est_collision():
                        piece.droite()
                elif event.key == pygame.K_RIGHT:
                    piece.droite()
                    if piece.est_collision():
                        piece.gauche()
                elif event.key == pygame.K_DOWN:
                    piece.descendre()
                    if piece.est_collision():
                        piece.y -= 1
                        piece.fixer()
                        piece = Piece()
                elif event.key == pygame.K_UP:
                    piece.tourner()
                    if piece.est_collision():
                        piece.tourner()

        piece.descendre()
        if piece.est_collision():
            piece.y -= 1
            piece.fixer()
            piece = Piece()

        fenetre.fill(BLANC)
        for i in range(len(grille)):
            for j in range(len(grille[i])):
                pygame.draw.rect(fenetre, grille[i][j], (j * taille_case, i * taille_case, taille_case, taille_case))
        piece.afficher()
        pygame.display.update()
        clock.tick(8)

    pygame.quit()
jeu()
