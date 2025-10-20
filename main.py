import pygame
import sys
from math import *

# Initialization of Pygame
pygame.init()

width = 400
height = 400
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Colors
background = (21, 67, 96)
border = (208, 211, 212)
red = (231, 76, 60)
white = (244, 246, 247)
violet = (136, 78, 160)
yellow = (244, 208, 63)
green = (88, 214, 141)

playerColor = [red, green, violet, yellow]

font = pygame.font.SysFont("Times New Roman", 30)

blocks = 40
noPlayers = 4

pygame.display.set_caption(f"Chain Reaction {noPlayers} Player")

score = [0] * noPlayers
players = playerColor[:noPlayers]

d = blocks // 2 - 2

cols = width // blocks
rows = height // blocks

grid = []

# Quit or Close the Game Window
def close():
    pygame.quit()
    sys.exit()

# Class for Each Spot in Grid
class Spot:
    def __init__(self):
        self.color = border
        self.neighbors = []
        self.noAtoms = 0

    def addNeighbors(self, i, j):
        if i > 0:
            self.neighbors.append(grid[i - 1][j])
        if i < cols - 1:
            self.neighbors.append(grid[i + 1][j])
        if j > 0:
            self.neighbors.append(grid[i][j - 1])
        if j < rows - 1:
            self.neighbors.append(grid[i][j + 1])

# Initialize Grid
def initializeGrid():
    global grid, score, players
    score = [0] * noPlayers
    players = playerColor[:noPlayers]
    grid = [[] for _ in range(cols)]
    for i in range(cols):
        for j in range(rows):
            newObj = Spot()
            grid[i].append(newObj)
    for i in range(cols):
        for j in range(rows):
            grid[i][j].addNeighbors(i, j)

# Draw the Grid
def drawGrid(currentIndex):
    for x in range(0, width, blocks):
        pygame.draw.line(display, players[currentIndex], (x, 0), (x, height))
    for y in range(0, height, blocks):
        pygame.draw.line(display, players[currentIndex], (0, y), (width, y))

# Show Current Grid
def showPresentGrid(vibrate=1):
    for i in range(cols):
        for j in range(rows):
            x = i * blocks
            y = j * blocks
            cell = grid[i][j]

            if cell.noAtoms == 0:
                cell.color = border
            elif cell.noAtoms == 1:
                pygame.draw.ellipse(display, cell.color, (x + blocks/2 - d/2 + vibrate, y + blocks/2 - d/2, d, d))
            elif cell.noAtoms == 2:
                pygame.draw.ellipse(display, cell.color, (x + 5, y + blocks/2 - d/2 - vibrate, d, d))
                pygame.draw.ellipse(display, cell.color, (x + blocks/2 + vibrate, y + blocks/2 - d/2, d, d))
            elif cell.noAtoms == 3:
                for angle in [90, 180, 270]:
                    cx = x + blocks/2 - d/2 + (d/2)*cos(radians(angle))
                    cy = y + blocks/2 - d/2 + (d/2)*sin(radians(angle))
                    pygame.draw.ellipse(display, cell.color, (cx + vibrate, cy, d, d))

    pygame.display.update()

# Overflow Handler
def overFlow(cell, color):
    showPresentGrid()
    pygame.time.delay(30)
    cell.noAtoms = 0
    for neighbor in cell.neighbors:
        neighbor.noAtoms += 1
        neighbor.color = color
        if neighbor.noAtoms >= len(neighbor.neighbors):
            overFlow(neighbor, color)

# Add Atom
def addAtom(i, j, color):
    cell = grid[i][j]
    cell.noAtoms += 1
    cell.color = color
    if cell.noAtoms >= len(cell.neighbors):
        overFlow(cell, color)

# Score Update
def isPlayerInGame():
    global score
    playerScore = [0] * noPlayers
    for i in range(cols):
        for j in range(rows):
            for k in range(noPlayers):
                if grid[i][j].color == players[k]:
                    playerScore[k] += grid[i][j].noAtoms
    score = playerScore[:]

# Game Over
def gameOver(playerIndex):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    gameLoop()

        display.fill(background)
        text = font.render(f"Player {playerIndex + 1} Won!", True, white)
        text2 = font.render("Press 'R' to Reset!", True, white)
        display.blit(text, (width / 3 - 40, height / 3))
        display.blit(text2, (width / 3 - 50, height / 2))
        pygame.display.update()
        clock.tick(60)

# Check Win
def checkWon():
    num = 0
    for i in range(noPlayers):
        if score[i] == 0:
            num += 1
    if num == noPlayers - 1:
        for i in range(noPlayers):
            if score[i]:
                return i
    return 9999

# Main Loop
def gameLoop():
    initializeGrid()
    loop = True
    turns = 0
    currentPlayer = 0
    vibrate = 0.5

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                i = int(x // blocks)
                j = int(y // blocks)
                if grid[i][j].color in [players[currentPlayer], border]:
                    turns += 1
                    addAtom(i, j, players[currentPlayer])
                    currentPlayer = (currentPlayer + 1) % noPlayers
                if turns >= noPlayers:
                    isPlayerInGame()

        display.fill(background)
        vibrate *= -1
        drawGrid(currentPlayer)
        showPresentGrid(vibrate)
        pygame.display.update()

        res = checkWon()
        if res < 9999:
            gameOver(res)

        clock.tick(20)

gameLoop()
