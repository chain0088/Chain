import pygame
import color_screen

pygame.init()                                   #เริ่มการทำงานของ pygame
pygame.display.set_caption("Dodge It!!!")       #ชื่อของหน้าต่างจอเกม
screen_w = 600
screen_h = 400
screen = pygame.display.set_mode((screen_w, screen_h))    #ขนาดหน้าต้างจอเกม

white = (255, 255, 255)
light_blue = (100, 150, 220)
dark_blue = (30, 60, 125)
gray = (200, 200 ,200)
dark_gray =(80, 80, 80)
screen.fill(white)                              #เปลี่ยนสีหน้าจอเกม

#pygame.draw.rect(screen, gray, (200, 200, 200, 200))

img = pygame.image.load("space_pixle.jpg")
img = pygame.transform.scale(img,(600, 400))

sys_FN = pygame.font.SysFont("calisto",50)
sys_FS = pygame.font.SysFont("calisto",35)
name_game = sys_FN.render("DODGE", True, white)
name_game2 = sys_FN.render("IT ! ! !", True, white)
start = sys_FS.render("START", True, white)
menu = sys_FS.render("Menu", True ,white)

screen.blit(img,(0, 0))
pygame.draw.rect(screen, dark_gray, (0, 225, 150, 50))
screen.blit(start, (17, 230))
screen.blit(name_game, (30, 30))
screen.blit(name_game2, (30, 100))
c = 0
mouse_x = 0
mouse_y = 0
run = True
while run :
    for e in pygame.event.get():                #ตรวจสอบเหตุการที่เกิดขึ้นภายในเกม
        if e.type == pygame.QUIT:              #ตรวจสอบว่ามีการปิดหน้าต่างเกมหรือไม่
            run = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = e.pos[0]
            mouse_y = e.pos[1]
        if (0 < mouse_x < 150) and (225 < mouse_y < 275) and (c == 0):
            screen.blit(img, (0, 0))
            pygame.draw.rect(screen, dark_gray, (0, 0, 100, 50))
            pygame.draw.circle(screen, white, (50, 200), 20)
            screen.blit(menu, (5, 2.5))
            c += 1
        if (0 < mouse_x < 100) and (0 < mouse_y < 50) and (c == 1):
            screen.blit(img,(0, 0))
            pygame.draw.rect(screen, dark_gray, (0, 225, 150, 50))
            screen.blit(start, (17, 230))
            screen.blit(name_game, (30, 30))
            screen.blit(name_game2, (30, 100))
            c -= 1



    pygame.display.update()                    #อัพเดทหน้าจอเกมที่แสดง


pygame.quit()                                   #หยุดการทำงานของ pygame
