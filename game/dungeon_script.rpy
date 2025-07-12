# This file is in the public domain.

label dungeon_start:
    
    # Initializing data
    python:
        
        # Create skills (name, type, hit, power)
        attack = Skill("Attack", "attack", 70, 20)
        escape = Skill("Escape", "escape")
        
        # Create battle actors (name, max_hp, skills)
        hero = Actor("Hero",100, [attack,escape])
        goblin = Actor("Goblin",40, [attack])
        
        # Create a dungeon stage (map,enemy)
        # "1" means wall, "0" means path. 
        stage1=Stage([
            "1111111111",
            "1111011001",
            "1000000001",
            "1110111101",
            "1000000001",
            "1111111111",
            ],
            enemy=goblin)
            
    # The game starts here.
    
    # Place a player position on a dungeon stage (stage,y,x,dy,dx).
    # dx,dy means direction. If dy=1, it's down. If dx=-1, it's left.
    $ here=Coordinate(stage1,2,2,0,1) 
    
    # To start exploring, call or jump to the label dungeon. 
    call dungeon
    
    # To start battling, call the label battle with 2 actor objects: player and enemy.
    call battle(hero,goblin)
