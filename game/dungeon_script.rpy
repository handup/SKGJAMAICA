# This file is in the public domain.

label dungeon_start:
    
    play music "dungeon.ogg"
    # Initializing data
    python:
        level = 1
        # Create skills (name, type, hit, power)
        attack = Skill("Attack", "attack", 50 + dexterity / 2, strength)
        goblin_attack = Skill("Attack", "attack", 70, 10 - stamina / 10)
        escape = Skill("Escape", "escape")
        
        # Create battle actors (name, max_hp, skills)
        hero = Actor("Hero", 100 + stamina, [attack,escape])
        goblin = Actor("Goblin", 40, [goblin_attack])
        goblin.image = "images/goblin.webp"
        
        # Create a dungeon stage (map,enemy)
        # "1" means wall, "0" means path. 
        stage1=Stage([
            "1111111111",
            "1111011001",
            "1000000001",
            "1110111101",
            "h000000001",
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
    call battle(hero, goblin)

label dungeon_2:
    
    # Initializing data
    python:
        # Create skills (name, type, hit, power)
        attack = Skill("Attack", "attack", 50 + dexterity / 2, strength)
        goblin_attack = Skill("Attack", "attack", 70, 10 - stamina / 10)
        escape = Skill("Escape", "escape")
        
        # Create battle actors (name, max_hp, skills)
        hero = Actor("Hero", 100 + stamina, [attack,escape])
        goblin = Actor("Goblin", 40, [goblin_attack])
        goblin.image = "images/goblin.webp"
        
        # Create a dungeon stage (map,enemy)
        # "1" means wall, "0" means path. 
        stage2=Stage([
            "111111111111",
            "111101100111",
            "1001h0000011",
            "100111101111",
            "100000000001",
            "111111111111",
            ],
            enemy=goblin)
            
    # The game starts here.
    
    # Place a player position on a dungeon stage (stage,y,x,dy,dx).
    # dx,dy means direction. If dy=1, it's down. If dx=-1, it's left.
    $ here=Coordinate(stage2,2,2,0,1) 
    
    # To start exploring, call or jump to the label dungeon. 
    call dungeon
    
    # To start battling, call the label battle with 2 actor objects: player and enemy.
    call battle(hero, goblin)

label dungeon_3:
    
    # Initializing data
    python:
        
        # Create skills (name, type, hit, power)
        attack = Skill("Attack", "attack", 50 + dexterity / 2, strength)
        goblin_attack = Skill("Attack", "attack", 70, 10 - stamina / 10)
        escape = Skill("Escape", "escape")
        
        # Create battle actors (name, max_hp, skills)
        hero = Actor("Hero", 100 + stamina, [attack,escape])
        goblin = Actor("Goblin", 40, [goblin_attack])
        goblin.image = "images/goblin.webp"
        
        # Create a dungeon stage (map,enemy)
        # "1" means wall, "0" means path. 
        stage3=Stage([
            "1111111111h1",
            "100000001101",
            "100100001101",
            "100111101101",
            "110001100001",
            "111111111111",
            ],
            enemy=goblin)
            
    # The game starts here.
    
    # Place a player position on a dungeon stage (stage,y,x,dy,dx).
    # dx,dy means direction. If dy=1, it's down. If dx=-1, it's left.
    $ here=Coordinate(stage3,2,2,0,1) 
    
    # To start exploring, call or jump to the label dungeon. 
    call dungeon
    
    # To start battling, call the label battle with 2 actor objects: player and enemy.
    call battle(hero, goblin)