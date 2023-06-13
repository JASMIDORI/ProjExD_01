import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230613/fig/pg_bg.jpg")
    bg_img2 = pg.image.load("ex01-20230613/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01-20230613/fig/3.png")
    kk_img = pg.transform.flip(pg.image.load("ex01-20230613/fig/3.png"), True, False)
    kk_img = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)]

    tmr = 0
    x = 0
    a = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [1600-x, 0])
        
        screen.blit(kk_img[a],[300,200])
        pg.display.update()
        tmr += 1  
        x += 1
        if x >= 1600:
            x = 0   
        if tmr % 16 <= 8:
            a = 0
        else:
            a = 1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()