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

    "After getting infected with a lethal dose of poison from swallowing a yummy looking mushroom I now have only 20 days left to live"

    "I have been a paladin of the most esteemed order of Mithras, so I ought to spend the rest of my days in prayer, but..."

    "There is no easy way to say this. I realized something"

    "If ten small days, thou let'st slip,\n
    Like water from thy fingertips.\n
    Now shadows stretch, the stars align...\n
    Thou didst die once… now a second time."

    # We jump to day to start the first day.
    jump day


# This is the label that is jumped to at the start of a day.
label day:

    # Increment the day it is.
    $ day += 1

    # We may also want to compute the name for the day here, but
    # right now we don't bother.

    "It's day %(day)d."

    # Here, we want to set up some of the default values for the
    # day planner. In a more complicated game, we would probably
    # want to add and remove choices from the dp_ variables
    # (especially dp_period_acts) to reflect the choices the
    # user has available.


    window hide

    $ day_act = None
    call screen day_planner(["Whole day"])
    window auto

    $ period = "day"
    $ act = day_act
    call events_run_period


label night:

    # This is now the end of the day, and not a period in which
    # events can be run. We put some boilerplate end-of-day text
    # in here.

    centered "Night"

    "It's getting late, so I decide to go to sleep."

    # We call events_end_day to let it know that the day is done.
    call events_end_day

    # And we jump back to day to start the next day. This goes
    # on forever, until an event ends the game.
    jump day
         

