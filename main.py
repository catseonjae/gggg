import pygame
import sys
SCREEN_WIDTH=640
SCREEN_HEIGHT=640
pygame.init()
pygame.display.set_caption("mono")

running = True
BLACK=(0,0,0)
WHITE=(255,255,255)
clock = pygame.time.Clock()

class Input_handler:
    def __init__(self):
        self.just_pressed={'a':False,'b':False,'c':False,'d':False,'e':False,'f':False,'g':False,'h':False,'i':False,'j':False,'k':False,'l':False,'m':False,'n':False,'o':False,'p':False,'q':False,'r':False,'s':False,'t':False,'u':False,'v':False,'w':False,'x':False,'y':False,'z':False}
        self.pressed={'a':False,'b':False,'c':False,'d':False,'e':False,'f':False,'g':False,'h':False,'i':False,'j':False,'k':False,'l':False,'m':False,'n':False,'o':False,'p':False,'q':False,'r':False,'s':False,'t':False,'u':False,'v':False,'w':False,'x':False,'y':False,'z':False}
        self.func={'a':None,'b':None,'c':None,'d':None,'e':None,'f':None,'g':None,'h':None,'i':None,'j':None,'k':None,'l':None,'m':None,'n':None,'o':None,'p':None,'q':None,'r':None,'s':None,'t':None,'u':None,'v':None,'w':None,'x':None,'y':None,'z':None}
        self.alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        self.leave=[]
        self.buffer=[]
    def update(self):
        for i in self.just_pressed.keys():
            self.just_pressed[i]=False
        for i in self.buffer:
            if not i in self.alphabets:
                continue
            if not self.pressed[i]:
                self.just_pressed[i]=True
                self.pressed[i]=True
        for i in self.leave:
            if not i in self.alphabets:
                continue
            self.pressed[i]=False
        self.buffer=[]
        self.leave=[]
    def update_pygame(self, key):
        char=""
        if key == pygame.K_a:
            char='a'     
        if key == pygame.K_b:
            char='b'     
        if key == pygame.K_c:
            char='c'     
        if key == pygame.K_d:
            char='d'     
        if key == pygame.K_e:
            char='e'     
        if key == pygame.K_f:
            char='f'     
        if key == pygame.K_g:
            char='g'     
        if key == pygame.K_h:
            char='h'     
        if key == pygame.K_i:
            char='i'     
        if key == pygame.K_j:
            char='j'     
        if key == pygame.K_k:
            char='k'     
        if key == pygame.K_l:
            char='l'     
        if key == pygame.K_m:
            char='m'     
        if key == pygame.K_n:
            char='n'     
        if key == pygame.K_o:
            char='o'     
        if key == pygame.K_p:
            char='p'     
        if key == pygame.K_q:
            char='q'     
        if key == pygame.K_r:
            char='r'
        if key == pygame.K_s:
            char='s'
        if key == pygame.K_t:
            char='t'
        if key == pygame.K_u:
            char='u'
        if key == pygame.K_v:
            char='v'
        if key == pygame.K_w:
            char='w'
        if key == pygame.K_x:
            char='x'
        if key == pygame.K_y:
            char='y'
        if key == pygame.K_z:
            char='z'
        self.buffer.append(char)
    def update_pygame_up(self,key):
        char=""
        if key == pygame.K_a:
            char='a'     
        if key == pygame.K_b:
            char='b'     
        if key == pygame.K_c:
            char='c'     
        if key == pygame.K_d:
            char='d'     
        if key == pygame.K_e:
            char='e'     
        if key == pygame.K_f:
            char='f'     
        if key == pygame.K_g:
            char='g'     
        if key == pygame.K_h:
            char='h'     
        if key == pygame.K_i:
            char='i'     
        if key == pygame.K_j:
            char='j'     
        if key == pygame.K_k:
            char='k'     
        if key == pygame.K_l:
            char='l'     
        if key == pygame.K_m:
            char='m'     
        if key == pygame.K_n:
            char='n'     
        if key == pygame.K_o:
            char='o'     
        if key == pygame.K_p:
            char='p'     
        if key == pygame.K_q:
            char='q'     
        if key == pygame.K_r:
            char='r'
        if key == pygame.K_s:
            char='s'
        if key == pygame.K_t:
            char='t'
        if key == pygame.K_u:
            char='u'
        if key == pygame.K_v:
            char='v'
        if key == pygame.K_w:
            char='w'
        if key == pygame.K_x:
            char='x'
        if key == pygame.K_y:
            char='y'
        if key == pygame.K_z:
            char='z'
        self.leave.append(char)
    def act(self):
        for i in self.pressed.keys():
            if self.pressed[i] and self.func[i] != None:
                self.func[i]()
    def set_func(self, key, func):
        self.func[key]=lambda: func(key)

