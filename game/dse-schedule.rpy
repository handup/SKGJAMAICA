# The Dating Sim Engine was written by PyTom, 
# with updates added by Andrea Landaker (qirien),
# and contributions by Edmund Wilfong (Pneumonica)
#
# For support, see the Lemma Soft forums thread:
# http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=31571
#
# It is released under the MIT License - see DSE-LICENSE.txt
#
#
# This is the main part of the program, where you setup your schedule and
# the options for the user. You can change the stats, periods, and choices
# here; just make sure they match up with the events setup in
# dse-events.rpy.  You can even have different time periods (months, instead
# of times of day, for example).

# Set up a default schedule.
init python:
    register_stat("Strength", "strength", 30, 100)
    register_stat("Dexterity", "dexterity", 10, 100)
    register_stat("Stamina", "stamina", 20, 100)
    register_stat("Hit points", "hitpoints", 120, 200)

    dp_period("Whole day", "day_act")
    dp_choice("Go In Dungeon", "dungeon_start")
    dp_choice("Strength Training", "train")
    dp_choice("Practice Footwork", "footwork")

    dp_choice("Go running", "running")
    dp_choice("Rest in", "rest")
    sower = Character("Sower of Seeds", color="#009900")
    you = Character("You", color="#e8e7ec")
    lemon = Character("Lemon trees", color="#d2ee1e")
    trainingFlag = False
    strengthFlag = False
    dexterityFlag = False    

# This is the entry point into the game.
label start:
    play music "town.ogg"
    # Initialize the default values of some of the variables used in
    # the game.
    $ day = 0

    image club = "images/town.jpg"
    # Show a default background.
    scene club

    # The script here is run before any event.

    "You've awoken for the first time in a town whose name you do not know. To your surprise you are alive."

    "Inside of the houses you can see lights but no people. There are, however, gardens filled with lemon trees."

    "The fruits shine yellow, like globes. You feel like you are here to pick these lemons and gather them."

    "As you pluck the first fruit you hear the leaves rusting in the wind as if a voice spoke."

    lemon "If ten small days, thou let'st slip,\n
    Like water from thy fingertips.\n
    Now shadows stretch, the stars align...\n
    Thou didst die once… now a second time."

    "Ten days does not feel like a long time. I better make them count."

    # We jump to day to start the first day.
    jump day


# This is the label that is jumped to at the start of a day.
label day:

    # Increment the day it is.
    $ day += 1

    # We may also want to compute the name for the day here, but
    # right now we don't bother.

    scene black
    centered "It's day %(day)d."
    scene club

    # Here, we want to set up some of the default values for the
    # day planner. In a more complicated game, we would probably
    # want to add and remove choices from the dp_ variables
    # (especially dp_period_acts) to reflect the choices the
    # user has available.

    "I spend the better part of the day plucking and gathering the lemons, but I still have time to do some other things."
    window hide

    if day > 10 or hitpoints < 1:
        jump endingA
    $ day_act = None
    call screen day_planner(["Whole day"])
    window auto

    $ period = "day"
    $ act = day_act
    call events_run_period from _call_events_run_period


label night:

    # This is now the end of the day, and not a period in which
    # events can be run. We put some boilerplate end-of-day text
    # in here.

    scene black
    centered "Night"
    scene club

    "It's getting late, so I decide to go to sleep."

    # We call events_end_day to let it know that the day is done.
    call events_end_day from _call_events_end_day

    # And we jump back to day to start the next day. This goes
    # on forever, until an event ends the game.
    jump day
         
label endingA:
    "You've done your job taking care of these lemon trees." 
    "But now the work is done and there is no other reason to be here"
    image druidess = Transform("images/druidess.png", zoom=1.25)
    show druidess
    sower "It is time. If you had chosen differently, perhaps we would meet in better circumstances"
    "You feel swallowed by the void..."
    $ MainMenu(confirm=False)()