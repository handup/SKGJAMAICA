﻿# This file is in the public domain.

init -1 python:
    
    from copy import copy
        
    class Skill(object):        
        
        '''            
        Class used for battle skills
        '''    
        
        def __init__(self, name, type, hit=0, power=0):
            self.name = name
            self.type = type
            self.hit = hit
            self.power = power        
            
    class Actor(object):        
        
        '''
        Class used for battle characters.
        '''        
        
        def __init__(self, name, max_hp=0, skills=[]):
            self.name=name
            self.max_hp=max_hp
            self.hp=max_hp
            self.skills = skills
                        
        def attack(self,skill,target):
            if self.skill.hit < renpy.random.randint (0,100):
                narrator ("{} dodged {}'s attack".format(target.name,self.name))
            else:
                target.hp -= self.skill.power
                narrator ("{} got {} damage".format(target.name, self.skill.power))                
                
screen battle_ui:    
    # Screen which shows battle status
    
    use battle_frame(char=player, position=(.95,.05))
    use battle_frame(char=enemy, position=(.05,.05))
    
screen battle_frame(char,position):
    # Screen included in the battle_ui screen
    
    frame xysize(180, 80) align position:
        vbox yfill True:
            text "[char.name]"
            hbox xfill True:
                text "HP"
                text "[char.hp]/[char.max_hp]" xalign 1.0
                
screen command_screen:    
    # Screen used for selecting skills
    
    vbox style_group "skill" align (.1,.8):
        for i in player.skills:
            textbutton "[i.name]" action Return (value=i)

style skill_button_text:
    size 40
    xminimum 200
                
label battle(player, enemy):
    # To start battling, call this label with 2 actor objects: player and enemy.
    
    # Preparation
    # Copying enemy object prevents modifying an original data.
    $ enemy=copy(enemy) 
    $ _rollback=False
    "[enemy.name] appeared"
    show image [enemy.image]
    window hide
    show screen battle_ui

    # Main phase
    call _battle(player, enemy)
    
    # Result
    if _return is "lose":
        "Gameover"
        $renpy.full_restart()
    elif _return is "win":
        "You won"
    elif _return is "escape":
        "You escaped back to town"
        hide screen battle_ui
        hide image [enemy.image]
        play music "town.ogg"
        scene club
        jump night        
    hide screen battle_ui
    hide image [enemy.image]
    $ _rollback=True
    return
    
label _battle(player, enemy):
    # A sub label used in the battle label.
    
    while True: 
        $ player.skill = renpy.call_screen("command_screen")
        $ enemy.skill = renpy.random.choice(enemy.skills)
        if player.skill.type=="escape":
            return "escape"
        $ player.attack(player.skill, enemy)
        if enemy.hp < 1:  
            return "win"
        $ enemy.attack(enemy.skill, player)
        if player.hp < 1:
            return "lose"
