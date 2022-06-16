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
menu=p.image.load("Neverland\Images\Backgrounds\Menu.png")
menu=p.transform.scale(menu,(WIDTH,HEIGHT))
Howto1=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_00_delay-0.png')
Howto2=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_01_delay-0.png')
Howto3=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_02_delay-0.png')
Howto4=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_03_delay-0.png')
Howto5=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_04_delay-0.png')
Howto6=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_05_delay-0.png')
Howto7=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_06_delay-0.png')
Howto8=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_07_delay-0.png')
Howto9=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_08_delay-0.png')
Howto10=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_09_delay-0.png')
Howto11=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_10_delay-0.png')
Howto12=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_11_delay-0.png')
Howto13=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_12_delay-0.png')
Howto14=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_13_delay-0.png')
Howto15=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_14_delay-0.png')
Howto16=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_15_delay-0.png')
Howto17=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_16_delay-0.png')
Howto18=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_17_delay-0.png')
Howto19=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_18_delay-0.png')
Howto20=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_19_delay-0.png')
Howto21=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_20_delay-0.png')
Howto22=p.image.load('Neverland\Images\Backgrounds\HowTo\\frame_21_delay-0.png')
Howto1=p.transform.scale(Howto1,(WIDTH,HEIGHT))
Howto2=p.transform.scale(Howto2,(WIDTH,HEIGHT))
Howto3=p.transform.scale(Howto3,(WIDTH,HEIGHT))
Howto4=p.transform.scale(Howto4,(WIDTH,HEIGHT))
Howto5=p.transform.scale(Howto5,(WIDTH,HEIGHT))
Howto6=p.transform.scale(Howto6,(WIDTH,HEIGHT))
Howto7=p.transform.scale(Howto7,(WIDTH,HEIGHT))
Howto8=p.transform.scale(Howto8,(WIDTH,HEIGHT))
Howto9=p.transform.scale(Howto9,(WIDTH,HEIGHT))
Howto10=p.transform.scale(Howto10,(WIDTH,HEIGHT))
Howto11=p.transform.scale(Howto11,(WIDTH,HEIGHT))
Howto12=p.transform.scale(Howto12,(WIDTH,HEIGHT))
Howto13=p.transform.scale(Howto13,(WIDTH,HEIGHT))
Howto14=p.transform.scale(Howto14,(WIDTH,HEIGHT))
Howto15=p.transform.scale(Howto15,(WIDTH,HEIGHT))
Howto16=p.transform.scale(Howto16,(WIDTH,HEIGHT))
Howto17=p.transform.scale(Howto17,(WIDTH,HEIGHT))
Howto18=p.transform.scale(Howto18,(WIDTH,HEIGHT))
Howto19=p.transform.scale(Howto19,(WIDTH,HEIGHT))
Howto20=p.transform.scale(Howto20,(WIDTH,HEIGHT))
Howto21=p.transform.scale(Howto21,(WIDTH,HEIGHT))
Howto22=p.transform.scale(Howto22,(WIDTH,HEIGHT))

bg=ttlScrn

#declare constants/ windows
TITLE=True
MAIN=False
INSTR=False
SETT=False
BACKCLR=False
CRCLR=False
SIZE=False
GAME=False
PSCORE1=False
SCOREBOARD=False
EXIT=False
#lists fr messages
MenuList=["Start Adventure", 'How to play', 'Settings', "Exit"]
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
titleScrn=p.font.Font("Neverland\Fonts\Rrquartet-B5wd.ttf", 130)
menuScrn=p.font.Font("Neverland\Fonts\Rrquartet-B5wd.ttf", 80)
popup = p.font.Font("Neverland\Fonts\AGoblinAppears-o2aV.ttf",12)
fancy= p.font.Font("Neverland\Fonts\AncientModernTales-a7Po.ttf", 30)
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
'forest':[36, 76, 32],'aqua':[51, 153, 255], 'pink': [200,75,125], 'litpur':[203,160,227],
'mag':[255, 0, 255], 'yellow':[240, 180, 14], 'brown': [45, 55, 38] }
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
    txt=titleScrn.render(message, 1, (colors.get('brown')))
    #get width of the text
    #x value = WIDTH/2 - wtext
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,HEIGHT*.3))
def toCon(message):
    txt=fancy.render(message, 1, (colors.get('forest')))
    #get width of the text
    #x value = WIDTH/2 - wtext
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,HEIGHT*.65))
def TitleMenu(message):
    txt=menuScrn.render(message, 1, (colors.get('brown')))
    #get width of the text
    #x value = WIDTH/2 - wtext
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(WIDTH*.42,HEIGHT*0.08))

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
    txty=HEIGHT*.279
    square.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        txt=fancy.render(message, 1, (colors.get('forest')) )
        screen.blit(txt, (WIDTH*.434,txty))
        txty+=75
  
def instr(): 
     
    txt=INST_FNT.render("the path you take is a forgotton track.", 1,(colors.get('forest')))
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,200))
    txt=INST_FNT.render("Keep your eyes wide for a way back.", 1, (colors.get('forest'))) 
    screen.blit(txt,(xt,240))
    txt=INST_FNT.render("do not wander when darkness falls",1, (colors.get('forest')))
    screen.blit(txt, (xt,280))
    txt=INST_FNT.render("for you have a chance to lose it all.",1, (colors.get('forest')))
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
        bg=ttlScrn
        screen.blit(bg,(0,0))
        FancyM("Escaping Neverland")
        toCon("Press Space Bar")
    if MAIN:
        bg=menu
        screen.blit(bg,(0,0))
        TitleMenu("Escaping Neverland")
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
    keys=p.key.get_pressed()
    #Mouse Controls
    #Menu Navigation
    if TITLE:
        if keys[p.K_SPACE]:
            mouse_pos=((WIDTH/2, HEIGHT*.07))
            TITLE=False
            MAIN=True
            mouse_pos=((WIDTH/2, HEIGHT*.07))
            
    if event.type ==p.MOUSEBUTTONDOWN:
        mouse_pos=p.mouse.get_pos()
        print(mouse_pos)
        if MAIN:
            eaten=0
            rad=15
            if ((mouse_pos[0] >WIDTH*0.434 and mouse_pos[0] <WIDTH*.624) and (mouse_pos[1] >HEIGHT*.268 and mouse_pos[1] <HEIGHT*.313)):
                MAIN=False
                GAME=True
            if((mouse_pos[0] >WIDTH*0.434 and mouse_pos[0] <WIDTH*.557) and (mouse_pos[1] >HEIGHT*.402 and mouse_pos[1] <HEIGHT*.447)):
                MAIN=False 
                INSTR=True   
            if ((mouse_pos[0] >WIDTH*0.434 and mouse_pos[0] <WIDTH*.523) and (mouse_pos[1] >HEIGHT*.530 and mouse_pos[1] <HEIGHT*.577)):
                MAIN=False
                SETT=True
            if ((mouse_pos[0] >WIDTH*0.434 and mouse_pos[0] <WIDTH*.483) and (mouse_pos[1] >HEIGHT*.659 and mouse_pos[1] <HEIGHT*.695)):
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
        if not MAIN:
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
    if GAME:
        print("work")



    p.display.update()
    p.time.delay(9)
