# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:23:47 2021

Basic Pacman clone, to familiarize with Python and Pygame
Valid level will consist of
width
height
height number of rows of strings of B (border) or o (pellet)
Pacman X
Pacman Y
Same as for Pacman for Blinky, Pinky, Inky, and Clyde

@author: donov
"""

import pygame, sys, collections, time, random, tkinter
from pygame.locals import *
from tkinter import filedialog

tiles=[] #Filled with rows; get individual tile via tiles[y[x]]
height=0
width=0
pacman=[] # contains x and y coordinates for each respectively.
blinky=[]
pinky=[]
inky=[]
clyde=[]

#Load level file
def loadLevel():
    root = tkinter.Tk()
    dirname = filedialog.askopenfilename(parent=root, initialdir="/",
                                    title='Please select a level')
    lines = open(dirname, 'r').readlines()
    if(len(lines)<2):
        quit()
    global width
    global height
    width=int(lines[0])
    height=int(lines[1])
    for y in range(height):
        print(lines[2+y])
        tiles.append(lines[2+y])
        #assign initial locations
    pacman.append(int(lines[2+height]));pacman.append(int(lines[3+height]));
    blinky.append(int(lines[4+height]));blinky.append(int(lines[5+height]));
    pinky.append(int(lines[6+height]));pinky.append(int(lines[7+height]));
    inky.append(int(lines[8+height]));inky.append(int(lines[9+height]));
    clyde.append(int(lines[10+height]));clyde.append(int(lines[11+height]));

loadLevel()

pygame.init()

#Images TODO: Alternate frames based on direction
PacmanImg = pygame.image.load('pacman.png')
BlinkyImg = pygame.image.load('blinky.png')
PinkyImg = pygame.image.load('pinky.png')
InkyImg = pygame.image.load('inky.png')
ClydeImg = pygame.image.load('clyde.png')

white = (255, 255, 255)
black = (0, 0, 0)
speed=10
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("arial", 20)

dis_width = width*50
dis_height = height*50
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('PacmanPython')

#Message user
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def drawMap():
    dis.blit(PacmanImg, (pacman[0], pacman[1]))
    dis.blit(BlinkyImg, (blinky[0], blinky[1]))
    dis.blit(PinkyImg, (pinky[0], pinky[1]))
    dis.blit(InkyImg, (inky[0], inky[1]))
    dis.blit(InkyImg, (clyde[0], clyde[1]))
    pygame.display.update()


def gameLoop():
    game_over = False
    game_close = False
    
    while not game_over:
 
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press P to Play Again or Q to Quit", white)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman[0]=pacman[0]-1
                elif event.key == pygame.K_RIGHT:
                    pacman[0]=pacman[0]+1
                elif event.key == pygame.K_UP:
                    pacman[1]=pacman[1]-1
                elif event.key == pygame.K_DOWN:
                    pacman[1]=pacman[1]+1
 
        if pacman[0] >= dis_width:
            pacman[0]=0
        if pacman[0] < 0:
            pacman[0]=dis_width-1
        if pacman[1] >= dis_height:
            pacman[1]=0
        if pacman[1] < 0:
            pacman[1]=dis_height-1
        dis.fill(black)
        drawMap()
        clock.tick(speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
