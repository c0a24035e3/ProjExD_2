import os
import random
import sys
import pygame as pg
import time

WIDTH, HEIGHT = 1100, 650
DELTA = {
    pg.K_UP: (0,-5),
    pg.K_DOWN: (0,+5),
    pg.K_LEFT: (-5,0),
    pg.K_RIGHT: (+5,0)


}
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def check_bound(rct: pg.Rect)->tuple[bool,bool]:
    yoko,tate = True,True
    if rct.left < 0 or WIDTH < rct.right:
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:
        tate = False
    return yoko,tate
#ゲームオーバー画面をつくる関数
def gameover(screen: pg.Surface) -> None:
     #screenと同じ大きさのサーフェイスを作成
     screen1 = pg.Surface((WIDTH,HEIGHT))
     pg.draw.rect(screen1,(0,0,0),pg.Rect(0,0,WIDTH,HEIGHT))
     #透明度を半分に調整
     screen1.set_alpha(128)
     #白文字でGame Overと書かれたフォントサーフェイスを作成
     fonto = pg.font.Font(None,80)
     txt = fonto.render("Game Over",True,(255,255,255))
     #こうかとんの画像をロード
     img = pg.image.load("fig/3.png")
     #Gameoverのテキストrectの中心を画面の真ん中にblit
     txt_rct = txt.get_rect()
     txt_rct.center = (WIDTH/2,HEIGHT/2)
     screen1.blit(txt,txt_rct)
     screen.blit(screen1,(0,0))
     #こうかとんの画像rectのcenterをテキストと同じにし、
     #右の画像をテキストの右に設定し、左の画像をテキストの左に設定した。
     img_rct = img.get_rect()
     img_rct.center = txt_rct.center
     img_rct.right = txt_rct.left
     screen.blit(img,img_rct)
     img_rct.left = txt_rct.right
     screen.blit(img,img_rct)

     pg.display.update()
     time.sleep(5)
    






def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    bb_img = pg.Surface((20,20))
    pg.draw.circle(bb_img,(255,0,0),(10,10),10)
    bb_img.set_colorkey((0,0,0))
    bb_rct = bb_img.get_rect()
    bb_rct.centerx = random.randint(0,WIDTH)
    bb_rct.centery = random.randint(0,WIDTH)
    vx,vy = +5,+5
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0]) 
        if kk_rct.colliderect(bb_rct):
           gameover(screen)
           return #main関数から出る

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for key, mv in DELTA.items():
            if key_lst[key]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
            #if key_lst[pg.K_UP]:
            #    sum_mv[1] -= 5
            #if key_lst[pg.K_DOWN]:
            #   sum_mv[1] += 5
            #if key_lst[pg.K_LEFT]:
            #    sum_mv[0] -= 5
            #if key_lst[pg.K_RIGHT]:
            #   sum_mv[0] += 5
    
        
        #if key_lst[pg.K_w]:
        #   sum_mv[1] -= 5
        #if key_lst[pg.K_DOWN]:
        #   sum_mv[1] += 5
        #if key_lst[pg.K_LEFT]:
        #   sum_mv[0] -= 5
        #if key_lst[pg.K_RIGHT]:
        #   sum_mv[0] += 5
        
        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True,True):
            kk_rct.move_ip(-sum_mv[0],-sum_mv[1])
        screen.blit(kk_img, kk_rct)
        bb_rct.move_ip(vx,vy)
        yoko,tate = check_bound(bb_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        screen.blit(bb_img, bb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)
        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
