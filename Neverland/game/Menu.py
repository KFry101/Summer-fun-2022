#Katie Frymire

from decimal import ROUND_UP
import os, random, math,datetime
import pygame as p
os.system('cls')

#intailize p
p.init()


#MENU VARIABLES

WIDTh=897
HEIGHt=597
xs=50
ys=250
wb=30
hb=30
howCount=0
shadowtick=0


#######################################################################################################################################################
#IMAGES#
n=1
ttlScrn=p.image.load('Neverland\Images\Backgrounds\\title.png')
ttlScrn=p.transform.scale(ttlScrn,(WIDTh,HEIGHt))
menu=p.image.load("Neverland\Images\Backgrounds\Menu.png")
menu=p.transform.scale(menu,((WIDTh),(HEIGHt)))
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
Howto1=p.transform.scale(Howto1,(WIDTh *n,HEIGHt*n))
Howto2=p.transform.scale(Howto2,(WIDTh,HEIGHt))
Howto3=p.transform.scale(Howto3,(WIDTh,HEIGHt))
Howto4=p.transform.scale(Howto4,(WIDTh,HEIGHt))
Howto5=p.transform.scale(Howto5,(WIDTh,HEIGHt))
Howto6=p.transform.scale(Howto6,(WIDTh,HEIGHt))
Howto7=p.transform.scale(Howto7,(WIDTh,HEIGHt))
Howto8=p.transform.scale(Howto8,(WIDTh,HEIGHt))
Howto9=p.transform.scale(Howto9,(WIDTh,HEIGHt))
Howto10=p.transform.scale(Howto10,(WIDTh,HEIGHt))
Howto11=p.transform.scale(Howto11,(WIDTh,HEIGHt))
Howto12=p.transform.scale(Howto12,(WIDTh,HEIGHt))
Howto13=p.transform.scale(Howto13,(WIDTh,HEIGHt))
Howto14=p.transform.scale(Howto14,(WIDTh,HEIGHt))
Howto15=p.transform.scale(Howto15,(WIDTh,HEIGHt))
Howto16=p.transform.scale(Howto16,(WIDTh,HEIGHt))
Howto17=p.transform.scale(Howto17,(WIDTh,HEIGHt))
Howto18=p.transform.scale(Howto18,(WIDTh,HEIGHt))
Howto19=p.transform.scale(Howto19,(WIDTh,HEIGHt))
Howto20=p.transform.scale(Howto20,(WIDTh,HEIGHt))
Howto21=p.transform.scale(Howto21,(WIDTh,HEIGHt))
Howto22=p.transform.scale(Howto22,(WIDTh,HEIGHt))
HowTo=[Howto1, Howto2, Howto3, Howto4, Howto5, Howto6, Howto7, Howto8, Howto9, Howto10, Howto11, Howto12, Howto13, Howto14, Howto15, Howto16, Howto17, Howto18, Howto19, Howto20, Howto21, Howto22, Howto21, Howto20, Howto19, Howto18, Howto17, Howto16, Howto15, Howto14, Howto13, Howto12, Howto11,Howto10, Howto9, Howto8, Howto7, Howto6, Howto5, Howto5, Howto4, Howto3, Howto2]
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
SettingList=[  'Avatar','Screen size']
CrClrList=['Green', "White", "Lilac", "Navy"]
SizeList=["bigger,",'Full','Orginal']
#screen
screen=p.display.set_mode((WIDTh,HEIGHt))
p.display.set_caption("Escaping Neverland")
#full = 1495 995
print (p.FULLSCREEN)
#Fonts
p.font.init()
#all non-SysFont fonts are made by "Chequered Ink"
titleScrn=p.font.Font("Neverland\Fonts\Rrquartet-B5wd.ttf", (int(HEIGHt*.21))) #130
menuScrn=p.font.Font("Neverland\Fonts\Rrquartet-B5wd.ttf", (int(HEIGHt*.134)))#80
popup = p.font.Font("Neverland\Fonts\AGoblinAppears-o2aV.ttf", (int(HEIGHt*.0201))) #12
fancy= p.font.Font("Neverland\Fonts\AncientModernTales-a7Po.ttf", (int(HEIGHt*.05)) )#30
TITLE_FNT= p.font.SysFont("timesnewroman",(int(HEIGHt*.134))) #80
SUBT_FNT= p.font.SysFont("comicsans", (int(HEIGHt*.0573))) #40
MENU_FNT= p.font.SysFont("arial", (int(HEIGHt*.0837))) #50
INST_FNT= p.font.SysFont('comicsans', (int(HEIGHt*.05)))  #30

#THE GAME VARIABLES
#declare consants,variables, lists and dictionary
check=True

