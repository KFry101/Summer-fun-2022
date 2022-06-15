#Katie Frymire

from decimal import ROUND_UP
import os, random, math,datetime
import pygame as p
os.system('cls')

#intailize p
p.init()


#MENU VARIABLES
WIDTH=897
HEIGHT=597
xs=50
ys=250
wb=30
hb=30
#######################################################################################################################################################
#IMAGES#
ttlScrn=p.image.load('Neverland\Images\Backgrounds\\title.png')
ttlScrn=p.transform.scale(ttlScrn,(WIDTH,HEIGHT))
bg=ttlScrn
#declare constants/ windows
TITLE=True
MAIN=False
INSTR=False
SETT=False
BACKCLR=False
CRCLR=False
SIZE=False
LEV_1=False
LEV_2=False
LEV_3=False
PSCORE1=False
SCOREBOARD=False
EXIT=False
#lists fr messages
MenuList=["Instructions", 'Settings', '  Level 1', "Exit"]
SettingList=[ 'Background Color', 'Avatar','Screen size']
BackColorList=['Aqua',"Magenta", "Yellow", "Orange"]
CrClrList=['Green', "White", "Lilac", "Navy"]
SizeList=["bigger,",'Full','Orginal']
#screen
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("Escaping Neverland")
#full = 1495 995
print (p.FULLSCREEN)
#Fonts
p.font.init()
#all non-SysFont fonts are made by "Chequered Ink"
popup = p.font.Font("Neverland\Fonts\AGoblinAppears-o2aV.ttf",12)
fancy= p.font.Font("Neverland\Fonts\AncientModernTales-a7Po.ttf", 100)
TITLE_FNT= p.font.SysFont("timesnewroman", 80)
SUBT_FNT= p.font.SysFont("comicsans", 40)
MENU_FNT= p.font.SysFont("arial", 50)
INST_FNT= p.font.SysFont('comicsans', 30)

#THE GAME VARIABLES
#declare consants,variables, lists and dictionary
check=True
move=5
grow=5
eaten=0
sec=0
#squareG variables
xsg=20
ysg=20
wbox=30
hbox=30
#circle variables
rad=15
xc=random.randint(rad, WIDTH-rad)
yc=random.randint(rad, HEIGHT-rad)
#inner box
ibox=rad*math.sqrt(2)
xig= xc-(ibox/2)
yig= yc-(ibox/2)
inscribSq=p.Rect(xig,yig,ibox,ibox)
#create the rect object
squareG=p.Rect(xsg, ysg, wbox, hbox)
square=p.Rect(xs,ys,wb,hb)
#Define Colors
colors={'white': [255,255,255], 'red': [255,0,0], 'orange':[255, 85, 0], 'navy':[5, 31, 64], 
'forest':[16, 46, 12],'aqua':[51, 153, 255], 'pink': [200,75,125], 'litpur':[203,160,227],
'mag':[255, 0, 255], 'yellow':[240, 180, 14] }
#Get colors
# background=colors.get('pink')
sq_color=colors.get('navy')
cr_color=colors.get('white')
inscribSq_color=colors.get('white')
sqM_color=colors.get('navy')
#GLobalization setup
txt=''
txty=''
xt=''
def PopUpM(message):
        txt=popup.render(message, 1, (255, 255, 255))
        #get width of the text
        #x value = WIDTH/2 - wtext
        xt= WIDTH/2-txt.get_width()/2
        screen.blit(txt,(xt,HEIGHT*.016))
def FancyM(message):
    txt=fancy.render(message, 1, (255, 255, 255))
    #get width of the text
    #x value = WIDTH/2 - wtext
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,HEIGHT*.0714))
def TitleMenu(message):
    txt=TITLE_FNT.render(message, 1, (255, 255, 255))
    #get width of the text
    #x value = WIDTH/2 - wtext
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,50))

