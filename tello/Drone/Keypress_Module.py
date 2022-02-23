import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400,400)) # to detect key press we need to be in game window so here we are creating game window

def getKey(keyName):
    ans = False
    for eve in pygame.event.get():pass   # detecting events in pygame
    keyInput = pygame.key.get_pressed()  # detecting Key pressed
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans # return true or False depending upon key pressed or not

def main():
    if getKey("LEFT"):
        print("Left Key Pressed")
    if getKey("RIGHT"):
        print("Right Key Pressed")


if __name__ == '__main__':
    init()
    while True:
        main()