#Define Colors
colors={'white': [235,255,100], 'red': [255,0,0], 'orange':[255, 85, 0], 'navy':[5, 31, 64], 
'forest':[36, 76, 32],'aqua':[51, 153, 255], 'pink': [200,75,125], 'litpur':[203,160,227],
'mag':[255, 0, 255], 'yellow':[240, 180, 14], 'brown': [45, 55, 38], 'blood':[101, 28, 50],
'gGrey':[133,138,126], 'wGrey':[110,98,89], 'dBrown':[78,53,36] }
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
        #get WIDTh of the text
        #x value = WIDTh/2 - wtext
        xt= WIDTh/2-txt.get_width()/2
        screen.blit(txt,(xt,HEIGHt*.016))
def FancyM(message):
    txt=titleScrn.render(message, 1, (colors.get('brown')))
    #get width of the text
    #x value = WIDTh/2 - wtext
    xt= WIDTh/2-txt.get_width()/2
    screen.blit(txt,(xt,HEIGHt*.3))
def toCon(message):
    txt=fancy.render(message, 1, (colors.get('gGrey')))
    #get WIDTh of the text
    #x value = WIDTh/2 - wtext
    xt= WIDTh/2-txt.get_width()/2
    screen.blit(txt,(xt,HEIGHt*.65))
def TitleMenu(message):
    txt=menuScrn.render(message, 1, (colors.get('forest')))
    #get width of the text
    #x value = WIDTh/2 - wtext
    xt= WIDTh/2-txt.get_width()/2
    screen.blit(txt,(WIDTh*.42,HEIGHt*0.08))

def ReturnBut(message, color):
    txt=MENU_FNT.render(message, 1, (color))
    xt= WIDTh/2-txt.get_width()/2
    screen.blit(txt,((WIDTh*.806),(HEIGHt*.725)))
    
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
# got this from https://realpython.com/python-rounding/#rounding-up
#this function uses parameters fr menu
def mainmenu(Mlist, color):
    txty=HEIGHt*.279
    for i in range(len(Mlist)):
        message=Mlist[i]
        txt=fancy.render(message, 1, (colors.get(color)) )
        screen.blit(txt, (WIDTh*.434,txty))
        txty+=(HEIGHt*.125)
  
def instr(): 
     
    txt=INST_FNT.render("the  path  you  take  is  a  forgotton  track.", 1,(colors.get('brown')))
    xt= WIDTh/2-txt.get_width()/2
    screen.blit(txt,(xt,100))
    txt=INST_FNT.render("Keep your eyes                    wide for a way back.", 1, (colors.get('forest'))) 
    xt= WIDTh/2-txt.get_width()/2
    screen.blit(txt,(xt,170))
    txt=INST_FNT.render("Do  not  wander             when  darkness falls.",1, (colors.get('forest')))
    xt= WIDTh/2-txt.get_width()/2
    screen.blit(txt, (xt,240))
    txt=INST_FNT.render("for you have a chance to lose it all.",1, (colors.get('forest')))
    xt= WIDTh/2-txt.get_width()/2
    screen.blit(txt, (xt,310)) 

def changeScreenSize():
    global HEIGHt, WIDTh, n, screen
    if ((mouse_pos[0] >WIDTh*0.434 and mouse_pos[0] <WIDTh*.624) and (mouse_pos[1] >HEIGHt*.268 and mouse_pos[1] <HEIGHt*.313)):
        HEIGHt=796
        WIDTh=1196
        n+=3333333333
        p.display.flip()
        

    if((mouse_pos[0] >WIDTh*0.434 and mouse_pos[0] <WIDTh*.557) and (mouse_pos[1] >HEIGHt*.402 and mouse_pos[1] <HEIGHt*.447)):
        HEIGHt=995
        WIDTh=1495
        
    if ((mouse_pos[0] >WIDTh*0.434 and mouse_pos[0] <WIDTh*.523) and (mouse_pos[1] >HEIGHt*.530 and mouse_pos[1] <HEIGHt*.577)):
        WIDTh=897
        HEIGHt=597
    
    screen=p.display.set_mode( (WIDTh,HEIGHt))

    p.display.update()
    p.display.flip()