def ReturnBut(message):
    txt=MENU_FNT.render(message, 1, (255, 255, 255))
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,550))
    
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
# got this from https://realpython.com/python-rounding/#rounding-up
#this function uses parameters fr menu
def mainmenu(Mlist):
    txty=245
    square.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        txt=INST_FNT.render(message, 1, (5, 31, 64) )
        screen.blit(txt, (90,txty))
        txty+=50
        p.draw.rect(screen, sqM_color, square)
        square.y+=50
  
def instr(): 
     
    txt=INST_FNT.render("Control the circle with the arrow keys", 1,(5, 31, 64))
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,200))
    txt=INST_FNT.render("and absorb the square. If there is a ", 1, (5, 31, 64)) 
    screen.blit(txt,(xt,240))
    txt=INST_FNT.render("second player, control the square with",1, (5, 31, 64))
    screen.blit(txt, (xt,280))
    txt=INST_FNT.render("the wasd keys. You got to be quick!",1, (5, 31, 64))
    screen.blit(txt, (xt,320)) 


def changeClr():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor) == bg:
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
changeClr()
sq_color=colors.get(randColor)  

def changeScreenSize(xm,ym):
    global HEIGHT, WIDTH, screen
    if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
        HEIGHT=800
        WIDTH=800
        print('here!')

    if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340)):
        HEIGHT=1000
        WIDTH=1000
        
    if ((mouse_pos[0] >0 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
        HEIGHT=700
        WIDTH=700
    screen=p.display.set_mode((WIDTH,HEIGHT))

######################################################################################################################
MAX=10
jumpCount=10
JUMP=False
mouse_pos=(0,0)
xm= mouse_pos[0]
ym=mouse_pos[1]
while check:
    keys=p.key.get_pressed()
    if TITLE:
        screen.blit(bg,(0,0))
        FancyM("Escaping Neverland")
    if MAIN:
        screen.blit(bg,(0,0))
        FancyM("Escaping Neverland")
        mainmenu(MenuList)
    if INSTR:
        screen.blit(bg,(0,0))
        TitleMenu("Instructions")
        ReturnBut("Return to Menu")
        instr()
    if SETT: 
        screen.blit(bg,(0,0))
        TitleMenu("Settings")
        ReturnBut("Return to Menu")
        mainmenu(SettingList)   
    if BACKCLR:
        screen.blit(bg,(0,0))
        TitleMenu("Background")
        ReturnBut("Back")
        mainmenu(BackColorList)   
    if CRCLR:
        screen.blit(bg,(0,0))
        TitleMenu("Avatar")
        ReturnBut("Back")
        mainmenu(CrClrList)
    if SIZE:
        screen.blit(bg,(0,0))
        TitleMenu("Screen Size")
        ReturnBut("Back")
        mainmenu(SizeList)     
    if EXIT:

        p.QUIT    

    for event in p.event.get():
        if event.type == p.QUIT:
            check = False 
    #Mouse Controls
    #Menu Navigation
    if event.type ==p.MOUSEBUTTONDOWN:
        mouse_pos=p.mouse.get_pos()
        print(mouse_pos)
        
        if MAIN:
            eaten=0
            rad=15
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <280))or INSTR:
                MAIN=False
                screen.fill(bg)
                INSTR=True
            if((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330))or SETT:
                MAIN=False 
                SETT=True
                p.time.delay(300)
                mouse_pos=(0,0)    
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <380))or LEV_1:
                MAIN=False
                LEV_1=True
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <430))or LEV_2:
                MAIN=False
                EXIT=True


        if SETT:
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290))or BACKCLR:
                SETT=False
                screen.fill(bg)
                BACKCLR=True
                p.time.delay(300)
                mouse_pos=(0,0)
            if((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340))or CRCLR:
                SETT=False
                CRCLR=True
                p.time.delay(300)
                mouse_pos=(0,0)
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
                SETT=False
                SIZE=True
                p.time.delay(400)
                mouse_pos=(0,0) 

        if BACKCLR:
            if ((mouse_pos[0] >306 and mouse_pos[0] <393) and (mouse_pos[1] >560 and mouse_pos[1] <595)) or SETT:
                BACKCLR=False
                SETT=True
                p.time.delay(400)
                mouse_pos=(0,0)
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
                bg=colors.get('aqua')  
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340)):
                bg=colors.get('mag')     
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
                bg=colors.get('yellow')
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <440)):
                bg=colors.get('orange')   
        
        if CRCLR:

            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
                cr_color=colors.get('forest') 
                inscribSq_color=colors.get('forest')  
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340)):
                cr_color=colors.get('white') 
                inscribSq_color=colors.get('white')   
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
                cr_color=colors.get('litpur')  
                inscribSq_color=colors.get('litpur')  
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <440)):
                cr_color=colors.get('navy')  
                inscribSq_color=colors.get('navy')  
            if ((mouse_pos[0] >306 and mouse_pos[0] <393) and (mouse_pos[1] >560 and mouse_pos[1] <595)) or SETT:
                CRCLR=False
                SETT=True
                p.time.delay(400)
                mouse_pos=(0,0)
        if SIZE:
            print("i am here!!!")
            changeScreenSize(xm,ym)
            if ((mouse_pos[0] >306 and mouse_pos[0] <393) and (mouse_pos[1] >560 and mouse_pos[1] <595)) or SETT:
                SIZE=False
                SETT=True
                p.time.delay(400)
                mouse_pos=(0,0)
                
        #return to Menu
        if not MAIN and not LEV_1:
            if ((mouse_pos[0] >210 and mouse_pos[0] <490) and (mouse_pos[1] >561 and mouse_pos[1] <595))or MAIN:
                if INSTR:
                    INSTR=False
                    MAIN=True
                if SETT:
                    SETT=False
                    MAIN=True
                if PSCORE1:
                    PSCORE1=False
                    MAIN=True
                if SCOREBOARD:
                    SCOREBOARD=False
                    MAIN=True

    #THE GAME Level 1##########################################################3###############################################################################
    if LEV_1:
        screen.fill(bg)
        # Game Controls
        #squareG control
        if keys[p.K_a] and squareG.x>=move :
            squareG.x -= move 
        if keys[p.K_d] and squareG.x <=WIDTH-(wbox+move):
            squareG.x += move
        #jumping part
        if not JUMP:
            if keys[p.K_w] and squareG.y>=move:
                squareG.y -= move  
            if keys[p.K_s] and squareG.y<=HEIGHT-(hbox+move):
                squareG.y += move 
            if keys[p.K_SPACE]:
                JUMP=True
        else:
            if jumpCount>=-MAX:
                squareG.y -= jumpCount*abs(jumpCount)/2
                jumpCount-=1
            else:
                jumpCount=MAX
                JUMP=False
        #circle control
        if keys[p.K_LEFT] and xc >=rad+move:
            xc -= move
        if keys[p.K_RIGHT] and xc<=WIDTH-(rad+move):
            xc += move
        if keys[p.K_UP] and yc>=rad+move:
            yc -= move
        if keys[p.K_DOWN] and yc<=HEIGHT-(rad+move):
            yc+= move
        
        checkCollide=squareG.collidepoint((xc,yc))
        if checkCollide:
            squareG.x=random.randint(wbox, WIDTH-wbox)
            squareG.y=random.randint(hbox, HEIGHT-hbox)
            rad+=grow
        ibox=rad*math.sqrt(2)
        xig= xc-(ibox/2)
        yig= yc-(ibox/2)
        inscribSq=p.Rect(xig,yig,ibox,ibox)
        sqCollide=squareG.colliderect((inscribSq))
        if sqCollide:
            squareG.x=random.randint(wbox, WIDTH-wbox)
            squareG.y=random.randint(hbox, HEIGHT-hbox)
            changeClr()
            sq_color=colors.get(randColor)  
            rad+=grow
            eaten+=1
            # secs=Something to track the amount of time played
    
        p.draw.rect(screen,sq_color, squareG)    
        p.draw.circle(screen,cr_color, (xc,yc), rad)
        p.draw.rect(screen,inscribSq_color, inscribSq)


    p.display.update()
    p.time.delay(9)
