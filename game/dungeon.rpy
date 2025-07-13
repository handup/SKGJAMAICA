# This file is in the public domain.

init -1 python:
    
    class Stage(object):
        
        '''
        Class which contains map itself, auto mapping record, and encounter enemy.
        '''
        
        def __init__(self, map, enemy=None):
            self.map=map
            self.enemy=enemy
            self.mapped=[]
            for n,i in  enumerate(map):
                self.mapped.append([])
                for j in i:
                    self.mapped[n].append(0)
                    
    class Coordinate(object):
        
        '''
        Class used for calculating relative coordinate.   
        '''
        
        def __init__(self, stage=None, y=0, x=0, dy=0, dx=0):
            self.stage=stage
            self.y=y
            self.x=x
            self.dy=dy
            self.dx=dx 
            
    class Minimap(object):
        
        '''
        A minimap. Minimap(current_coordinate).sm is a displayable to show this minimap.
        '''
        
        def __init__(self,child):
            self.sm = SpriteManager(ignore_time=True)
            for n,i in enumerate(child.stage.map):
                for m, j in enumerate(i):
                    if child.stage.mapped[n][m]==1:
                        if j in ["1"]:
                            d = Solid("#666", xysize=(12,12))
                        else:
                            d = Solid("#fff9", xysize=(12,12))
                    else:
                        d = Solid("#0000", xysize=(12,12))
                    self.add(d,n,m)
            if child.dy==-1:
                self.add(Text("↑",size=12),child.y,child.x)
            elif child.dx==1:
                self.add(Text("→",size=12),child.y,child.x)
            elif child.dy==1:
                self.add(Text("↓",size=12),child.y,child.x)
            else:
                self.add(Text("←",size=12),child.y,child.x)
                    
        def add(self, d,n,m):
            s = self.sm.create(d)
            s.x = m*12+12
            s.y = n*12+12
            
screen move:
    # Screen which shows move buttons and a minimap 
    
    fixed style_group "move":
        if front1.stage.map[front1.y][front1.x] is not "1":
            textbutton "↑" action Return(value=front1)  xcenter .2 ycenter .7
        textbutton "→" action Return(value=turnright) xcenter .3 ycenter .8
        textbutton "↓" action Return(value=turnback) xcenter .2 ycenter .9
        textbutton "←" action Return(value=turnleft) xcenter .1 ycenter .8
    
    add Minimap(here).sm
    
style move_button_text:
    size 60
        
# Assign background images.    
# "left0" means a wall on the lefthand, "front2" means a further wall on the front, and so on.

# left2, front2, right2
# left1, front1, right1
# left0,  here , right0 

image floor = "floor.png"
image left0 = "left0.png"
image right0 = Transform("left0.png", xzoom=-1)
image front1 ="front1.png"
image left1 = "left1.png"
image right1 = Transform("left1.png", xzoom=-1)    
image front2 = "front2.png"
image left2 = "left2.png"
image right2 = Transform("left2.png", xzoom=-1)    
    
label dungeon:
    # To start exploring, call or jump to this label
    # To exit, create an event which has return or jump statement.
    
    while True:
        # Calculate relative coordinates
        python:            
            turnright=Coordinate(here.stage, here.y,here.x, here.dx,-here.dy)
            turnleft=Coordinate(here.stage, here.y, here.x, -here.dx,here.dy)
            turnback=Coordinate(here.stage, here.y,here.x, -here.dy,-here.dx)
            right0=Coordinate(here.stage, here.y+here.dx,here.x-here.dy, here.dy,here.dx)
            left0=Coordinate(here.stage, here.y-here.dx,here.x+here.dy, here.dy,here.dx)
            front1=Coordinate(here.stage, here.y+here.dy,here.x+here.dx, here.dy,here.dx)
            right1=Coordinate(here.stage, front1.y+front1.dx,front1.x-front1.dy, here.dy,here.dx)
            left1=Coordinate(here.stage, front1.y-front1.dx,front1.x+front1.dy, here.dy,here.dx)
            front2=Coordinate(here.stage, front1.y+front1.dy,front1.x+front1.dx, here.dy,here.dx)
            right2=Coordinate(here.stage, front2.y+front2.dx,front2.x-front2.dy, here.dy,here.dx)
            left2=Coordinate(here.stage, front2.y-front2.dx,front2.x+front2.dy, here.dy,here.dx)                    
        
        # Composite background images. Try-except clauses are used to prevent the List Out of Index Error
        scene
        show floor
        python:
            for i in ["left2", "right2", "front2", "left1", "right1", "front1", "left0", "right0"]:
                try:
                    j=globals()[i]
                    if j.stage.map[j.y][j.x]=="1":
                        renpy.show(i)
                except:
                    pass
                
        # Record maps
        python:
            for i in [left1, right1, front1, left0, right0, here]:
                here.stage.mapped[i.y][i.x]=1
                
        # Check events. If it happens, call a label or jump out to a label.
        if here.stage.enemy is not None and renpy.random.random()< .2:
            call battle(player=hero, enemy=here.stage.enemy)
        
        if here.stage.map[here.y][here.x] == "h":
            scene black
            "Time for bed."
            jump night
            
        if here.stage.map[front1.y][front1.x] == "h":
            image stairs = "images/stairs.png"
            show stairs:
                zoom 0.5
                xalign 0.5
                yalign 0.8 
    
        if front2.x >= 0 and front2.y >= 0 and front2.y < len(here.stage.map) and front2.x < len(here.stage.map[front2.y]):
            if here.stage.map[front2.y][front2.x] == "h":
                image stairs = "images/stairs.png"
                show stairs:
                    zoom 0.25
                    xalign 0.5
                    yalign 0.5 
        
        # Otherwise, call the move screen
        $ renpy.block_rollback()
        call screen move
        $ here=_return