class Object:
    def __init__(self,x=0,y=0,img_path="images\\img"):
        self.x=x
        self.y=y
        self.image=pygame.image.load(img_path)
        self.dy=[0,-1,0,1]
        self.dx=[1,0,-1,0]
    def move(self, dx,dy):
        x+=dx
        y+=dy

class Tile:
    def __init__(self, tile_set={}):
        self.tile_set=tile_set
        self.tile_size=64
    def add_tile(self, name,image):
        self.tile_set[name]=image
class World:
    def __init__(self,tile,world_size=[10000,10000],window_size=(640,640),background=BLACK,camera=[0,0]):
        self.screen = pygame.display.set_mode(window_size)
        self.xrange=[-world_size[0]/2,world_size[0]/2]
        self.yrange=[-world_size[1]/2,world_size[1]/2]
        self.obj=[]
        self.maps=[[0]*world_size[0] for i in range(world_size[1])]
        self.tile_size=tile.tile_size
        self.tile=tile
        self.camera=camera
    def add_obj(self,obj):
        self.obj.append(obj)
        return len(self.obj)
    def loop(self):
        xwindow=[self.camera[0]-self.window_size[0]/2,self.camera[0]+self.window_size[0]/2]
        ywindow=[self.camera[1]-self.window_size[1]/2,self.camera[1]+self.window_size[1]/2]

        for i in self.obj:
            

    def min(a,b):
        if a<b:
            return a
        return b
    def max(a,b):
        if a>b:
            return a
        return b
    def minmax_x(self,a):
        return min(max(self.xrange[0],a),self.xrange[1])
    def minmax_y(self,a):
        return min(max(self.yrange[0],a),self.yrange[1])

class Vector:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y        
    def __add__(self, v):
        self.x+=v.x
        self.y+=v.y
    def __sub__(self,v):
        self.x-=v.x
        self.y-=v.y
    def __mul__(self, v):
        return self.x*v.x-self.y*v.y
    def length(self):
        return (self.x**2+self.y**2)**0.5
    def normalize(self):
        length=self.length()
        self.x/=length
        self.y/=length


x=0
y=0
dx=0
dy=0
v=10
def move(key):
    global dy
    global dx
    if key=='w':
        dy-=v
    if key=='a':
        dx-=v
    if key=='s':
        dy+=v
    if key=='d':
        dx+=v
input_handler = Input_handler()
input_handler.set_func('w',move)
input_handler.set_func('a',move)
input_handler.set_func('s',move)
input_handler.set_func('d',move)


while running:
    clock.tick(60)

 
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            break
        if event.type == pygame.KEYDOWN:
            input_handler.update_pygame(event.key)
        if event.type== pygame.KEYUP:
            input_handler.update_pygame_up(event.key)
    input_handler.update()
    input_handler.act()
    #sqrt(dx^2+dy^2)=v
    #dx^2+dy^2=v^2
    #
    length=dx**2+dy**2
    if length!=0:
        length=length**0.5
        dx=dx/length*v
        dy=dy/length*v
    y+=dy
    x+=dx
    x=minmax(x)
    y=minmax(y)
    print((dx**2+dy**2)**0.5)
    dx=0
    dy=0