##################################################################################################################################################################


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
        print(shadowtick)
        bg=ttlScrn
        screen.blit(bg,(0,0))
        FancyM("Escaping Neverland")
        toCon("Press Space Bar")
    if MAIN:
        bg=menu
        screen.blit(bg,(0,0))
        TitleMenu("Escaping Neverland")
        mainmenu(MenuList, 'dBrown')
    if INSTR:
        light=True
        Dark=False
        if howCount >=210:
            howCount=0
        if howCount==209:
            shadowtick+=1
        if light:
            
            screen.blit(HowTo[howCount//5], (0,0))
            howCount+=1
            print(shadowtick)
            ReturnBut("back",colors.get('forest') )
            instr()
        # if Dark:

        if shadowtick==50:
            light=False
            Dark=True

        
        
    if SETT: 
        screen.blit(bg,(0,0))
        
        TitleMenu("Settings")
        ReturnBut("back",colors.get('dBrown'))
        mainmenu(SettingList, 'dBrown')      
    if CRCLR:
        screen.blit(bg,(0,0))
        TitleMenu("Avatar")
        ReturnBut("back",colors.get('dBrown'))
        mainmenu(CrClrList, 'dBrown')
    if SIZE:
        screen.blit(bg,(0,0))
        TitleMenu("Screen Size")
        ReturnBut("back",colors.get('dBrown'))
        mainmenu(SizeList, 'dBrown')  
        p.display.update()   
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
            mouse_pos=((WIDTh/2, HEIGHt*.07))
            TITLE=False
            MAIN=True
            mouse_pos=((WIDTh/2, HEIGHt*.07))
            
    if event.type ==p.MOUSEBUTTONDOWN:
        mouse_pos=p.mouse.get_pos()
        print(mouse_pos)
        if MAIN:
            eaten=0
            rad=15
            if ((mouse_pos[0] >WIDTh*0.434 and mouse_pos[0] <WIDTh*.624) and (mouse_pos[1] >HEIGHt*.268 and mouse_pos[1] <HEIGHt*.313)):
                MAIN=False
                GAME=True
            if((mouse_pos[0] >WIDTh*0.434 and mouse_pos[0] <WIDTh*.557) and (mouse_pos[1] >HEIGHt*.402 and mouse_pos[1] <HEIGHt*.447)):
                MAIN=False 
                INSTR=True   
            if ((mouse_pos[0] >WIDTh*0.434 and mouse_pos[0] <WIDTh*.523) and (mouse_pos[1] >HEIGHt*.530 and mouse_pos[1] <HEIGHt*.577)):
                MAIN=False
                SETT=True
            if ((mouse_pos[0] >WIDTh*0.434 and mouse_pos[0] <WIDTh*.483) and (mouse_pos[1] >HEIGHt*.659 and mouse_pos[1] <HEIGHt*.695)):
                MAIN=False
                EXIT=True


        if SETT:
            if ((mouse_pos[0] >WIDTh*0.434 and mouse_pos[0] <WIDTh*.624) and (mouse_pos[1] >HEIGHt*.268 and mouse_pos[1] <HEIGHt*.313)):
                SETT=False
                CRCLR=True
                p.time.delay(300)
                mouse_pos=(0,0)
            if ((mouse_pos[0] >WIDTh*0.434 and mouse_pos[0] <WIDTh*.557) and (mouse_pos[1] >HEIGHt*.402 and mouse_pos[1] <HEIGHt*.447)):
                SETT=False
                SIZE=True
                p.time.delay(300)
                mouse_pos=(0,0)
            # if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
            #     SETT=False
            #     SIZE=True
            #     p.time.delay(400)
            #     mouse_pos=(0,0) 

        
        if CRCLR:

            if ((mouse_pos[0] >WIDTh*0.434 and mouse_pos[0] <WIDTh*.624) and (mouse_pos[1] >HEIGHt*.268 and mouse_pos[1] <HEIGHt*.313)):
                cr_color=colors.get('forest') 
                inscribSq_color=colors.get('forest')  
            if ((mouse_pos[0] >WIDTh*0.434 and mouse_pos[0] <WIDTh*.557) and (mouse_pos[1] >HEIGHt*.402 and mouse_pos[1] <HEIGHt*.447)):
                cr_color=colors.get('white') 
                inscribSq_color=colors.get('white')   
            if ((mouse_pos[0] >WIDTh*0.434 and mouse_pos[0] <WIDTh*.523) and (mouse_pos[1] >HEIGHt*.530 and mouse_pos[1] <HEIGHt*.577)):
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
            changeScreenSize()
               
        #return to Menu WIDTh*.806),(HEIGHt*.725
        if not MAIN:
            if ((mouse_pos[0] >WIDTh*.806 and mouse_pos[0] <WIDTh*.899) and (mouse_pos[1] > HEIGHt*.725 and mouse_pos[1] <HEIGHt*.805)):
                if INSTR:
                    INSTR=False
                    MAIN=True
                if SETT:
                    SETT=False
                    MAIN=True
                if SIZE:
                    SIZE=False
                    SETT=True
                    p.time.delay(400)
                    mouse_pos=(0,0)
             

    #THE GAME Level 1##########################################################3###############################################################################
    if GAME:
        print("work")



    p.display.update()
    p.time.delay(9)
